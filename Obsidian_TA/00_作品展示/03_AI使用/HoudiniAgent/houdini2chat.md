# Houdini2Chat 项目分析

  

## 一句话概括

  

**Houdini2Chat** 是一个 Houdini 数字资产（HDA），它能将 Houdini 节点网络导出为 **AI/LLM 友好的 Python 风格伪代码**，让艺术家可以直接把 Houdini 场景"喂"给 ChatGPT、Claude、Gemini 等 AI 工具理解和分析。

  

作者：**Michel Habib (RenderMagix)** | 版本：**v0.1.0** | 许可：开源

  

---

  

## 核心流程

  

```

Houdini 场景 (.hip)

       │

       ▼

HDA 遍历节点网络（/obj 下）

       │

       ▼

提取节点参数、连线、循环、分支、便签、网络框

       │

       ▼

Jinja2 模板渲染 → Python 风格伪代码 (.py)

       │

       ▼

复制粘贴到 AI 聊天 / VS Code Copilot

```

  

---

  

## 项目结构

  

```

houdini2chat/

├── .github/

│   ├── copilot-instructions.md          # Github Copilot 自定义指令

│   └── prompts/

│       └── .prompt.md                   # Copilot AI 编码助手提示

├── docs/

│   ├── DEV_README.md                    # 开发工具和 IDE 设置说明

│   ├── Evaluation.md                    # 多个 LLM 的详细评估结果

│   ├── presentation.md                  # 问题/解决方案架构推介文稿

│   └── images/                          # 评估和演示的截图/GIF

├── hda/

│   └── sop_rendermagix.houdini_2_chat.0.1.0.hdalc   # 打包的 HDA 文件

├── hda_scripts/                         # 嵌入在 HDA 中的 Python 模块

│   ├── PythonModule.py                  # 入口点：从 HDA 部分加载所有模块

│   ├── main.py                          # 主编排逻辑

│   ├── hda_manager.py                   # HDA 参数管理器和配置

│   ├── houdini_node_manager.py          # Houdini 节点查询工具

│   ├── gnode.py                         # 图形节点数据类（包装 hou.Node）

│   ├── node_graph.py                    # 图形构建、分解和渲染逻辑（~600行，最复杂）

│   ├── render_manager.py                # Jinja2 模板渲染和文件输出

│   ├── extract_functions.py             # 节点类型自省和代码生成

│   └── templates/                       # Jinja2 模板（7个 .j2 文件）

│       ├── network_full.py.j2           # 整个网络的顶层包装器

│       ├── network_unit.py.j2           # 单个网络单元（节点 + 分支）

│       ├── nodes_unit.py.j2             # 节点定义宏

│       ├── branches_unit.py.j2          # 分支连接定义

│       ├── loop_unit.py.j2              # 循环块包装器

│       ├── loop_branches.py.j2          # 循环内的分支连接

│       └── general_macros.py.j2         # 占位符页眉/页脚宏

├── tools/

│   ├── pyproject.toml                   # 可视化工具的 Poetry 配置

│   └── network_visualizer/              # 独立的 pyvis/networkx 可视化工具

│       ├── main.py                      # 网络可视化（读取 JSON，渲染为 HTML）

│       ├── parser.py                    # Houdini 文档解析器

│       └── test.py                      # 网络可视化基本测试

├── README.md

└── .gitignore

```

  

---

  

## 架构与数据流

  

### 五个阶段

  

| 阶段 | 描述 |

|------|------|

| **1. 节点发现与过滤** | HDAManager 读取 HDA 参数，HoudiniNodeManager 查询场景节点，按网络框过滤 |

| **2. 图形构建与分解** | NodeGraph 创建 GNode 字典，检测循环，分解多输入/多输出节点，分解为分支，分配便签 |

| **3. 属性提取** | 每个 GNode 通过 HoudiniNodeManager 提取参数：值、表达式、引用、未展开字符串、用户参数 |

