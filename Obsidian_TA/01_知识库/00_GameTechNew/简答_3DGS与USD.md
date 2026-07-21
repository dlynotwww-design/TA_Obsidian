---
title: 3DGS & USD 面试简答
date: 2026-07-21
tags:
  - 3DGS
  - USD
  - 面试
  - TA
  - PCG
---

# 3DGS & USD 面试简答

> 综合自 [[3DGS_历史发展]]、[[3DGS_最新发展_2026]]、[[USD_历史发展]]、[[USD_流程概念]]

---

# 第一部分：3D Gaussian Splatting

## 一句话

**3DGS 用数百万个带颜色的 3D 高斯椭球显式表示场景，通过可微分 CUDA 光栅化实现 1080p 实时渲染，是 NeRF 之后最重要的新视角合成技术。**

## 30 秒版本

NeRF（2020）用 MLP 隐式建模场景，质量好但太慢。3DGS（SIGGRAPH 2023）把场景换成**显式的 3D 高斯椭球**——每个高斯自带位置、形状、颜色（球谐函数）、不透明度——然后用定制 CUDA 光栅化直接画到屏幕上，不需要 NeRF 那种逐像素光线 marching。结果：**质量接近 NeRF，速度快几个数量级，而且因为是显式表示，天然可编辑。**

## 核心创新（四个）

| 创新 | 做了什么 | 为什么重要 |
|------|----------|-----------|
| **显式高斯表示** | 场景 = 数百万个 3D 高斯椭球，每个存位置+协方差+SH 颜色+不透明度 | 可见、可编辑，不依赖黑盒 MLP |
| **可微分光栅化** | 定制 CUDA 管线，把高斯投影到屏幕再混合 | 1080p 实时渲染，告别逐像素 marching |
| **自适应密度控制** | 从 SfM 点云初始化，梯度驱动克隆/分裂/剔除 | 自动填补空洞、去除浮点伪影 |
| **球谐函数颜色** | 用 SH 系数编码视角相关颜色 | 高光、反射等视角相关效果自然呈现 |

## 和 NeRF 的对比

| | NeRF | 3DGS |
|---|---|---|
| 表示方式 | 隐式（MLP 权重） | 显式（高斯椭球） |
| 渲染速度 | 慢（秒级/帧） | 快（实时 30+ fps） |
| 训练速度 | 小时级 | 分钟级 |
| 可编辑性 | 难（黑盒） | 易（移动/删除高斯） |
| 存储 | 小（MLP 权重） | 大（数百万高斯参数） |
| 代表年份 | 2020 | 2023 |

## 发展脉络（面试一句话带过）

```
NeRF (2020) → Instant-NGP (2022) → 3DGS (2023) → 4DGS/SLAM/生成式 (2024-2025) → 移动端/物理/引擎集成 (2026)
```

## 2026 年最值得关注的五个方向

| 方向 | 代表工作 | 对游戏/TA 的意义 |
|------|---------|-----------------|
| **SLAM 大世界** | KiloGS-SLAM（千米级室外） | 扫描真实城市→数字孪生 |
| **动态/4DGS** | L2D2-GS, Multi4D | 可渲染+可编辑+可物理模拟 |
| **移动端轻量化** | ACE-GS, ACEsplat | 手机/AR 眼镜上用 3DGS |
| **生成式 3DGS** | FLUX3D, OrbitForge | 文字→3D 可渲染场景 |
| **物理交互** | 场景级异构物理, MeGAS | 高斯场景支持刚体/流体/热力学 |

## 和游戏管线的结合点

- **Houdini**：GSOPs 插件，3DGS 视口渲染器
- **UE5**：XV3DGS-UEPlugin
- **Unity**：UnityGaussianSplatting, DynGsplat-unity
- **USD 桥接**：3DGS 资产通过 USD 进入传统 DCC 管线
- **PCG 混合**：扫描实景（3DGS）+ 程序化生成（Houdini）→ USD → 引擎

---

# 第二部分：USD（Universal Scene Description）

## 一句话

**USD 是 Pixar 开源的场景数据交换标准，通过分层叠加（Layering）和组合弧（Composition Arcs）实现非破坏性协作，已成为影视/游戏/AIGC 3D 的事实标准。**

## 30 秒版本

USD 解决的核心问题是：一个大场景里，地编、灯光、动画、特效各自要改自己的部分，不能互相覆盖。USD 的做法是把场景拆成多个**图层（Layer）**，每个部门在自己的图层工作，最后通过**组合弧（Reference、Payload、Variant）**叠加成完整场景。就像 Git 的 branch——每个人在自己的分支改，最后 merge 到一起。

## 五大核心概念

| 概念 | 做什么 | 类比 |
|------|--------|------|
| **Layer（图层）** | 把场景拆成多个 .usd 文件，每个只负责一部分 | Photoshop 图层 |
| **Prim（基本单元）** | 场景中每个对象（`/World/Character/Hero`） | 场景图节点 |
| **Reference（引用）** | 引用外部 USD 文件到当前场景 | 软链接/实例化 |
| **Payload（负载）** | 懒加载引用，按需加载 | 异步加载 |
| **Variant（变体）** | 同一 Prim 多套版本（LOD/风格/季节） | 配置切换 |

