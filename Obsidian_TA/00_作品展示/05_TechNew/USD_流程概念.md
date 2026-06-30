---
title: USD 流程概念及项目应用流程
date: 2026-06-30
tags:
  - USD
  - Pipeline
  - TA
  - PCG
  - 技术美术
---

# USD 流程概念及项目应用流程

> USD（Universal Scene Description，通用场景描述）是 Pixar 开源的一套场景数据交换与组合标准。最初用于影视动画大场景协作，现在已成为游戏、数字孪生、AIGC 3D 工业的事实标准之一。

---

## 一、USD 核心概念

### 1. 分层（Layering）

USD 把场景拆成多个 `.usd` / `.usda`（ASCII）/ `.usdc`（二进制）/ `.usdz`（压缩包）文件，通过**图层叠加**组合成最终场景。

```text
scene.usd
├── environment.usd      # 环境/地编
├── characters.usd       # 角色
├── props.usd            # 道具
└── lighting.usd         # 灯光
```

每个图层只负责一部分，互不破坏。

### 2. Prim（基本单元）

场景中的每个对象都是一个 **Prim**（primitive），类似场景图中的节点：

- `/World/Environment/Building_01`
- `/World/Characters/Hero`
- `/World/Lighting/KeyLight`

每个 Prim 可以有：
- **Transform**（位置/旋转/缩放）
- **Mesh / Material / Light / Camera**
- **自定义属性**

### 3. 组合机制（Composition Arcs）

这是 USD 最强大的部分：

| 机制 | 作用 | 类比 |
|------|------|------|
| **Reference** | 引用外部 USD 文件到当前场景 | 软链接/实例化 |
| **Payload** | 懒加载引用，按需加载 | 异步加载 |
| **Variant** | 同一 Prim 的多套变体 | LOD / 风格切换 |
| **Inherit** | 继承基类 Prim 的属性 | OOP 继承 |
| **Specialize** | 特化，继承但可覆盖 | 模板覆盖 |

### 4. Variant Set（变体集）

例如一个建筑 Prim 可以设置变体：

```usd
def "Building_A" (
    variants = {
        string style = "modern"
        string lod = "high"
    }
)
```

同一资产可以切换风格/LOD/损坏状态，美术只维护一个源文件。

### 5. Stage（舞台）

USD **Stage** 是运行时加载后的完整场景视图。多个 Layer 叠加后，最终呈现在 Stage 上。

---

## 二、为什么项目要用 USD？

| 优势 | 说明 |
|------|------|
| **非破坏性协作** | 地编、灯光、动画、特效各自改自己的 Layer，不互相覆盖 |
| **大数据量** | 支持延迟加载（Payload）、实例化、流式加载 |
| **DCC 互通** | Houdini、Maya、Blender、UE、Omniverse、Katana 都支持 |
| **资产可追溯** | 每个 Prim 的来源、版本、引用关系清晰 |
| **程序化友好** | 有 Python API，适合 PCG/Houdini 批量生成 |
| **AIGC 互通** | 越来越多的生成式 3D 工具直接输出 USD |

---

## 三、USD 项目应用流程

### 阶段 1：资产制作（Asset Build）

```text
assets/
├── characters/
│   └── hero/
│       ├── model.usd          # 模型
│       ├── lookdev.usd        # 材质/贴图
│       ├── rig.usd            # 绑定
│       └── hero.usd           # 组合引用以上
├── props/
│   └── crate/
│       ├── model.usd
│       ├── lookdev.usd
│       └── crate.usd
└── environments/
    └── city_block/
        ├── buildings.usd
        ├── roads.usd
        └── city_block.usd
```

每个资产自底向上组装：

```text
hero.usd
  ├── reference → model.usd
  ├── reference → lookdev.usd
  └── reference → rig.usd
```

### 阶段 2：Shot / Level 组装

影视中以镜头为单位，游戏中以关卡为单位：

```text
shot_010.usd
  ├── reference → assets/environments/city_block/city_block.usd
  ├── reference → assets/characters/hero/hero.usd
  ├── reference → assets/props/crate/crate.usd
  └── layer → lighting_shot_010.usd
```

### 阶段 3：部门协作 Layer