| **4. Jinja2 渲染** | RenderManager 将数据输入 .j2 模板，特殊节点（attribwrangle、solver）有自定义宏 |

| **5. 文件输出** | .py 文件写入磁盘，支持按节点/按网络框命名 |

  

---

  

## 关键组件

  

### PythonModule.py — 入口点

HDA Python 模块部分，使用 `toolutils.createModuleFromSection()` 动态加载所有嵌入脚本。**当前有未提交的 bug 修复：** 修复了 `sys.modules["main"]` 被错误映射到 `extract_functions` 的问题。

  

### HDAManager — 集中式配置单例

读取所有 HDA 参数：项目位置、输出格式、网络框过滤、便签设置、调试标志。提供日志和文件管理方法。

  

### HoudiniNodeManager — Houdini API 门面

查询场景：获取节点子级、网络框、便签、过滤框、提取参数值/表达式/引用。处理复杂的参数元组逻辑。

  

### GNode — 轻量级节点数据类

包装 `hou.Node` 路径，存储：名称、类型、注释、输入、输出、位置、循环关联、便签文本和参数属性。

  

### NodeGraph — 核心图形引擎（~600 行）

1. 从节点列表构建有向图

2. 检测 `block_begin`/`block_end` 循环对

3. 分离循环到子图中

4. 处理多输出节点（插入 `@reference` 节点）

5. 可选地分解多输入节点

6. 通过遍历从根节点的出边将图形分解为分支

7. 通过接近度将便签分配给节点

  

### RenderManager — Jinja2 渲染器

从 HDA 嵌入部分加载模板，使用 `DictLoader` 解析 `{% include %}` 语句。支持自定义宏（如 `attribwrangle` 内联 VEX 代码）。

  

### ExtractFunctions — 节点类型自省

遍历 Houdini 的 `nodeTypeCategories` 并生成带有参数签名的 Python 函数定义，用于代码助手自动补全。

  

---

  

## HDA 参数（用户可配置）

  

| 类别 | 参数 |

|------|------|

| **网络框** | `group_by_network_box_l1`, `include_nodes_outside_boxes`, `filter_network_boxes`, `network_box_filter` |

| **便签** | `include_notes`, `link_sticky_notes_to_boxes`, 距离阈值, 位置设置 |

| **文件输出** | `project_location`, `break_by_node_path`, `break_by_network_box`, `auto_node_folder`, `default_filename_format`, `node_filename_format`, `netbox_filename_format` |

| **内容** | `header_text`, `footer_text`, `export_this_node` |

| **操作** | `action_selected`（0=无，1=导出，2/3=提取节点类型） |

| **高级** | `no_bmi`（跳过分解多输入）, `export_debug_files`, `print_debug_messages` |

| **节点选择** | `nodes_to_extract` + `node_path_N` 多重参数 |

  

---

  

## 评估结果（来自 Evaluation.md）

  

| 场景 | 复杂度 | 最佳表现模型 | 结果 |

|------|--------|--------------|------|

| xyzdist 演示（26 节点） | 简单 | Claude 3.7 Sonnet | 出色 |

| 8 数码游戏（10 节点） | 中等 | o3-mini-high / Claude | 需要提示才能获得动画逻辑 |

| 程序化汉堡（88 节点） | 困难 | Claude 3.7 Sonnet | 正确猜中 7 种食材中的 6 种 |

| 魔方 | 待定 | 多个 | 评估中 |

  

---

  

## 设计模式与亮点

  

- **HDA 作为分发机制**：所有 Python 代码嵌入在 `.hdalc` 文件内，一个文件就是一切

- **伪代码输出格式**：选择 Python 语法（`.py` 后缀），LLM 对 Python 训练最好，所有编辑器自动高亮

- **基于宏的模板化**：`nodes_unit.py.j2` 支持自定义宏（`attribwrangle`、`solver`），为特殊节点类型提供专门渲染