## Composition Arcs（组合弧）——USD 的灵魂

```
shot_010.usd
  ├── reference → city_block.usd       # 引用城市资产
  ├── reference → hero.usd             # 引用角色
  │     └── reference → model.usd      #   引用模型
  │     └── reference → lookdev.usd    #   引用材质
  │     └── variant "lod" = "high"     #   选高精度 LOD
  ├── payload → fx.usd                 # 特效懒加载
  └── sublayer → lighting.usd          # 灯光叠加
```

五种组合机制：Reference、Payload、Variant、Inherit、Specialize。每种解决不同的场景组织需求。

## 为什么游戏行业要用 USD？

| 痛点 | USD 怎么解决 |
|------|-------------|
| 多人协作互相覆盖 | 不同部门不同 Layer，非破坏性 |
| 大世界加载慢 | Payload 懒加载 + 实例化 |
| DCC 之间数据丢失 | USD 是 DCC 中立的中间格式 |
| 资产版本混乱 | 每个 Prim 的来源/引用链可追溯 |
| LOD/变体管理复杂 | Variant 原生支持 |
| PCG 输出格式不统一 | Houdini Solaris 原生 USD 输出 |

## 发展时间线（精简）

| 年份 | 事件 |
|------|------|
| 2010-2012 | Pixar 内部开发，配合 Presto 动画系统 |
| 2016 | SIGGRAPH 开源 |
| 2018 | 加入 Academy Software Foundation |
| 2019 | Apple 推出 USDZ（移动 AR） |
| 2020 | NVIDIA Omniverse 以 USD 为核心 |
| 2023 | Alliance for OpenUSD（AOUSD）成立，Pixar/Apple/NVIDIA/Adobe/Autodesk 联合 |
| 2024 | 进入 ISO 标准化流程 |
| 2025-2026 | AIGC 3D 工具广泛输出 USD，空间计算（Vision Pro）推动 USDZ |

## Houdini TA 视角：USD 在管线中的位置

```
Houdini PCG（程序化生成城市/植被/道路）
        ↓
Solaris USD 输出（带 Variant：LOD/风格/损坏状态）
        ↓
USD Asset Build（检查、规范、打包）
        ↓
关卡 USD（引用各资产 + 布局 + 灯光）
        ↓
UE5 USD Stage Actor 加载
        ↓
运行时 Variant/Payload 控制
```

## 3DGS + USD 的交汇（2026 趋势）

**3DGS 负责"扫出来"，USD 负责"管起来"：**

- 3DGS 扫描真实场景 → 导出为 USD 兼容格式
- 3DGS 资产与 Mesh 资产在同一个 USD Stage 中混合编辑
- AI 生成 3D 内容（生成式 3DGS / Meshy / FLUX3D）以 USD 输出
- Houdini PCG 做程序化放大，USD 做统一汇总

**一句话：3DGS 解决"内容从哪来"，USD 解决"内容怎么管"。**

---

# 面试常见追问

## Q: 3DGS 和 NeRF 本质区别是什么？
**A:** NeRF 是隐式表示（场景信息编码在 MLP 权重里），3DGS 是显式表示（场景由可见的高斯椭球组成）。显式意味着：可编辑、可导出、可实时渲染、可与其他图形管线互通。

## Q: 3DGS 的存储开销有多大？怎么解决？
**A:** 一个场景可能数百万高斯，原始存储几百 MB 到 GB 级。解决方案：SH 系数压缩、锚点去冗余（Scaffold-GS）、专用压缩格式（.splat/.spz）、移动端轻量化（ACE-GS）。

## Q: USD 和 FBX/glTF 有什么区别？
**A:** FBX/glTF 是**文件格式**（一个文件 = 一个资产），USD 是**场景描述系统**（多个文件 + 组合逻辑 = 整个场景）。USD 的 Reference/Payload/Variant 是 FBX/glTF 没有的场景组织能力。

## Q: 为什么 USD 有 .usda / .usdc / .usdz 三种格式？
**A:** `.usda`（ASCII）便于 Git diff 和人工阅读；`.usdc`（二进制）加载快，用于发布；`.usdz`（压缩包）用于移动端 AR 分发。

## Q: 作为 TA，3DGS 和 USD 对你的工作有什么实际影响？
**A:** 
- **3DGS**：改变了"内容从哪来"——以后可能扫描一个真实环境就能得到 3D 场景基底，然后程序化叠加细节，不再从零手摆
- **USD**：改变了"内容怎么管"——PCG 生成的海量资产、3DGS 扫描数据、手工制作的道具，都用 USD 统一管理版本、变体、引用关系
- **结合点**：Houdini 做 PCG + USD 做容器 + 3DGS 做基底 = 下一代场景生产管线