```text
shot_010/
├── shot_010_layout.usd        # 地编/布局
├── shot_010_animation.usd     # 动画
├── shot_010_fx.usd            # 特效
├── shot_010_lighting.usd      # 灯光
└── shot_010_comp.usd          # 合成/最终输出
```

每个部门在自己的 Layer 工作，通过 `subLayer` 叠加。

### 阶段 4：渲染/引擎输出

- **影视**：导入 Katana / Solaris / Renderman / Arnold 渲染
- **游戏**：导入 UE5 / Unity，或直接使用 Omniverse 做中转
- **数字孪生**：通过 USD Connector 同步到各种 RT3D 引擎

---

## 四、USD 与 PCG/技术美术的结合

作为 PCG TA，USD 可以在以下环节发挥作用：

### 1. Houdini → USD → UE

Houdini Solaris 原生基于 USD，PCG 生成的城市、植被、道路可以直接输出为 `.usd`，再导入 UE：

```text
Houdini PCG
   ↓
生成 USD（带 Variant：LOD/风格）
   ↓
UE5 通过 USD Stage Actor 加载
   ↓
运行时切换 Variant / Payload
```

### 2. 程序化资产生成

用 Python USD API 批量生成资产：

```python
from pxr import Usd, UsdGeom, Sdf

stage = Usd.Stage.CreateNew("city_block.usda")
world = stage.DefinePrim("/World")
building = UsdGeom.Mesh.Define(stage, "/World/Building_01")
# 设置顶点、UV、材质引用...
stage.GetRootLayer().Save()
```

### 3. 大世界场景管理

- 用 **Payload** 实现地块流式加载
- 用 **Variant** 实现同一建筑的多种风格/LOD
- 用 **Reference** 实现实例化，减少重复数据

### 4. 与 AI/3DGS 结合

越来越多的 AI 生成 3D 工具输出 USD，PCG 管线可以把：
- **生成式 3D 资产**（USD）
- **3DGS 扫描场景**
- **Houdini 程序化场景**

统一汇总到 USD Stage 中做二次编辑。

---

## 五、常用工具链

| 工具 | USD 支持 |
|------|----------|
| **Houdini / Solaris** | 原生 USD，PCG 输出首选 |
| **Maya** | USD Plugin（Maya USD） |
| **Blender** | 第三方 USD 导入导出 |
| **UE5** | USD Stage Actor、USD Importer |
| **Omniverse** | NVIDIA 的 USD 协作平台 |
| **Katana** | 影视灯光合成，原生 USD |
| **Substance / SpeedTree** | 可输出 USD 格式资产 |

---

## 六、USD 在项目中的最佳实践

1. **一个资产一个 Root Prim**：例如 `/World/Assets/Building_A`
2. **模型与材质分离**：`model.usd` 引用 `lookdev.usd`
3. **善用 Variant**：LOD、风格、季节、损坏状态
4. **Payload 懒加载**：大世界场景一定开 Payload，否则启动慢
5. **命名规范统一**：Prim path 是场景的数据库索引
6. **版本控制友好**：`.usda` 是文本，便于 Git diff；`.usdc` 用于发布
7. **Python 自动化**：批量检查、修复、发布 USD 资产
8. **与现有流程兼容**：USD 是中间格式，不强制替换原有 DCC

---

## 七、与游戏引擎对接的简化流程

```text
资产制作（Maya/Blender/Houdini）
        ↓
导出 USD（模型+材质+变体）
        ↓
USD Asset Build（检查、规范、打包）
        ↓
关卡 USD（引用各资产 + 布局 + 灯光）
        ↓
UE5 / Unity / 自研引擎
        ↓
运行时 Variant / Payload 控制
```

---

## 八、学习资源

- [OpenUSD 官方文档](https://openusd.org/release/index.html)
- [NVIDIA Omniverse USD 文档](https://docs.omniverse.nvidia.com/usd/latest/index.html)
- [Houdini Solaris USD 文档](https://www.sidefx.com/docs/houdini/solaris/index.html)
- [UE5 USD 文档](https://docs.unrealengine.com/5.0/en-US/USD-in-Unreal-Engine/)
