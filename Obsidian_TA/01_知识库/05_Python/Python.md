---
tags:
  - python
  - 面试
  - TA
  - 技术美术
  - PCG
created: 2026-07-22
updated: 2026-07-22
related:
  - "[[00_技术美术 简历_PCG方向]]"
  - "[[01_复盘]]"
  - "[[网易面试回答]]"
  - "[[QA_PCG技术美术面试题集]]"
---

# 技术美术 Python 面试 — 完整答案

> 面向 PCG TA 岗位（网易/腾讯/TapTap），每题附带面试回答 + 项目关联

---

## 一、Python 基础（高频八股，但 TA 面试只考实用的）

### 1. `list` vs `tuple` vs `set` vs `dict`

**面试回答**：

| 类型 | 特点 | TA 场景 |
|------|------|---------|
| `list` | 有序、可改、可重复 | 存储节点列表、文件路径列表 |
| `tuple` | 有序、**不可改**、可重复 | 存不可变配置（坐标、RGB 颜色） |
| `set` | 无序、**不重复**、可改 | 去重——"这 500 个资产用了哪些材质？" |
| `dict` | 键值对、键唯一 | 最常用！旧名→新名映射、资产元数据、配置表 |

> **你的项目**：[[00_技术美术 简历_PCG方向#Python 管线]] 中批量处理脚本大量用 `dict` 做贴图后缀映射：`{"_d": "sRGB", "_n": "Normalmap", "_m": "Linear"}`

**关键追问题**：为什么批量改名时要用 `dict` 做旧名→新名映射，而不是直接在循环里改？

> "因为 Houdini/Maya 中节点改名可能触发引用更新——如果你循环中边读边改，遍历顺序会乱。用 dict 先收集所有映射，再统一执行改名，避免这种竞态问题。"

---

### 2. 可变 vs 不可变对象

**面试回答**：

- **不可变**：`int`, `float`, `str`, `tuple` — 创建后不能修改内容
- **可变**：`list`, `dict`, `set` — 可以修改内容

**TA 场景的经典坑**：函数默认参数用可变对象

```python
# ❌ 经典踩坑 —— 默认参数是可变对象
def collect_nodes(node, results=[]):
    results.append(node)
    for child in node.children():
        collect_nodes(child, results)
    return results

# 第二次调用 results 不会清空！上一次的结果还在！

# ✅ 正确做法
def collect_nodes(node, results=None):
    if results is None:
        results = []
    results.append(node)
    ...
```

---

### 3. 深浅拷贝

**面试回答**：

```python
import copy

# 浅拷贝：只复制第一层，内层引用共享
a = [[1, 2], [3, 4]]
b = copy.copy(a)      # b 是新列表，但 b[0] 和 a[0] 是同一个子列表
b[0][0] = 99          # a[0][0] 也变成 99！

# 深拷贝：递归复制所有层
c = copy.deepcopy(a)  # 完全独立
```

**TA 场景**：
> "在 Houdini 中克隆节点网络时，如果你用 `hou.Node.copy()` 只是浅拷贝，参数和连接可能还被共享。要完全独立就要小心。另外处理嵌套几何体数据（如 `MFnMesh` 的顶点列表）时，浅拷贝可能导致修改一处影响另一处。"

---

### 4. `*args` 和 `**kwargs`

**面试回答**：

```python
def process_assets(project_name, *file_paths, **settings):
    """
    批量处理资产 —— 我实际项目中写这种函数很多
    
    project_name: 必需参数
    *file_paths:  可变数量的文件路径
    **settings:   键值对配置（后缀映射、输出路径等）
    """
    for path in file_paths:
        print(f"Processing {path} for {project_name}")
    
    if settings.get("compress"):
        print(f"Compression: {settings['compress']}")
    if settings.get("output_dir"):
        print(f"Output: {settings['output_dir']}")

# 调用
process_assets(
    "盘丝洞",
    "/tex/diffuse.tga", "/tex/normal.tga", "/tex/roughness.tga",
    compress="BC7", output_dir="/game/assets"
)
```

> **你的项目**：[[00_技术美术 简历_PCG方向#Python 管线]] 的批量导入脚本正是这种模式——函数接受任意数量的贴图路径 + 配置字典。

---

### 5. 闭包是什么？

**面试回答**：

> "闭包 = 函数 + 它能访问的外部变量。典型场景：**生成配置化的处理函数**，比如创建一个带特定前缀的重命名器。"

```python
def make_renamer(prefix, suffix):
    """创建一个重命名函数，锁定前缀和后缀"""
    def rename(name):
        return f"{prefix}_{name}_{suffix}"
    return rename

# 使用
building_renamer = make_renamer("BDG", "LOD0")
print(building_renamer("House_01"))  # → BDG_House_01_LOD0

vegetation_renamer = make_renamer("VGT", "LOD1")
print(vegetation_renamer("Tree_Oak"))  # → VGT_Tree_Oak_LOD1
```

> "TA 场景：定义一个通用的处理规则，然后在不同上下文复用。比如 [[网易面试回答#Q17 道路工具]] 中，路灯和行道树的间距生成逻辑是同一模式——用闭包封装'间距规则'传入不同参数。"

---

### 6. 装饰器原理？写一个带参数的装饰器

**面试回答**（这题网易和腾讯面试都出现了）：

> "装饰器本质是一个**接收函数、返回函数**的高阶函数。核心原理是 Python 中函数是一等公民，可以像变量一样被传递和返回。"

```python
import time
from functools import wraps

# === 基础装饰器：计时 ===
def timer(func):
    @wraps(func)  # 保留原函数的 __name__ 和 __doc__
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def cook_all_hdas(hda_list):
    for hda in hda_list:
        hda.cook()

# === 带参数的装饰器：重试机制 ===
def retry(max_attempts=3, delay=1.0):
    """TA 场景：Houdini Cook 可能偶发失败，自动重试"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"[Retry {attempt+1}/{max_attempts}] {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2.0)
def cook_hda_safe(hda_node):
    hda_node.cook(force=True)
```

> **你的项目**：[[网易面试回答#Q23 AI 项目]] 中用 GPT 生成代码后逐行 Review，装饰器是一个好的验证点——你可以说"AI 写的装饰器我懂得原理，所以能判断它是否正确处理了 `@wraps` 和参数传递"。

---

### 7. 迭代器 vs 生成器

**面试回答**：

> "**可迭代对象**：能放进 `for` 循环的（list, dict, …）  
> **迭代器**：记住'遍历到哪了'，用 `next()` 逐个取  
> **生成器**：用 `yield` 的函数，惰性求值，不一次性占内存"

```python
# 列表：一次性加载，占内存
all_points = [process_point(p) for p in range(1_000_000)]  # 全部算完才执行下一步

# 生成器：惰性，逐个产出，不占内存
def iter_pcg_points(point_data):
    for point in point_data:
        if point.density > 0.5:
            yield point  # 只产出满足条件的点

# TA 场景：处理百万级点云时，生成器避免内存爆炸
for point in iter_pcg_points(huge_dataset):
    place_asset(point)
```

> **你的项目**：[[网易面试回答#Q6 VEX]] 中逐点操作对应 Python 中大量点云处理，生成器是处理海量 PCG 点的核心手段。

---

### 8. `@staticmethod` vs `@classmethod` vs 普通方法

**面试回答**：

```python
class AssetProcessor:
    """资产处理器 —— TA 工具类的典型结构"""
    
    version = "2.1"  # 类变量
    
    def __init__(self, input_dir):
        self.input_dir = input_dir  # 实例变量
    
    def process(self, file_name):
        """普通方法：需要 self，访问实例数据"""
        path = f"{self.input_dir}/{file_name}"
        return self._load(path)
    
    @classmethod
    def from_config(cls, config_path):
        """类方法：接收 cls，常用于工厂方法——从配置文件创建实例"""
        with open(config_path) as f:
            config = json.load(f)
        return cls(config["input_dir"])
    
    @staticmethod
    def validate_name(name):
        """静态方法：不需要 self/cls，纯工具函数但逻辑上属于这个类"""
        return bool(re.match(r"^SM_[A-Za-z0-9_]+$", name))

# 使用
# 普通方法
ap = AssetProcessor("/game/assets")
ap.process("wall.fbx")

# 类方法 —— 工厂模式
ap = AssetProcessor.from_config("pipeline_config.json")

# 静态方法 —— 不需要实例化
AssetProcessor.validate_name("SM_Wall_Stone_01")  # True
```

> **TA 场景**：`@classmethod` 在管线工具中很常用——"从 JSON 配置创建处理器"；`@staticmethod` 用于纯校验函数（命名检查、格式验证），这些在 [[QA简历面试题#Q17 Python 批量脚本]] 的批量处理场景里经常出现。

---

### 9. `@property` 装饰器——TA 工具中的例子

**面试回答**：

> "`@property` 让方法调用看起来像属性访问，适合需要计算但又想保持简洁接口的场景。"

```python
class HDAConfig:
    """HDA 参数配置 —— 封装对 Houdini HDA 参数的读写"""
    
    def __init__(self, hda_node):
        self._node = hda_node
    
    @property
    def building_height(self):
        """像读属性一样读 HDA 参数"""
        return self._node.parm("building_height").eval()
    
    @building_height.setter
    def building_height(self, value):
        """设置时自动做范围检查"""
        value = max(3.0, min(value, 50.0))  # 限制在 3-50m
        self._node.parm("building_height").set(value)
    
    @property
    def status(self):
        """动态计算状态，不是存储的值"""
        errors = self._node.errors()
        return "OK" if not errors else f"Error: {errors[0]}"

# 使用 —— 干净简洁
config = HDAConfig(building_hda)
config.building_height = 12   # 自动范围检查
print(config.building_height) # 12.0
print(config.status)          # OK（自动计算）
```

> **你的项目**：[[网易面试回答#Q10 HDA 参数设计]] 中讨论的 HDA 参数暴露——`@property` 是封装 HDA 参数读写的最佳方式，允许加验证逻辑而不改变外部调用接口。

---

### 10. 鸭子类型（Duck Typing）

**面试回答**：

> "鸭子类型 = '如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子'。Python 不检查对象的类型，只检查对象**有没有你需要的方法/属性**。"

```python
# 不检查类型，只要有 .cook() 方法就能用
def batch_cook(nodes):
    for node in nodes:
        node.cook(force=True)

# 可以传入 Houdini SOP、ROP、HDA——只要它们有 .cook() 方法
batch_cook([geo_node, rop_node, hda_node])

# ❌ 非鸭子类型写法（不推荐）
def batch_cook(nodes):
    for node in nodes:
        if isinstance(node, hou.SopNode):  # 写死了类型
            node.cook()
```

> **TA 场景**：管线工具中处理不同类型的 DCC 节点（SOP/Render/HDA），用鸭子类型让代码更灵活。不用 `isinstance` 检查，只要对象有 `.cook()` 方法就能传。

---

### 11. `try/except/else/finally` 的执行顺序

**面试回答**：

```python
def cook_and_export(hda_node, export_path):
    """真实的 TA 工作函数 —— 每个阶段都有明确的异常处理"""
    try:
        # try: 执行可能出错的代码
        hda_node.cook(force=True)
    
    except hou.OperationFailed as e:
        # except: 出错时执行
        print(f"[FAILED] Cook failed: {e}")
        return False
    
    else:
        # else: try 成功后才执行（不捕获此处的异常）
        # 关键理解：只有 Cook 成功才导出，否则跳过
        export_fbx(hda_node, export_path)
        print(f"[OK] Exported to {export_path}")
    
    finally:
        # finally: 无论成功失败都执行 —— 清理资源
        hda_node.destroy()  # 删除临时节点
    
    return True
```

> **执行顺序**：`try` 成功 → `else` → `finally`  
> `try` 失败（被 `except` 捕获）→ `except` → `finally`  
> `try` 失败（未被 `except` 捕获）→ `finally` → 异常继续向上抛

> **TA 场景**：[[QA_PCG技术美术面试题集#JD-Q18 批量 Cook 脚本]] 中，每个 HDA 的 Cook 都可能失败，但你不希望一个失败导致 100 个全停——`try/except` 去捕获单个失败，记录日志，继续处理下一个。

---

### 12. 上下文管理器（`with` 语句）

**面试回答**：

> "`with` 语句确保资源在使用后被正确释放，核心是 `__enter__`（进入时执行）和 `__exit__`（退出时执行，包括异常情况）。"

```python
# === TA 场景1：临时禁用 Maya undo，操作完自动恢复 ===
class UndoDisabled:
    """批量操作时禁用 Undo 以提速，with 块结束后自动恢复"""
    
    def __enter__(self):
        cmds.undoInfo(stateWithoutFlush=False)  # 关 undo
    
    def __exit__(self, *args):
        cmds.undoInfo(stateWithoutFlush=True)   # 恢复 undo

# 使用
with UndoDisabled():
    for i in range(1000):
        cmds.polyCube()  # 操作不会被记录到 undo 队列，快很多

# === TA 场景2：临时切换 Houdini 当前节点 ===
class TempNodeContext:
    """临时切换到某个节点，退出时恢复"""
    
    def __init__(self, target_node):
        self.target = target_node
        self.previous = None
    
    def __enter__(self):
        self.previous = hou.pwd()
        self.target.setCurrent(True, clear_all_selected=True)
        return self.target
    
    def __exit__(self, *args):
        if self.previous:
            self.previous.setCurrent(True, clear_all_selected=True)

# 使用
with TempNodeContext(geo_node):
    create_sop_chain()  # 所有操作都在 geo_node 内

# === 也可以用 contextlib 简化 ===
from contextlib import contextmanager

@contextmanager
def temp_parm(node, parm_name, temp_value):
    """临时改参数，退出时恢复原值"""
    original = node.parm(parm_name).eval()
    node.parm(parm_name).set(temp_value)
    try:
        yield
    finally:
        node.parm(parm_name).set(original)

with temp_parm(hda, "preview_mode", 1):
    render_thumbnail()  # 用预览模式渲染，结束后恢复
```

> **你的项目**：[[QA简历面试题#Q15 盘丝洞性能优化]] 中批量操作时要关 Undo 提速——这就是 `with` 语句的典型应用。面试时说这个场景，能体现你对 DCC API 的深度理解和工程化思维。

---

### 13. `if __name__ == "__main__"` 的作用

**面试回答**：

> "区分'直接运行这个脚本'和'被别人 import 导入'。直接运行时执行 `if` 内的代码；被 import 时不执行。"

```python
# my_pipeline_tools.py
def batch_import_textures(texture_dir):
    """贴图批量导入 —— 可被其他脚本 import 调用"""
    ...

def validate_scene():
    """场景规范检查"""
    ...

if __name__ == "__main__":
    # 只在直接运行这个文件时执行 —— 方便独立测试
    import sys
    batch_import_textures(sys.argv[1])
```

> **TA 应用**：你的管线工具脚本既可以在命令行独立运行（直接 `python batch_import.py /tex/`），也可以被更大的工具面板 import 其中的函数。加上这个判断让模块"可运行也可被引用"。

---

### 14. `.py` vs `.pyc` vs `.pyd` + `reload` 的坑

**面试回答**：

| 文件类型 | 说明 | TA 场景 |
|----------|------|---------|
| `.py` | Python 源码 | 你写的工具脚本 |
| `.pyc` | 编译成字节码的缓存（加载更快） | DCC 启动时自动生成 |
| `.pyd` | Windows 上的 C 扩展（相当于 `.so`） | Maya/Houdini 的底层 API |

**`reload` 的坑**：

> "DCC 中调试工具脚本时，改了 `.py` 文件但 DCC 用的是旧的 `.pyc` 缓存。需要 `reload()` 强制刷新。但 `reload` 有个常见坑——类定义不会更新已有实例，旧的实例还是用旧类。所以调试时通常建议重启 DCC 或重建节点。"

```python
import importlib
importlib.reload(my_tool_module)  # 强制重新加载
```

---

## 二、DCC 工具开发（TA 面试最核心的 Python 板块）

### 15. Maya Python 三层 API 对比

**面试回答**（TA 面试几乎必问）：

| 层级 | 全称 | 特点 | 适用场景 |
|------|------|------|----------|
| **`maya.cmds`** | Maya Commands | 命令式，字符串传参，最慢但最简单 | 快速脚本、一次性操作 |
| **`pymel`** | PyMEL | 面向对象，链式调用，可读性好 | 工具开发、复杂逻辑 |
| **`OpenMaya 1.0`** | Maya API (SWIG) | C++ API 的 SWIG 绑定，快但 API 丑 | 高性能需求 |
| **`OpenMaya 2.0`** | `maya.api.OpenMaya` | Python 化的新版 C++ API，推荐 | 批量几何操作、自定义节点 |

**具体对比**：

```python
# cmds —— 简单但慢
cmds.setAttr("pCube1.translateX", 5)

# pymel —— 面向对象，可读性好但比 cmds 慢
cube = pm.PyNode("pCube1")
cube.translateX.set(5)

# OpenMaya 2.0 —— 最快，适合批量操作
mesh_fn = OpenMaya.MFnMesh(mesh_dag_path)
positions = OpenMaya.MPointArray()
for i in range(100000):
    positions.append(OpenMaya.MPoint(x[i], y[i], z[i]))
mesh_fn.setPoints(positions)  # 一次性设置所有顶点
```

**选型建议**：

> "快速原型用 `cmds`，工具开发用 `pymel`，批量几何操作用 `maya.api.OpenMaya`。实际项目中我通常**混用**——工具框架用 pymel 保证可读性，数据处理部分切到 OpenMaya 2.0 保证性能。"

---

### 16. Houdini hou 模块常用操作

**面试回答**——结合你的实际项目：

```python
import hou

# === 1. 查找节点 ===
node = hou.node("/obj/geo1/building_generator")
node = hou.node(".")          # 返回一个 Generator，不是直接可用的节点
node = hou.pwd()              # 当前节点（在 HDA 的 Python SOP 中）

# === 2. 创建/修改节点 ===
geo = hou.node("/obj").createNode("geo", "my_city_generator")
box = geo.createNode("box")
wrangle = geo.createNode("attribwrangle")

# === 3. 操作参数 ===
node.parm("seed").set(42)
height = node.parm("building_height").eval()        # 返回 float
building_type = node.parm("style").evalAsString()   # 返回 str
node.parm("show_preview").set(True)                  # Toggle

# === 4. 连接节点 ===
box.setInput(0, wrangle)       # 把 wrangle 的输出连到 box 的输入 0
null_node.setDisplayFlag(True) # 设为显示节点
null_node.setRenderFlag(True)  # 设为渲染节点

# === 5. 遍历节点 ===
for child in geo.children():
    print(child.name(), child.type().name())

for conn in node.inputConnections():
    print(conn.inputNode().name())
    print(conn.inputIndex())      # 连到第几个输入口
    print(conn.outputIndex())     # 从第几个输出口出来

# === 6. 读写属性（Geometry） ===
geo_data = node.geometry()        # 获取几何体
for point in geo_data.points():
    pos = point.position()
    density = point.attribValue("density")  # 读取自定义属性
    point.setAttribValue("pscale", 1.5)     # 设置属性

# === 7. Cook ===
node.cook(force=True)            # 强制重新计算
```

> **你的项目**：[[网易面试回答#Q6 VEX vs Python]] 的 VEX 章节对比了两种语言的场景——这里补充 Python 侧的实际用法。

---

### 17. Python SOP 在 Houdini 中的用法

**面试回答**：

> "Python SOP 允许在 Houdini 中编写 Python 来操作几何体。它比 VEX 慢，但能做一些 VEX 做不了的事——比如调外部 API、复杂文件 I/O、条件逻辑。"

```python
# Python SOP 示例：读取 CSV 点云数据并创建几何体
node = hou.pwd()
geo = node.geometry()

import csv
csv_path = node.parm("csv_file").eval()

# 读取外部 CSV
points = []
with open(csv_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        pos = (float(row["x"]), float(row["y"]), float(row["z"]))
        species = row["species"]
        points.append((pos, species))

# 创建点
geo.createPoints(len(points))
for i, (pos, species) in enumerate(points):
    pt = geo.points()[i]
    pt.setPosition(pos)
    pt.setAttribValue("species", species)
```

**何时用 Python SOP vs VEX Wrangle**：

| 场景 | 用 Python SOP | 用 VEX Wrangle |
|------|:---:|:---:|
| 逐点数学运算 | ❌ 慢 | ✅ 原生高性能 |
| 读取外部 JSON/CSV | ✅ | ❌ |
| 调外部 API/Web | ✅ | ❌ |
| 创建/连接 Houdini 节点 | ✅ | ❌ |

---

### 18. Python 批量创建/修改节点

**面试回答**——这是你项目中大量使用的模式：

```python
import hou

def create_city_generator(parent_path, city_config):
    """
    根据配置字典批量创建城市生成节点网络
    — 这就是你 PSD 转体块工具的底层逻辑
    """
    parent = hou.node(parent_path)
    if not parent:
        parent = hou.node("/obj").createNode("geo", "city_generator")
    
    # 批量创建节点
    nodes = {}
    node_specs = [
        ("file", "input_psd"),
        ("trace", "trace_blocks"),
        ("resample", "smooth_edges"),
        ("polyextrude", "extrude_buildings"),
        ("attribwrangle", "color_to_type"),
        ("null", "OUT_BUILDINGS"),
    ]
    
    for node_type, name in node_specs:
        nodes[name] = parent.createNode(node_type, name)
    
    # 批量连线
    nodes["trace_blocks"].setInput(0, nodes["input_psd"])
    nodes["smooth_edges"].setInput(0, nodes["trace_blocks"])
    nodes["extrude_buildings"].setInput(0, nodes["smooth_edges"])
    nodes["color_to_type"].setInput(0, nodes["extrude_buildings"])
    nodes["OUT_BUILDINGS"].setInput(0, nodes["color_to_type"])
    
    # 批量设参数
    nodes["extrude_buildings"].parm("dist").set(city_config.get("height", 10))
    nodes["smooth_edges"].parm("length").set(2.0)
    
    # 设显示和渲染标志
    nodes["OUT_BUILDINGS"].setDisplayFlag(True)
    nodes["OUT_BUILDINGS"].setRenderFlag(True)
    
    # 自动排列
    parent.layoutChildren()
    
    return parent

# 使用
config = {"height": 15, "style": "commercial"}
city_node = create_city_generator("/obj", config)
```

> **面试闪光点**："我的 PSD 转体块工具就是这种结构——配置驱动生成节点网络，不同颜色映射不同建筑类型。代码生成节点而非手动拖节点，让工具可以批量实例化。"

---

### 19. HDA 中 Python 路径管理

**面试回答**：

> "HDA 中写 Python 脚本时，外部模块的导入是个常见坑。Houdini 的 Python 环境不一定能找到你的自定义模块。"

```python
# === HDA Python SOP 内部的正确做法 ===

import os
import sys

# 方案 1：添加 HDA 所在目录到 sys.path
hda_dir = os.path.dirname(hou.node(".").type().definition().libraryFilePath())
if hda_dir not in sys.path:
    sys.path.insert(0, hda_dir)

# 方案 2：使用 hou.session（Houdini 会话级共享模块）
import hou.session
# 把公共函数放在 Python Source Editor 的 hou.session 中
# 然后在任何地方调用 hou.session.my_tool_function()

# 方案 3：使用 HDA 内嵌的 Python 模块
# 在 HDA 的 Scripts 标签页 → Python Module 中定义
# 然后通过 kwargs["type"] 获取
```

> **常见坑**：修改了外部 `.py` 文件但 Houdini 不刷新——需要 `importlib.reload()` 或重启。

---

### 20. DCC 主线程限制

**面试回答**（腾讯和网易都问过这个）：

> "几乎所有 DCC（Maya、Houdini、UE）的 UI 和大部分 API 都不是线程安全的，**必须在主线程调用**。这是因为底层 C++ 对象的状态管理没有做线程保护。"

**解决方案**：

```python
# Maya: executeDeferred — 把操作推迟到主线程执行
import maya.utils
maya.utils.executeDeferred(my_ui_update_function)

# Maya: evalDeferred — 执行字符串代码
cmds.evalDeferred('cmds.select("pCube1")')

# Houdini: 使用回调
hou.ui.addEventLoopCallback(my_function)

# 实践中的正确处理
from PySide2.QtCore import QThread, Signal

class CookWorker(QThread):
    """工作线程做 Cook，通过信号把结果传回主线程"""
    finished = Signal(object)
    
    def run(self):
        # 注意：这里不能直接调 hou API！
        # 应该用 subprocess 或 hython 进程
        import subprocess
        result = subprocess.run(["hython", "cook_script.py"], capture_output=True)
        self.finished.emit(result)

# 主线程接收结果并更新 UI
worker = CookWorker()
worker.finished.connect(self.on_cook_finished)  # 信号在主线程处理
worker.start()
```

> "简单说：**计算可以在后台做，但任何 DCC API 调用必须在主线程。**"

---

### 21. DCC 启动脚本

**面试回答**：

| DCC | 启动脚本 | 作用 |
|-----|----------|------|
| **Maya** | `userSetup.py`（在 `~/maya/scripts/`） | Maya 启动时自动执行，注册工具菜单/快捷键 |
| **Houdini** | `456.py`（在 `~/houdiniXX.X/scripts/`） | Houdini 启动时执行（在 UI 加载前） |
| **Houdini** | `123.py` | 场景新建/打开时执行 |
| **Maya** | `__init__.py`（在模块路径） | 模块化分发工具 |

```python
# Maya userSetup.py 示例
import maya.cmds as cmds

def setup_ta_tools():
    """启动时注册 TA 工具菜单"""
    menu = cmds.menu("TA_Tools", parent=cmds.mayaMainWindow(), label="TA Tools")
    cmds.menuItem(label="批量重命名", command="import batch_rename; batch_rename.show()")
    cmds.menuItem(label="资产检查", command="import asset_checker; asset_checker.show()")

cmds.evalDeferred(setup_ta_tools)  # 推迟到 Maya 完全加载后执行
```

---

## 三、UI 开发（PySide/Qt）

### 22. Qt 信号与槽

**面试回答**：

> "信号槽是 Qt 的**事件通信机制**。信号 = 事件的发射方（如'按钮被点了'），槽 = 事件的响应方（如'按钮被点后执行什么'）。核心价值是**解耦**——发射方不需要知道谁在接收。"

```python
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QWidget

class TAExporterUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        self.export_btn = QPushButton("导出 FBX")
        self.cancel_btn = QPushButton("取消")
        
        layout.addWidget(self.export_btn)
        layout.addWidget(self.cancel_btn)
        
        # 连接信号和槽
        self.export_btn.clicked.connect(self.on_export_clicked)
        self.cancel_btn.clicked.connect(self.close)
    
    def on_export_clicked(self):
        """按钮被点击时的响应"""
        print("开始导出...")
        batch_export_fbx()  # 调用管线函数
```

**自定义信号**（工作线程通知 UI）：

```python
from PySide2.QtCore import QObject, Signal

class ExportWorker(QObject):
    progress = Signal(int)        # 进度 0-100
    finished = Signal(list)       # 结果列表
    error_occurred = Signal(str)  # 错误信息
    
    def run(self):
        try:
            files = get_file_list()
            for i, f in enumerate(files):
                export_file(f)
                self.progress.emit(int((i+1)/len(files)*100))
            self.finished.emit(files)
        except Exception as e:
            self.error_occurred.emit(str(e))
```

> **拿你项目举例**：[[QA简历面试题#Q17 Python 批量脚本]] 的批量导入工具如果升级为 UI 版本，用信号槽把后台处理进度实时更新到 QProgressBar 上，让美术看到进度而非干等。

---

### 23. QThread 正确用法

**面试回答**（高频问题）：

> "Python 的 GIL 让多线程不能加速 CPU 密集型计算。但在 TA 工具中，多线程用来**让 UI 不卡顿**——后台 Cook HDA，前台进度条照常响应。"

```python
from PySide2.QtCore import QThread, Signal

class CookWorker(QThread):
    """后台 Cook 线程"""
    progress = Signal(int, str)  # 进度 + 当前处理的节点名
    
    def __init__(self, hda_list):
        super().__init__()
        self.hda_list = hda_list
    
    def run(self):
        # ⚠️ 注意：Houdini API 不能在子线程直接调用！
        # 正确做法：用 hython 子进程
        import subprocess
        for i, hda_path in enumerate(self.hda_list):
            self.progress.emit(int((i+1)/len(self.hda_list)*100), hda_path)
            subprocess.run(["hython", "-c", 
                f"import hou; hou.node('{hda_path}').cook(force=True)"
            ])

# 主线程中
def start_cook():
    self.worker = CookWorker(hda_list)
    self.worker.progress.connect(self.on_progress)
    self.worker.finished.connect(self.on_finished)
    self.worker.start()  # 启动线程，主线程继续响应 UI

# ⚠️ 关键：worker.start() ≠ worker.run()
# start() 创建新线程并调用 run()；直接调用 run() 会在当前线程执行（卡 UI）
```

**两种方案对比**：

| 方案 | 优点 | 缺点 | 适用 |
|------|------|------|------|
| **继承 QThread** | 代码直观 | 耦合度高 | 简单的一次性任务 |
| **moveToThread** | 解耦好，可复用 | 代码稍多 | 长期运行的服务/多次任务 |

> **关键提醒**："面试时一定要说清楚：**DCC API（hou/cmds）不能在子线程调用**。正确做法是用 `subprocess` 调 `hython` 或 `mayapy` 进程。"

---

### 24. Maya Qt 窗口管理

**面试回答**：

> "在 Maya 中创建 Qt 窗口最大的坑是**窗口 parent 问题**——如果 parent 设错了，Maya 关了窗口还在后台运行，下次打开就重复。"

```python
# === Maya Qt 窗口的标准模板 ===
from PySide2 import QtWidgets
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

def get_maya_main_window():
    """获取 Maya 主窗口作为 Qt parent —— 关键步骤"""
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class TAToolWindow(QtWidgets.QDialog):
    def __init__(self, parent=get_maya_main_window()):
        super().__init__(parent)
        self.setWindowTitle("TA 工具面板")
        self.setObjectName("TAToolWindow_Unique")  # 唯一名
        
        # 删除关闭时的默认行为（隐藏而非销毁）
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        
        # ... UI 构建 ...

# 全局唯一实例
_tool_window = None

def show_tool():
    global _tool_window
    if _tool_window is None:
        _tool_window = TAToolWindow()
    _tool_window.show()
    _tool_window.raise_()  # 提到最前
```

**Maya 特有的 workspaceControl**（Maya 2017+）：

```python
# 把 Qt 窗口嵌入 Maya 的工作区（可停靠）
workspace_control = cmds.workspaceControl(
    "TAToolWorkspace",
    label="TA 工具",
    retain=False,     # Maya 关闭时不保存状态
    floating=True,
    widthProperty="freeform"
)
```

> "面试时说出 `wrapInstance` + `omui.MQtUtil.mainWindow()` 这个 magic pattern，面试官就知道你确实做过 Maya 工具开发。"

---

## 四、文件处理与管线数据

### 25. JSON vs YAML 在管线中的选择

**面试回答**：

> "管线配置我推荐 **JSON**——所有语言原生支持、人可读、没有安全问题。YAML 可读性更好但容易缩进出错。XML 太重了，游戏行业基本不用。"

```python
# === JSON 配置驱动 —— 你的工具开发模式 ===
# pipeline_config.json
{
    "texture_rules": {
        "_d": {"color_space": "sRGB", "compression": "BC7"},
        "_n": {"color_space": "Linear", "compression": "BC5"},
        "_m": {"color_space": "Linear", "compression": "BC4"},
        "_orm": {"color_space": "Linear", "compression": "BC7"}
    },
    "naming_convention": {
        "static_mesh": "SM_{type}_{description}_{variant}",
        "material": "M_{type}_{description}",
        "texture": "T_{mesh}_{channel}"
    },
    "lod_settings": {
        "LOD0": {"screen_size": 1.0, "reduction": 0},
        "LOD1": {"screen_size": 0.5, "reduction": 50},
        "LOD2": {"screen_size": 0.25, "reduction": 75}
    }
}
```

```python
import json

def load_pipeline_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def apply_texture_settings(texture_path, config):
    """根据后缀自动匹配贴图设置"""
    rules = config["texture_rules"]
    for suffix, settings in rules.items():
        if texture_path.endswith(suffix):
            set_color_space(settings["color_space"])
            set_compression(settings["compression"])
            return
```

> **你的项目**：[[00_技术美术 简历_PCG方向#Python 管线]] 的批量导入脚本就是这个核心逻辑——根据后缀 `_d`/`_n`/`_m` 自动匹配导入设置。面试时说"配置驱动而非硬编码"，能体现工业化思维。

---

### 26. 处理大文件的策略

**面试回答**：

> "TA 管线中常见的大文件场景：几 GB 的点云 CSV、Houdini 的 bgeo 缓存文件、不合理的全量加载。策略是**流式+分块+懒加载**。"

```python
# ❌ 大文件全量加载 — 内存爆炸
data = open("huge_pointcloud.csv").read()  # 几 GB 全读入内存
points = data.split("\n")                  # 再次翻倍

# ✅ 流式读取 + 生成器
def iter_points(csv_path):
    """逐行读取百万行点云数据，不占内存"""
    with open(csv_path) as f:
        header = f.readline()  # 读表头
        for line in f:
            x, y, z, density = line.strip().split(",")
            if float(density) > 0.5:
                yield (float(x), float(y), float(z))

# 处理
count = 0
for point in iter_points("10GB_pointcloud.csv"):
    count += 1
    if count % 100000 == 0:
        print(f"Processed {count} points...")  # 进度反馈
```

**分块处理策略**：

```python
import pandas as pd

# 用 pandas 分块读大型 CSV
chunk_size = 100000
for chunk in pd.read_csv("huge_data.csv", chunksize=chunk_size):
    # 每 10 万行处理一块
    processed = chunk[chunk["density"] > 0.5]
    processed.to_csv("filtered_output.csv", mode="a", header=False)
```

---

### 27. `os.path` vs `pathlib`

**面试回答**：

> "新项目一律用 `pathlib`——代码更简洁、面向对象、跨平台性好。`os.path` 是老项目的遗留代码。"

```python
from pathlib import Path

# os.path 风格 — 嵌套函数调用，不直观
import os
path = os.path.join(os.path.dirname(__file__), "assets", "textures")
ext = os.path.splitext(file)[1]

# pathlib 风格 — 链式调用，像说话
path = Path(__file__).parent / "assets" / "textures"
ext = Path(file).suffix

# pathlib 的便利操作
asset_dir = Path("D:/Projects/Game/Assets")

# 遍历所有 FBX
for fbx in asset_dir.rglob("*.fbx"):
    print(fbx.stem)      # 文件名（无扩展名）
    print(fbx.suffix)    # .fbx
    print(fbx.parent)    # 父目录

# 批量重命名
for fbx in asset_dir.glob("*.fbx"):
    new_name = fbx.stem.replace("old_", "new_") + ".fbx"
    fbx.rename(fbx.parent / new_name)

# 确保目录存在
output = Path("D:/Projects/Game/Exports/2024/Q1")
output.mkdir(parents=True, exist_ok=True)
```

---

## 五、性能与优化

### 28. Python 性能瓶颈 + profiling

**面试回答**：

> "Python 的性能瓶颈通常不在语言本身，而在**算法选择和 I/O 模式**。比如 DCC 中常见的：10000 次 API 调用 vs 1 次批量调用，差距是数量级。"

```python
import cProfile
import pstats

# 方法 1：cProfile — 定位耗时函数
cProfile.run("batch_cook_all_hdas()", "cook_stats.prof")

# 分析结果
stats = pstats.Stats("cook_stats.prof")
stats.sort_stats("cumulative").print_stats(20)  # 最耗时的 20 个函数

# 方法 2：简单计时 — 日常调试
import time
start = time.time()
expensive_operation()
print(f"Took {time.time() - start:.2f}s")

# 方法 3：timeit — 微基准测试
import timeit
elapsed = timeit.timeit("my_func()", setup="from __main__ import my_func", number=100)
```

**TA 场景的常见瓶颈**：

| 瓶颈类型 | 表现 | 解决方案 |
|----------|------|----------|
| 循环内 API 调用 | 10000 次 `cmds.setAttr` | 批量 `cmds.setAttr` 或 OM2 的 `setPoints` |
| 逐点操作 | Point Wrangle 用 Python 写 | 改用 VEX（Houdini 中快 10-100 倍） |
| 文件 I/O | 每个文件单独开闭 | 批量读写、用缓存 |
| 无意义的 Cook | 每改一个参数 Cook 整个网络 | `cmds.refresh(su=True)` 暂停刷新 |

> **你的项目**：[[QA简历面试题#Q15 盘丝洞性能优化]] 中讲优化的思路完全适用于 Python 性能——Profile→定位瓶颈→针对性优化→量化收益。

---

### 29. GIL / 多线程 / 多进程

**面试回答**（高频必问）：

> "**GIL（Global Interpreter Lock）** 是 CPython 的全局锁——同一时刻只有一个线程执行 Python 字节码。所以 Python 多线程不能加速 CPU 密集计算，但可以加速 I/O 密集型任务（文件读写、网络请求、子进程等待）。"

```python
# 多线程 — I/O 密集（文件批量处理）
from concurrent.futures import ThreadPoolExecutor

def process_single_file(file_path):
    """I/O 密集型：读写文件"""
    data = read_large_file(file_path)
    return process(data)

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(process_single_file, file_list)
    # 4 个文件并行读写，因为大部分时间在等磁盘 I/O

# 多进程 — CPU 密集（真正需要计算力的）
from concurrent.futures import ProcessPoolExecutor

def cook_hda_heavy(hda_args):
    """每个进程独立调用 hython Cook HDA"""
    import subprocess
    return subprocess.run(["hython", "cook_worker.py", str(hda_args)])

with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(cook_hda_heavy, hda_params_list)
    # 每个进程有独立的 Python 解释器和 GIL，真正并行
```

**TA 实际做法**：用 `subprocess` 调用独立的 `hython`/`mayapy` 进程，每个进程有独立 GIL，天然并行。这是 Houdini PDG 和 Maya Batch Render 的底层原理。

---

### 30. DCC 批量操作加速技巧

**面试回答**（结合你的实际经验）：

```python
# === Maya ===

# 1. 关闭 undo 队列 — 批量操作最关键的加速
cmds.undoInfo(stateWithoutFlush=False)  # 关闭
for i in range(5000):
    cmds.polyCube()  # 不会被记录到 undo 历史
cmds.undoInfo(stateWithoutFlush=True)   # 恢复

# 2. 暂停视口刷新
cmds.refresh(suspend=True)   # 操作期间不渲染视口
# ... 批量操作 ...
cmds.refresh(suspend=False)

# 3. 使用 OpenMaya 2.0 批量 API
# 比较：cmds 循环 10000 次 ≈ 3 秒，OM2 一次性 ≈ 0.1 秒

# 4. 把操作合并在一个 Python 调用内
# ❌ 多次往返 Python ↔ Maya C++ 
for obj in objects:
    cmds.setAttr(f"{obj}.tx", 5)
# ✅ 一次往返
cmds.setAttr([f"{obj}.tx" for obj in objects], 5)


# === Houdini ===

# 1. 批量创建/设置而非逐个调用
# ❌ 逐个
for name in names:
    geo.createNode("box", name)
# ✅ 用 build_network 或批量创建

# 2. 用 VEX 替代 Python Wrangle（逐点操作）
# Python Wrangle: 100万点 ≈ 30秒
# VEX Wrangle:    100万点 ≈ 0.3秒

# 3. HDA Cook 用 PDG 并行
# 传统：for hda in hdas: hda.cook()
# PDG：Wedge → HDA Processor → 自动并行
```

> **面试技巧**："这些优化里，**关 undo 和暂停视口刷新**是最容易做、效果最明显的——很多 TA 面到这里面试官会点头认可。"

---

## 六、版本控制

### 31. Git rebase vs merge

**面试回答**：

> "`merge` 保留真实历史，多一个合并提交；`rebase` 把提交'移动'到目标分支顶端，历史线性干净但改写了历史。"

```bash
# merge 策略 — 保留所有分支脉络
git checkout feature/pcg-tool
git merge main
# 结果：多一个 merge commit，历史保留"谁在什么时候做了什么"

# rebase 策略 — 线性干净
git checkout feature/pcg-tool
git rebase main
# 结果：你的提交被"重放"到 main 最新处，历史是一条线
```

**TA 团队协作中的使用**：

| 场景 | 推荐 | 原因 |
|------|:---:|------|
| 个人分支整理提交 | `rebase` | 清理"WIP""fix typo"等无意义提交 |
| 向主分支合并 | `merge` | 保留完整历史，方便追溯 |
| 多人同时改同一 HDA | `merge` | `rebase` 可能让 HDA 二进制冲突更难解 |

> "对于 HDA 文件的版本管理，Houdini 自带版本对比功能（Compare HDA），但 `.hda` 是二进制文件，git diff 无法直接看差异——建议配合 Houdini 的 Diff 工具或导出文本描述。"

### 32. Python 依赖管理

**面试回答**：

```bash
# 基础：requirements.txt
pip freeze > requirements.txt    # 导出全部依赖
pip install -r requirements.txt  # 安装

# 现代：pyproject.toml（推荐）
# 描述项目元数据和依赖

# DCC 环境隔离
# 方案 1：虚拟环境
python -m venv pipeline_env
source pipeline_env/bin/activate  # or .\Scripts\Activate.ps1 on Windows
pip install PySide2 openpyxl

# 方案 2：给每个 DCC 设置独立 sys.path
# Maya userSetup.py
import sys
sys.path.insert(0, "D:/TA_Tools/libs")
```

**TA 特有的坑**：不同 DCC 自带不同版本的 Python（Maya 2024 用 Python 3.10，Houdini 20.5 用 Python 3.11）——工具脚本尽量只用标准库 + PySide，避免引入第三方依赖导致版本冲突。

---

## 七、场景题——带完整答案

### 场景 1：批量重命名 500 个节点

**问题**："DCC 场景中有 500 个节点需要按规则重命名，如何高效实现？"

**回答**：

> "核心策略：**先收集映射，再统一执行**——避免循环中边读边改导致引用混乱。"

```python
import re

def batch_rename(pattern, replacement, dry_run=True):
    """批量重命名 Houdini 节点"""
    
    # Step 1: 收集所有节点
    all_nodes = hou.node("/obj").allSubChildren()
    
    # Step 2: 建立旧名→新名映射（还没改，只是在内存中计算）
    rename_map = {}
    conflict_check = set()
    
    for node in all_nodes:
        old_name = node.name()
        new_name = re.sub(pattern, replacement, old_name)
        
        if new_name == old_name:
            continue  # 不需要改的跳过
        
        # 检查命名冲突（两节点想要同一个新名）
        if new_name in conflict_check:
            new_name = f"{new_name}_conflict_{old_name}"
        conflict_check.add(new_name)
        
        rename_map[node] = new_name
    
    # Step 3: 预览模式（安全机制）
    if dry_run:
        print(f"=== Dry Run: {len(rename_map)} nodes will be renamed ===")
        for node, new_name in list(rename_map.items())[:10]:
            print(f"  {node.name()} → {new_name}")
        if len(rename_map) > 10:
            print(f"  ... and {len(rename_map) - 10} more")
        return
    
    # Step 4: 统一执行改名
    for node, new_name in rename_map.items():
        try:
            node.setName(new_name)
        except hou.OperationFailed as e:
            print(f"Failed to rename {node.name()}: {e}")

# 使用：把所有 "old_" 前缀改成 "new_"
batch_rename(r"^old_", "new_", dry_run=True)   # 先预览
batch_rename(r"^old_", "new_", dry_run=False)  # 确认后执行
```

**面试继续追问**："命名冲突怎么处理？"

> "三种策略：1) 自动加后缀（如上代码）；2) 分组——父节点名+子节点名保证唯一；3) 给美术弹窗让手动解决。实际项目中我选方案 1——不阻塞流程，自动消歧。"

---

### 场景 2：导出工具设计

**问题**："从 DCC 导出 FBX 的工具，需要支持批量导出和命名规范。"

**回答**——结合你的实际经验：

```python
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import logging

class FBXExporter:
    """FBX 批量导出器 —— 我在项目中实际开发的模式"""
    
    def __init__(self, config_path):
        self.config = json.loads(Path(config_path).read_text())
        self.naming_template = self.config["naming_template"]
        self.export_dir = Path(self.config["export_dir"])
        self.export_dir.mkdir(parents=True, exist_ok=True)
        
        # 日志
        logging.basicConfig(
            filename=self.export_dir / "export.log",
            level=logging.INFO
        )
    
    def generate_filename(self, asset_name, asset_type, variant):
        """按命名规范生成文件名"""
        return self.naming_template.format(
            project=self.config["project"],
            type=asset_type,
            name=asset_name,
            variant=variant,
            lod="LOD0"
        )
    
    def export_single(self, asset):
        """导出单个资产（可被多线程调用）"""
        try:
            name = self.generate_filename(
                asset["name"], asset["type"], asset["variant"]
            )
            output_path = self.export_dir / name
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 调 DCC API 导出
            self._do_export(asset["dcc_path"], output_path)
            
            logging.info(f"[OK] {output_path}")
            return {"status": "ok", "path": str(output_path)}
            
        except Exception as e:
            logging.error(f"[FAIL] {asset['name']}: {e}")
            return {"status": "error", "name": asset["name"], "error": str(e)}
    
    def export_batch(self, assets, max_workers=4):
        """批量导出 + 进度反馈"""
        total = len(assets)
        results = []
        
        # I/O 密集型用 ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.export_single, a): a for a in assets}
            
            for i, future in enumerate(futures):
                result = future.result()
                results.append(result)
                print(f"\rProgress: {i+1}/{total} ({int((i+1)/total*100)}%)", end="")
        
        # 生成报告
        ok = [r for r in results if r["status"] == "ok"]
        failed = [r for r in results if r["status"] == "error"]
        print(f"\nDone: {len(ok)} success, {len(failed)} failed")
        
        return {"success": ok, "failed": failed}

# 使用
exporter = FBXExporter("export_config.json")
exporter.export_batch(asset_list)
```

**面试追问**："如果导出过程中 UE 崩溃了怎么恢复？"

> "每个资产导出时写状态文件（`_export_state.json`），记录哪些已完成。重新运行工具时读状态文件，跳过已完成的部分。这是典型的断点续传模式——我在 Houdini PDG 批量 Cook 场景中也用类似的思路。"

---

### 场景 3：资产检查器

**问题**："写一个自动检查场景规范的工具（命名、材质、UV、LOD）。"

**回答**：

```python
class AssetChecker:
    """可配置的资产合规检查器 —— 检查规则全部 JSON 驱动"""
    
    def __init__(self, rules_path):
        self.rules = json.loads(Path(rules_path).read_text())
        self.issues = []
    
    def check(self, asset_path):
        """运行全部检查，返回问题列表"""
        self.issues = []
        
        for rule in self.rules["checks"]:
            if not rule.get("enabled", True):
                continue
            
            method = getattr(self, f"_check_{rule['id']}", None)
            if method:
                method(asset_path, rule)
            else:
                self.issues.append({
                    "severity": "warning",
                    "rule": rule["id"],
                    "message": f"No checker for {rule['id']}"
                })
        
        return self._generate_report()
    
    def _check_naming(self, path, rule):
        """检查命名规范"""
        name = Path(path).stem
        pattern = rule.get("pattern", r"^SM_[A-Za-z0-9_]+$")
        if not re.match(pattern, name):
            self.issues.append({
                "severity": "error",
                "rule": "naming",
                "message": f"'{name}' doesn't match '{pattern}'",
                "auto_fix": False  # 命名不能自动修
            })
    
    def _check_triangle_count(self, path, rule):
        """检查面数"""
        tri_count = self._get_triangle_count(path)
        max_tris = rule.get("max", 50000)
        
        if tri_count > max_tris:
            severity = "error" if tri_count > max_tris * 1.5 else "warning"
            self.issues.append({
                "severity": severity,
                "rule": "triangle_count",
                "message": f"{tri_count} tris > {max_tris}",
                "current": tri_count,
                "limit": max_tris,
                "auto_fix": True  # 可以自动减面
            })
    
    def _check_texture_size(self, path, rule):
        """检查贴图分辨率"""
        textures = self._get_textures(path)
        max_size = rule.get("max", 2048)
        
        for tex in textures:
            width, height = tex["size"]
            if max(width, height) > max_size:
                self.issues.append({
                    "severity": "warning",
                    "rule": "texture_size",
                    "message": f"{tex['name']} is {width}x{height} > {max_size}",
                    "auto_fix": True  # 可以自动缩贴图
                })
    
    def _generate_report(self):
        """生成检查报告"""
        errors = [i for i in self.issues if i["severity"] == "error"]
        warnings = [i for i in self.issues if i["severity"] == "warning"]
        
        return {
            "asset": "...",
            "passed": len(self.issues) == 0,
            "errors": len(errors),
            "warnings": len(warnings),
            "issues": self.issues
        }

# 配置文件 — rules.json
{
    "checks": [
        {"id": "naming", "enabled": true, "pattern": "^SM_[A-Za-z0-9_]+$"},
        {"id": "triangle_count", "enabled": true, "max": 50000},
        {"id": "texture_size", "enabled": true, "max": 2048},
        {"id": "uv_channels", "enabled": true, "min": 1, "max": 3},
        {"id": "lod_count", "enabled": true, "min": 3}
    ]
}
```

> **面试闪光点**："规则全部 JSON 驱动——新增检查项不需要改代码，美术也能加规则。`auto_fix` 字段区分哪些问题可以自动修复（如贴图缩尺寸）vs 必须手动改（如命名不规范）。我就是用这个模式做的 [[QA简历面试题#Q15 盘丝洞性能优化]] 中的资产规范化检查。"

---

### 场景 4：多 DCC 数据传递

**问题**："Maya 和 Houdini 之间如何传递数据？"

**回答**（结合你简历中 Houdini→UE 三通路经验）：

| 数据类型 | 推荐格式 | 理由 |
|----------|----------|------|
| **静态 Mesh** | FBX | 最兼容、LOD 组支持好 |
| **场景层级+材质+变体** | USD | 多 DCC 协作、非破坏性编辑 |
| **大量散布点** | JSON/CSV | 轻量、人类可读、易调试 |
| **地形数据** | 16-bit RAW (Heightmap) | 直接导入 Landscape |
| **骨骼动画** | FBX 或 Alembic | 各有优劣 |
| **顶点动画** | VAT 贴图 (EXR) | 替代骨骼动画降 DrawCall |
| **配置/参数** | JSON | 轻量、版本管理友好 |

**Houdini → UE 你的实际三通路**：

```python
# === 通路 1: Heightmap → UE Landscape ===
hou.node("/obj/terrain/heightfield_output").parm("sopoutput").set(
    "D:/Project/Landscape/terrain.r16"  # 16-bit RAW
)

# === 通路 2: FBX → UE Static Mesh ===
rop = hou.node("/out").createNode("filmboxfbx", "export_buildings")
rop.parm("sopoutput").set("D:/Project/Meshes/city_blocks.fbx")
rop.parm("execute").pressButton()

# === 通路 3: Point Cloud → UE PCG Graph ===
import csv
geo = hou.node("/obj/city/OUT_POINTS").geometry()
with open("D:/Project/PCG/city_points.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "z", "species", "scale", "seed"])
    for pt in geo.points():
        pos = pt.position()
        writer.writerow([
            pos.x(), pos.y(), pos.z(),
            pt.attribValue("species"),
            pt.attribValue("pscale"),
            int(pt.attribValue("seed"))
        ])
```

> **你的项目**：[[00_技术美术 简历_PCG方向#Houdini→UE 数据桥接]] 中详细写了这三条通路——面试时讲这个比抽象讨论更有说服力。

---

### 场景 5：性能排查——"导出太慢"

**问题**："批量导出 FBX 非常慢，如何定位和优化？"

**回答**：

> "分四步走——Profile 定位 → 分析瓶颈 → 针对性优化 → 量化验证。"

```
Step 1: Profile 定位瓶颈
├── 用 cProfile 跑一次导出
├── 发现 80% 时间在 cmds.file(export=True)
└── 而不是在处理逻辑

Step 2: 分析根本原因
├── 每个资产独立 file open → export → close
├── 每次 export 都会触发 Maya 的 pre/post export 回调
└── 有些不必要的验证在 export 时执行

Step 3: 针对性优化
├── 用 subprocess 并行导出（多进程绕过 GIL）
├── 每个进程独立导出 1/N 的资产
├── 减少单个导出包含的内容（只导出当前选中，不做全场景导出）
└── 禁用不必要的 export 回调

Step 4: 验证
├── 优化前：100 资产 = 45 分钟
├── 优化后：4 进程并行 = 12 分钟
└── 效率提升 73%
```

**代码骨架**：

```python
from concurrent.futures import ProcessPoolExecutor
import subprocess
import json

def export_worker(asset_info):
    """独立进程导出单个资产"""
    script = f"""
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

cmds.file('{asset_info['scene']}', open=True)
cmds.select('{asset_info['root_group']}')
cmds.file('{asset_info['output']}', exportSelected=True, type='FBX export')
"""
    return subprocess.run(
        ["mayapy", "-c", script],
        capture_output=True, text=True, timeout=300
    )

def parallel_export(assets, max_workers=4):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(export_worker, assets))
    return results
```

---

## 八、进阶 Python（TA 面试一般不会深问，但要知道概念）

### 33. `__slots__` 的作用

> "减少内存占用。当你需要创建几十万个对象时（如 PCG 点数据），用 `__slots__` 禁止动态添加属性，内存减少约 50%。TA 中主要用于处理海量点云的中间数据结构。"

### 34. `dataclasses` 和 `pydantic`

> "`dataclasses`（Python 3.7+）自动生成 `__init__`/`__repr__`/`__eq__`，减少样板代码。`pydantic` 更进一步——加运行时类型验证，适合管线配置的 schema 校验。"

```python
from dataclasses import dataclass

@dataclass
class AssetInfo:
    name: str
    path: str
    tri_count: int
    material_count: int = 1  # 默认值
    
    @property
    def is_valid(self):
        return self.tri_count < 100000

# 使用 — 比 dict 更明确
asset = AssetInfo(name="Wall_01", path="/meshes/wall.fbx", tri_count=4500)
print(asset.is_valid)  # True
```

### 35. C 扩展（ctypes / pybind11）

> "当纯 Python 性能不够时——比如实时处理百万顶点的几何体——用 C/C++ 扩展。pybind11 是推荐方案，Maya OpenMaya 和 UE Python API 底层都是这种模式。我目前能阅读但还不会写——这是我学习计划中的 P0 项。"

---

## 九、面试自检清单——针对你的背景

### 面试时必须能说清楚的

| # | 问题 | 你的答案锚点 | 状态 |
|---|------|-------------|:--:|
| 1 | Python 在 Houdini 中的具体用途 | [[网易面试回答#Q6 VEX vs Python]] | ☐ |
| 2 | 装饰器原理 + 写一个计时装饰器 | 本文第 6 题 | ☐ |
| 3 | 批量重命名的 dict 映射策略 | 本文场景 1 | ☐ |
| 4 | 你的贴图批量处理脚本具体做了什么 | [[QA简历面试题#Q17]] | ☐ |
| 5 | DCC 主线程问题 + 解决方案 | 本文第 20 题 | ☐ |
| 6 | Qt 信号槽 + QThread 不阻塞 UI | 本文第 22-23 题 | ☐ |
| 7 | 生成器 vs 列表 + 点云处理场景 | 本文第 7 题 | ☐ |
| 8 | JSON 配置驱动 vs 硬编码 | 本文第 25 题 | ☐ |
| 9 | Context Manager + Undo 禁用场景 | 本文第 12 题 | ☐ |
| 10 | AI 辅助写 Python 的流程 + 踩坑 | [[网易面试回答#Q23]] | ☐ |

### 面试话术模板

**当面试官问"你 Python 水平怎么样"时**：

> "我的 Python 是面向 TA 管线开发的实战水平——不是纯计算机的算法向，而是大量用于 DCC 工具开发、批量处理脚本、管线自动化。
>
> 具体来说：Houdini 中我用 hou 模块创建节点网络、批量 Cook HDA、读取几何体属性；Maya 中写批量导入导出、资产整理工具；Qt 方面做过带进度条的工具面板。
>
> 另外我重度使用 GPT/Claude 辅助写 Python——伪代码→AI初版→逐行Review→测试验证，效率提升 2-3 倍。但我能判断 AI 代码的正确性，不是盲目粘贴。
>
> 薄弱的方面是数据结构算法、复杂度分析这些纯 CS 基础——但我工作中需要的高性能操作会切到 VEX 或 C++ API，所以 Python 层面的算法优化不是我的日常重点。"

---

> [!NOTE] 使用建议
> 1. 面试前重点练习**加粗标记**的题（第 3/6/12/15/20/23 题——这些是网易/腾讯面经中出现过的）
> 2. 每个知识点都往你的项目上引——"这个我在 PSD 体块工具里用过" 比 "这个我知道" 强 10 倍
> 3. 代码题不用背原文，但要能**口述逻辑 + 关键 API 名**
> 4. 搭配 [[网易面试回答]] 和 [[QA简历面试题]] 一起复习