- **文件名标记系统**：`[node.name]`、`[netbox.name]` 等支持灵活的输出文件命名

  

---

  

## 已知限制

  

1. **仅 `/obj` 级别** — 不支持 `/mat`、`/stage`、`/out`、`/shop` 等

2. **不递归子网络** — 不展开嵌套子网络和 HDA 内部

3. **循环检测是启发式的** — 1000 个分支后强行停止（`node_graph.py` L278）

4. **没有自动化测试** — 核心 HDA 脚本缺乏测试覆盖

5. **HDAManager 被反复实例化** — 不是真正的单例，每次构造都重新读取 HDA 参数

6. **硬编码路径** — `tools/network_visualizer/` 中有绝对路径，在此仓库之外无法工作

  

---

  

## 当前状态

  

- **版本**: v0.1.0（2025年2月-3月）

- **Git 状态**: 有未提交修改

  - `hda_scripts/PythonModule.py`：修复了 `sys.modules["main"]` 被错误映射到 `extract_functions` 的 bug

- **最近提交**: 文档打磨、网络框 bug 修复、求解器节点模板、演示视频和社交媒体链接


---
---

# 面试回答版（简化）


## 一句话

**houdini2chat 是一个 Houdini HDA，把节点网络导出为 Python 风格的伪代码，让艺术家直接把场景丢给 ChatGPT/Claude 理解，不需要手动描述。**


## 3 分钟面试回答

### 它解决什么问题？

Houdini 场景动辄几十上百个节点，艺术家想向 AI 求助时，需要手动描述"我有个 Mountain 接了 Scatter 再接了 Copy to Points..."——效率低且容易遗漏。houdini2chat 把这件事自动化了：**一键导出场景为 LLM 能读懂的伪代码**。

### 怎么做？（五阶段流水线）

| 阶段 | 做什么 |
|------|--------|
| **发现** | 读取 HDA 参数 → `hou.node()` 遍历 `/obj` 下子节点 → 按 NetworkBox 过滤 |
| **构图** | `NodeGraph`（~600行核心）构建有向图，检测 `block_begin`/`block_end` 循环对，处理多输出节点（插入 @reference 占位），分解为分支 |
| **提取** | 每个节点提取：类型、名称、参数值/表达式/引用、输入输出连线、VEX 代码、便签 |
| **渲染** | 7 个 Jinja2 模板，特殊节点（attribwrangle、solver）有自定义宏，内联 VEX 代码 |
| **输出** | `.py` 文件写入磁盘，支持按节点/按 NetworkBox 命名 |

### 为什么选 Python 伪代码？

LLM 对 Python 训练最多，所有编辑器自动高亮。本质是把**视觉节点网络编译成 LLM 的"母语"**。

### 关键设计决策

- **HDA 作为分发**：一个 `.hdalc` 文件包含所有代码，零安装
- **人还在回路中**：AI 只分析建议，不直接操作——避免了线程安全问题
- **NetworkBox 感知**：能按分组导出，大型网络不撑爆 LLM 上下文窗口

### 和同类方案的区别

| | houdini2chat | fxhoudinimcp | Houdini Agent |
|---|---|---|---|
| 方式 | 文件导出 | MCP 实时 | 独立程序 |
| 能改场景 | ❌ | ✅ | ✅ |
| 门槛 | 拖个 HDA | 配 MCP Server | 装桌面程序 |
| 适用 | 学习、求助 | 实时操控 | 全流程协作 |

### 诚实说局限

- 只读、仅 `/obj` 级、无几何数据、无自动化测试
- v0.1.0，概念验证阶段

### 我的理解

它的设计哲学是**"最低摩擦"**——不改变艺术家工作流，不需要额外配置。在 MCP 和 Agent 方案还不够成熟时，这种"导出→对话"的轻量方案反而最实用。