# FXHoudini-MCP 项目分析文档

  

## 项目概述

  

**FXHoudini-MCP** 是 SideFX Houdini 最全面的 MCP (Model Context Protocol) 服务器，由 [Valentin Beaumont (healkeiser)](https://github.com/healkeiser) 开发，MIT 许可证。它让 AI 助手（如 Claude）通过自然语言控制 Houdini 的场景搭建、模拟、渲染等工作。

  

| 指标 | 数值 |

|------|------|

| MCP 工具数 | 179 个，覆盖 22 个类别 |

| MCP 资源数 | 8 个（场景、几何体、USD） |

| MCP 提示模板 | 6 个工作流 |

| Python 版本 | 3.10+ |

| Houdini 版本 | 20.5+（实测 21.0） |

| 核心依赖 | MCP SDK ≥ 1.8.0, httpx ≥ 0.27.0, pydantic ≥ 2.0.0 |

  

---

  

## 核心架构（三层设计）

  

```

AI 客户端（Claude Desktop / VS Code / Claude Code）

       │  MCP 协议 · stdio

       ▼

┌─ FXHoudini MCP 服务器 (独立 Python 进程) ───────────────┐

│  FastMCP · 179 tools · 8 resources · 6 prompts        │

│  bridge.py  ←→  HTTP / JSON  ←→  port 8100            │

└────────────────────────────────────────────────────────┘

       │  HTTP POST /api

       │  Content-Type: application/x-www-form-urlencoded

       │  Body: json=["mcp.execute", [], {"command": "...", ...}]

       ▼

┌─ SideFX Houdini 内部 ──────────────────────────────────┐

│  hwebserver (内置)                                       │

│    → dispatcher (主线程调度)                              │

│      → hou.* Handlers (22 个 handler 模块)              │

│  使用 hdefereval.executeInMainThreadWithResult()         │

└────────────────────────────────────────────────────────┘

```

  

### 关键设计决策

  

1. **使用 Houdini 内置 hwebserver**：不引入自定义 socket 服务器、不用 rpyc，零额外依赖。Houdini 原生支持 `@hwebserver.apiFunction` 装饰器注册 API 端点。

  

2. **hdefereval 主线程调度**：Houdini 的 `hou.*` API 必须在主线程执行，但 hwebserver 的 handler 运行在 worker 线程上。dispatcher 通过 `hdefereval.executeInMainThreadWithResult()` 将调用封送到主线程，并有 120 秒超时保护。无头模式（hython）下自动切换为直接执行。

  

3. **JSON-RPC 风格通信**：POST `{"json": "[\"namespace.function\", [], {kwargs}]"}` 到 `/api`，返回统一格式：

   ```json

   {"status": "success", "data": {...}, "request_id": "...", "timing_ms": 12.5}

   ```

  

4. **原子化网络构建 + 预验证**：`build_network` 先实例化每种节点类型作为"探针"获取参数名集合，验证所有类型名、参数名、输入引用后，才批量创建。失败自动回滚。

  

---

  

## 目录结构

  

```

fxhoudinimcp-main/

├── python/fxhoudinimcp/          # MCP 服务端（独立 Python 进程）

│   ├── server.py                 # FastMCP 定义 + lifespan 管理

│   ├── bridge.py                 # 异步 HTTP 客户端，连接 Houdini

│   ├── config.py                 # 环境变量读取（FXHOUDINIMCP_AUTO_LAYOUT）

│   ├── errors.py                 # 异常层次结构

│   ├── protocol.py               # Request/Response 数据类 + ErrorCode

│   ├── _types.py                 # Value 类型别名（JSON 兼容值）

│   ├── _loader.py                # Markdown 提示文件加载 + 缓存

│   ├── tools/                    # 23 个工具模块

│   │   ├── __init__.py           # 注册所有工具 + result_with_image()

│   │   ├── graph.py              # 图智能（build_network 等 4 个工具）

│   │   ├── nodes.py              # 节点操作（17 个工具）

│   │   ├── parameters.py         # 参数操作（11 个工具）

│   │   ├── geometry.py           # 几何体/SOP（12 个工具）

│   │   ├── lops.py               # LOPs/USD（18 个工具）

│   │   ├── dops.py               # DOPs/模拟（8 个工具）

│   │   ├── tops.py               # PDG/TOPs（10 个工具）

│   │   ├── cops.py               # COPs（7 个工具）

│   │   ├── chops.py              # CHOPs（4 个工具）

│   │   ├── hda.py                # HDAs（10 个工具）

│   │   ├── animation.py          # 动画（9 个工具）

│   │   ├── rendering.py          # 渲染（9 个工具）

│   │   ├── vex.py                # VEX（5 个工具）

│   │   ├── code.py               # 代码执行（4 个工具）

│   │   ├── viewport.py           # 视口/UI（13 个工具）

│   │   ├── context.py            # 场景上下文（8 个工具）

│   │   ├── workflows.py          # 高层工作流（8 个工具）

│   │   ├── materials.py          # 材质（5 个工具）

│   │   ├── cache.py              # 缓存管理（4 个工具）

│   │   ├── takes.py              # Takes（4 个工具）

│   │   ├── scene.py              # 场景管理（7 个工具）

│   │   └── help.py               # 帮助文档查询（2 个工具）

│   ├── resources/                # MCP 资源定义

│   │   ├── scene_resources.py

│   │   ├── geo_resources.py

│   │   └── usd_resources.py

│   ├── prompts/                  # MCP 提示模板

│   │   ├── workflows.py          # 6 个工作流 Prompt 注册

│   │   └── markdown/             # 8 个 Markdown 模板文件

│   └── __main__.py               # 入口点

│

├── houdini/                      # Houdini 内插件（安装到 Houdini 的包目录）

│   ├── fxhoudinimcp.json         # Houdini 包描述符

│   ├── scripts/python/fxhoudinimcp_server/

│   │   ├── __init__.py

│   │   ├── hwebserver_app.py     # hwebserver API 端点注册（/api）

│   │   ├── dispatcher.py         # 主线程命令调度器

│   │   ├── config.py             # 环境变量读取（Houdini 内版本）

│   │   └── handlers/             # 22 个 handler 模块

│   │       ├── __init__.py       # 动态加载所有 handler 模块

│   │       ├── graph_handlers.py # 图智能 handler（核心）

│   │       ├── node_handlers.py  # 节点操作 handler

│   │       ├── ...               # 其他 handler

│   │       └── workflow_handlers.py

│   ├── python3.9libs/uiready.py  # UI 就绪检测（Python 3.9）

│   ├── python3.10libs/uiready.py # UI 就绪检测（Python 3.10）

│   ├── python3.11libs/uiready.py # UI 就绪检测（Python 3.11）

│   └── toolbar/fxhoudinimcp.shelf # Shelf 工具

│

├── tests/                        # 测试

│   ├── conftest.py               # 共享 fixtures（mock_bridge, mock_ctx）

│   ├── test_bridge.py            # 桥接器单元测试

│   ├── test_*.py                 # 其他单元测试

│   ├── run_integration.py        # 集成测试启动器（自动查找 hython）

│   └── integration/              # 集成测试（需真实 Houdini 许可证）

│       ├── test_nodes_live.py

│       ├── test_graph_live.py

│       └── ...

│

├── docs/                         # MkDocs 文档站

│   ├── .scripts/generate_technical_docs.py

│   └── ...

├── mkdocs.yml                    # MkDocs 配置

├── pyproject.toml                # Python 包配置（hatchling）

└── package.json                  # 仅用于 auto-changelog

```

  

---

  

## 通信流程详解

  

### 一次完整的工具调用

  

```

1. AI 客户端发起 MCP 工具调用

     ↓

2. FastMCP 调度到对应的 tool 函数（如 create_node）

     ↓

3. tool 函数从 Context 提取 HoudiniBridge

     ↓

4. bridge.execute("nodes.create_node", {params})

     ↓  HTTP POST http://localhost:8100/api

     ↓  Body: {"json": "[\"mcp.execute\", [], {\"command\": \"nodes.create_node\", ...}]"}

     ↓

5. Houdini hwebserver 接收请求

     ↓

6. hwebserver_app.py 的 mcp.execute() 被调用

     ↓

7. dispatcher.dispatch(command, params)

     ↓  hdefereval.executeInMainThreadWithResult(_execute)

     ↓  主线程执行 handler(**params)

     ↓

8. handler 调用 hou.* API，返回 dict

     ↓

9. 响应沿原路返回，附带 timing_ms

```

  

### 注册机制

  

```python

# Handler 端 (Houdini 内) — 模块导入时注册

from fxhoudinimcp_server.dispatcher import register_handler

  

def create_node(parent_path, node_type, ...):

    ...

  

register_handler("nodes.create_node", create_node)  # 命令名 → 函数

  

# Tool 端 (MCP 进程) — 装饰器在导入时注册

@mcp.tool()

async def create_node(ctx, parent_path, node_type, ...):

    bridge = _get_bridge(ctx)

    return await bridge.execute("nodes.create_node", params)

```

  

---

  

## 核心亮点功能

  

### 1. 图智能工具 (`graph.py`)

  

这是项目最核心的特性，体现"资深艺术家工作流"：

  

| 工具 | 用途 |

|------|------|

| `build_network` | 原子化构建整个节点网络，预验证所有类型/参数/连接，失败自动回滚 |

| `verify_network` | 一键检查所有节点错误/警告/标志 + 几何体计数（"中键检查一切"） |

| `get_node_card` | 从 Houdini 内置 `nodes.zip` 提取节点文档：真实参数名/默认值/菜单/连接器 |

| `find_expensive_nodes` | 使用 `hou.perfMon` 做性能剖析，按耗时排序节点 |

  

**`build_network` 的三阶段执行**：

  

- **Phase 1 — 验证**：解析所有 spec，检查父路径是否存在、类型名是否合法（用 `get_close_matches` 给出建议）、参数名是否匹配（实例化探针节点获取真实参数集合）、输入引用是否可解析。任一失败返回完整错误列表。

- **Phase 2 — 构建**：原子创建所有节点 → 设置参数 → 连线 → 设置标志/颜色/注释。任何异常触发回滚。

- **Phase 3 — 验证**：cook 显示节点，返回每个节点的错误报告 + 几何体计数。

  

### 2. 参数探针机制

  

`build_network` 在正式创建节点前，对每种唯一类型实例化一个临时节点：

```python

probe = parent.createNode(node_type.name())  # 创建探针

parm_names = {p.name() for p in probe.parms()}  # 记录参数名

tuple_names = {pt.name() for pt in probe.parmTuples()}  # 记录参数组名

probe.destroy()  # 立即销毁

```

这确保了参数验证 100% 准确，错误的参数名会得到 "Did you mean: [...]?" 建议。

  

### 3. 参数广播

  

`_apply_parm` 支持标量自动广播到多分量参数：

```python

# 设置单个值到 float3 → 自动广播为 [v, v, v]

_apply_parm(node, "t", 5.0)  # → parmTuple.set([5.0, 5.0, 5.0])

```

  

### 4. 截图嵌入

  

`result_with_image()` 将 handler 返回的 `image_base64` 转换为 MCP `ImageContent`，截图直接显示在 AI 客户端中，无需打开外部文件。

  

### 5. 节点文档提取

  

`get_node_card` 直接从 Houdini 安装目录的 `$HFS/houdini/help/nodes.zip` 提取文档，支持带版本号和不带版本号的查找（如 `copytopoints::2.0` → `copytopoints.txt`），并缓存 zip 索引。

  

---

  

## 工具模块完整清单

  

| 类别 | 模块 | 工具数 | 关键工具 |

|------|------|--------|----------|

| 图智能 | `graph.py` | 4 | build_network, verify_network, get_node_card, find_expensive_nodes |

| 节点操作 | `nodes.py` | 17 | create_node, delete_node, connect_nodes, set_node_flags, layout_children |

| 参数 | `parameters.py` | 11 | set_parameter, set_parameters, create_spare_parameter, link_parameters |

| 几何体/SOP | `geometry.py` | 12 | get_geometry_info, get_points, sample_geometry, find_nearest_point |

| LOPs/USD | `lops.py` | 18 | get_stage_info, list_usd_prims, create_light, create_light_rig |

| DOPs/模拟 | `dops.py` | 8 | get_simulation_info, list_dop_objects, step_simulation, get_sim_memory_usage |

| PDG/TOPs | `tops.py` | 10 | cook_top_node, get_pdg_graph, get_work_item_states |

| COPs | `cops.py` | 7 | create_cop_node, get_cop_layer, get_cop_vdb |

| HDAs | `hda.py` | 10 | create_hda, install_hda, get_hda_sections, set_hda_section_content |

| 动画 | `animation.py` | 9 | set_keyframe, set_keyframes, playbar_control, delete_keyframe |

| 渲染 | `rendering.py` | 9 | start_render, capture_screenshot, render_viewport, setup_render |

| VEX | `vex.py` | 5 | create_wrangle, set_wrangle_code, validate_vex |

| 代码执行 | `code.py` | 4 | execute_python, execute_hscript, evaluate_expression |

| 视口/UI | `viewport.py` | 13 | set_viewport_direction, set_viewport_display, log_status |

| 场景上下文 | `context.py` | 8 | get_scene_summary, get_network_overview, find_error_nodes |

| 工作流 | `workflows.py` | 8 | setup_pyro_sim, setup_rbd_sim, setup_flip_sim, setup_vellum_sim, build_sop_chain |

| 材质 | `materials.py` | 5 | create_material, assign_material, list_materials, get_material_info |

| CHOPs | `chops.py` | 4 | create_chop_node, get_chop_data, export_chop_to_parm |

| 缓存 | `cache.py` | 4 | list_caches, get_cache_status, write_cache, clear_cache |

| Takes | `takes.py` | 4 | list_takes, create_take, set_current_take, get_current_take |

| 场景管理 | `scene.py` | 7 | get_scene_info, save_scene, load_scene, import_file, export_file |

| 帮助文档 | `help.py` | 2 | search_help, get_help_page |

  

---

  

## 工作流提示模板

  

`prompts/workflows.py` 注册了 6 个 MCP Prompt，引导 AI 完成特定任务：

  

| Prompt | 用途 |

|--------|------|

| `procedural_modeling_workflow` | 程序化建模网络搭建 |

| `usd_scene_assembly` | Solaris/USD 场景装配 |

| `simulation_setup` | Pyro/FLIP/RBD/Vellum/POP 模拟搭建 |

| `pdg_pipeline` | PDG/TOPs 管线构建 |

| `hda_development` | 数字资产（HDA）创建 |

| `debug_scene` | 场景错误系统性排查 |

  

每个 Prompt 从 `prompts/markdown/*.md` 加载模板，支持 `{placeholder}` 替换，并自动注入 `layout_guidance`。

  

---

  

## 值得学习的架构模式

  

### 1. 工具端/Handler 端分离

MCP 工具函数（独立 Python 进程）是薄包装 → `bridge.execute(command, params)` → Handler 函数（Houdini 内执行 `hou.*`）。清晰的责任边界：工具端负责参数校验和 MCP 协议适配，Handler 端负责实际的 Houdini API 调用。

  

### 2. 命令注册 + 中央路由

```python

# Handler 端声明

register_handler("nodes.create_node", create_node)

  

# 中央路由

dispatcher.dispatch(command, params) → 查找 handler → 执行 → 返回

```

  

### 3. 优雅的模块加载

`handlers/__init__.py` 使用 `importlib.import_module` 动态加载所有 handler 模块，加载失败不阻断其他模块：

```python

for _module_name in _HANDLER_MODULES:

    try:

        importlib.import_module(f".{_module_name}", __package__)

        _loaded.append(_module_name)

    except Exception:

        _failed.append(_module_name)

```

  

### 4. 环境变量分层读取

`config.py` 在 Houdini 内通过 `hou.getenv()` 读取（支持 `houdini.env` 配置和运行时 `hou.putenv`），在 MCP 端通过 `os.getenv()` 读取：

  

- `FXHOUDINIMCP_AUTO_LAYOUT` — 控制自动节点排版（0=禁用）

- `FXHOUDINIMCP_PORT` / `HOUDINI_PORT` — 端口对齐

- `FXHOUDINIMCP_AUTOSTART` — 控制插件自动启动

  

### 5. 异常层次结构

```python

FXHoudiniError (code, details)

├── ConnectionError     # 无法连接 Houdini

├── NodeNotFoundError   # 节点路径不存在

├── InvalidParameterError

├── GeometryError

├── USDError

├── CookError

├── TimeoutError

└── HoudiniCommandError # Houdini 端返回的错误

```

  

---

  

## 关键通信协议

  

### 错误码定义 (`protocol.py`)

  

```python

class ErrorCode:

    NODE_NOT_FOUND = "NODE_NOT_FOUND"

    INVALID_PARAMETER = "INVALID_PARAMETER"

    GEOMETRY_ERROR = "GEOMETRY_ERROR"

    USD_ERROR = "USD_ERROR"

    COOK_ERROR = "COOK_ERROR"

    PERMISSION_ERROR = "PERMISSION_ERROR"

    TIMEOUT_ERROR = "TIMEOUT_ERROR"

    UNKNOWN_COMMAND = "UNKNOWN_COMMAND"

    CONNECTION_ERROR = "CONNECTION_ERROR"

    DISPATCH_ERROR = "DISPATCH_ERROR"

    INVALID_REQUEST = "INVALID_REQUEST"

```

  

### Request/Response 数据类

  

```python

@dataclass

class Request:

    command: str          # "nodes.create_node"

    params: dict          # {"parent_path": "/obj/geo1", "node_type": "box"}

    request_id: str       # UUID

  

@dataclass

class Response:

    status: str           # "success" | "error"

    data: dict | None

    error: dict | None    # {"code": "...", "message": "...", "traceback": "..."}

    request_id: str

    timing_ms: float

```

  

---

  

## 已知改进空间

  

1. **版本号重复定义**：`__init__.py` 中 `__version__ = "0.1.0"`，`pyproject.toml` 使用 VCS 动态版本 — 两处可能不一致

2. **Handler 模块列表硬编码**：`handlers/__init__.py` 的 `_HANDLER_MODULES` 硬编码了 21 个模块名，新增 handler 需手动注册

3. **无 WebSocket 实时推送**：纯 HTTP 轮询，无法实时推送渲染进度或模拟步骤

4. **hwebserver 依赖图形界面**：`hdefereval` 在 hython 无头模式下不可用（但有 fallback 直接执行）

5. **无连接池**：`HoudiniBridge` 使用单一 `httpx.AsyncClient`，高并发场景可能有瓶颈


## fxhoudinimcp 实现原理

fxhoudinimcp 是一个三层架构的 MCP 服务器，让 AI（如 Claude）能通过自然语言控制 Houdini。下面按数据流方向逐层分析。

---

### 整体架构

```
Claude Desktop / Claude Code
       ↕ MCP 协议 (stdio)
fxhoudinimcp（独立 Python 进程）
       ↕ HTTP / JSON（端口 8100）
Houdini 内置 hwebserver
       ↕ hdefereval.executeInMainThreadWithResult()
Houdini hou.* API（主线程执行）
```

---

### 第一层：MCP Server（`python/fxhoudinimcp/`）

这是一个**独立的 Python 进程**，基于 FastMCP 框架构建。它对外暴露了 **179 个工具**，这些工具覆盖了 Houdini 的几乎所有上下文（SOP、LOP、DOP、TOP、COP、CHOP、VEX、HDAs 等）。

- **职责**：接收 AI 客户端的 MCP 协议请求（如 "创建一个 Box 节点"），解析后转换为结构化的 JSON 命令
- **关键模块** `bridge.py`：异步 HTTP 客户端，负责将 JSON 命令发送到 Houdini，并反序列化返回结果，处理连接异常和超时

核心逻辑是：AI 说 "Create a box" → MCP Server 把这个意图翻译成 `{"tool": "create_node", "params": {"node_type": "box", ...}}` 这样的 JSON，然后通过 HTTP POST 发给 Houdini。

---

### 第二层：Houdini 插件（`houdini/`）

这部分运行在 **Houdini 内部的 Python 环境**里，利用了 Houdini 自带的 `hwebserver`。

**启动机制**：
- `python3.Xlibs/uiready.py`：当 Houdini UI 就绪后自动启动，通过 `FXHOUDINIMCP_AUTOSTART` 环境变量控制
- 也可以手动通过 shelf 工具切换

**请求处理**：
- 注册了 `@hwebserver.apiFunction` 装饰器标记的 HTTP 端点，接收 MCP Server 发来的 JSON 命令
- **关键设计**：使用 `hdefereval.executeInMainThreadWithResult()` 将所有 `hou.*` API 调用安全地调度到 Houdini 的主线程执行

这是整个架构最精妙的地方——**Houdini 的 Python API (`hou.*`) 不是线程安全的**，必须在主线程调用。`hdefereval` 正是 Houdini 官方提供的将代码从后台线程调度到主线程的机制。

---

### 第三层：Houdini API（`hou.*`）

插件收到命令后，调用 Houdini 的 Python API 执行实际操作：
- **节点操作**：`hou.node().createNode()` 创建节点，`node.setInput()` 连接节点
- **参数设置**：`parm.set()` 设置参数值
- **几何体操作**：读取点、面、属性数据
- **场景管理**：打开/保存文件、导入/导出

---

### 为什么不用自定义 Socket / rpyc？

作者明确指出：**不自定义 Socket 服务器，不用 rpyc**。原因是：

| 方案 | 问题 |
|----|----|
| 自定义 Socket | 需要自己处理 Houdini 主线程调度，容易出 bug |
| rpyc | 不是线程安全的，Houdini 的 API 调用可能崩溃 |
| **hwebserver + hdefereval** | Houdini 自带，官方维护，天然线程安全 |

---

### 一个完整调用的数据流

以 "创建一个 Box 节点" 为例：

```
1. 用户/Claude: "Create a box node"
       ↓
2. MCP Server（fxhoudinimcp 进程）:
   解析意图 → 构造 JSON:
   {"command": "create_node", "parent_path": "/obj/geo1", "node_type": "box"}
       ↓ HTTP POST localhost:8100
3. Houdini hwebserver 接收到请求
       ↓ hdefereval.executeInMainThreadWithResult()
4. Houdini 主线程:
   hou.node("/obj/geo1").createNode("box")
       ↓ 返回结果
5. MCP Server 收到响应 → 格式化 → 返回给 AI
       ↓
6. AI: "已成功创建 box1 节点"
```

---

### 与同类项目的对比

你在 `[[Houdini AI Agent 相关项目与工具.md]]` 中记录了完整的生态对比。fxhoudinimcp 的核心优势是：

- **工具数量最多**（179 个 → 你在笔记里记的 168 个已经过时了，项目又更新了）
- **覆盖最全**：不仅是 SOP，LOP/USD、DOP、PDG/TOP、COP、HDA 管理全都有
- **架构最干净**：完全依赖 Houdini 内置设施（hwebserver + hdefereval），没有外部依赖或自定义通信协议
- **先天支持 AI 代码执行**：通过 VEX、Python、HScript 三类代码执行工具，AI 可以编写并运行自定义代码，弥补预置工具覆盖不到的边缘场景



---
---

# 面试回答版（简化）


## 一句话

**fxhoudinimcp 是目前最全面的 Houdini MCP Server——179 个工具覆盖所有 Houdini 上下文，让 Claude 通过自然语言直接操控 Houdini。**


## 3 分钟面试回答

### 它解决什么问题？

Houdini 的 `hou.*` Python API 不是线程安全的，必须在主线程调用。但 MCP Server 是独立进程，天然不在 Houdini 主线程。这个矛盾是所有 Houdini AI 工具的核心难点。fxhoudinimcp 用 Houdini 官方基础设施干净地解决了它。

### 三层架构（每一层都踩在官方肩膀上）

```
Claude / Claude Code
       ↕ MCP 协议（stdio）
MCP Server（独立 Python 进程，基于 FastMCP）
       ↕ HTTP / JSON（localhost:8100）
Houdini hwebserver（Houdini 自带的 Web 服务器）
       ↕ hdefereval.executeInMainThreadWithResult()
hou.* API（在主线程安全执行）
```

| 层 | 技术 | 为什么这样选 |
|----|------|-------------|
| **第一层：MCP Server** | FastMCP 框架 | 179 个工具统一注册，把 AI 意图翻译成结构化 JSON |
| **第二层：Houdini 插件** | `hwebserver` + `@hwebserver.apiFunction` | Houdini 自带 Web 服务，零外部依赖 |
| **第三层：线程调度** | `hdefereval.executeInMainThreadWithResult()` | Houdini 官方 API，把后台线程的 `hou.*` 调用安全地调度到主线程 |

### 核心精妙之处：线程安全

作者明确拒绝了自定义 Socket 和 rpyc——前者需要自己处理主线程调度，后者不是线程安全的。`hwebserver` + `hdefereval` 是 Houdini 官方提供并维护的设施，天然可靠。

### 工具覆盖（179 个，22 个类别）

| 类别 | 覆盖 |
|------|------|
| SOP 几何操作 | 创建、连接、参数、属性、分组、采样 |
| LOP/USD | Stage 检查、Prim 操作、Layer、变体、灯光 |
| DOP 模拟 | Pyro/RBD/FLIP/Vellum 一键搭建、步进、内存分析 |
| PDG/TOP | Cook、工作项、调度器、依赖图 |
| VEX | 创建/编辑 Wrangle，验证 VEX 代码 |
| 代码执行 | Python、HScript、表达式 eval |
| 视口/渲染 | 截图、预览、Karma 渲染配置 |
| HDA | 创建、安装、管理数字资产 |
| COP/CHOP | 图像处理、通道数据 |

### 关键设计决策

- **build_network 原子构建**：3 个以上节点一次性提交，先 `dry_run` 验证，比逐个创建快 10 倍
- **verify_network**：每次构建后自动检查所有节点错误，像艺术家手动中键每个节点
- **get_node_card**：从运行中的 Houdini 取真实参数名，绝不猜参数
- **search_help + get_help_page**：查 Houdini 自带文档，不凭记忆写代码

### 和同类方案的对比

| | fxhoudinimcp | houdini2chat | Houdini Agent |
|---|---|---|---|
| 通信 | MCP 双向实时 | 文件导出 | Socket Bridge |
| 能改场景 | ✅ 全能 | ❌ 只读 | ✅ |
| 工具量 | 179（最全） | 无（纯导出） | 50+ |
| 门槛 | 需配置 MCP | 拖个 HDA | 装桌面程序 |
| 成熟度 | 成熟，有 CI | v0.1.0 PoC | 成熟，打包安装 |
| 架构哲学 | 依赖 Houdini 内置设施 | 最低摩擦 | 全功能 AI 协作平台 |

### 诚实说局限

- 需要配置 MCP 客户端（Claude Desktop / VS Code），对非技术用户有门槛
- 依赖 Houdini 的 hwebserver，端口冲突时需要手动调
- 连接断开需要重启 Houdini

### 我的理解

fxhoudinimcp 体现了**"用官方设施而非自己造轮子"**的工程智慧。作者面对 Houdini 线程安全这个硬问题，没有走自定义协议的老路，而是找到了 `hwebserver` + `hdefereval` 这条 Houdini 官方预埋的路径。179 个工具、dry_run 验证、真实文档查询——这些细节说明作者不是在"嫁接"AI，而是真正理解 Houdini 艺术家的心智模型，设计了符合他们工作习惯的工具集。
