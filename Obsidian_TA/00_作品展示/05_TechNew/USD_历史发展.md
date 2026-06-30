---
title: USD 历史发展
date: 2026-06-30
tags:
  - USD
  - Pipeline
  - 历史
  - TA
  - PCG
---

# USD 历史发展

> USD（Universal Scene Description）从 Pixar 内部工具起步，逐步发展为跨行业 3D 数据交换标准。本笔记梳理 USD 从诞生到成为工业标准的关键节点。

---

## 一、诞生背景：Pixar 的内部需求

### 2000s：影视动画的场景复杂度爆炸

Pixar 在制作《海底总动员》《汽车总动员》《机器人总动员》等电影时，面临以下问题：

- 场景规模从几百个对象增长到**数百万个对象**
- 多个部门（模型、绑定、动画、特效、灯光）需要同时修改同一场景
- 传统 Maya 场景文件体积庞大、加载慢、协作困难
- 不同 DCC 之间的数据交换频繁丢失信息

### 2010-2012：Presto 与 USD 雏形

Pixar 开发了自己的动画系统 **Presto**，并在此过程中逐步抽象出一套可组合、可扩展、可分层的场景描述格式。这就是 USD 的前身。

**核心设计目标**：
- 高效处理**超大规模场景**
- 支持**非破坏性协作**（多个部门同时工作）
- 提供**程序化接口**（Python/C++）
- 实现**DCC 之间的无损交换**

---

## 二、开源与早期发展（2016-2018）

### 2016 年：USD 开源

Pixar 在 **SIGGRAPH 2016** 上正式将 USD 开源，并发布在 GitHub 上。

- 初始版本包含核心库：`Usd`、`UsdGeom`、`UsdShade`、`UsdLux`、`UsdSkel` 等
- 提供了 `.usda`（ASCII）、`.usdc`（二进制）、`.usdz`（压缩包）三种文件格式
- 首次公开了 **Composition Arcs**、**Variant**、**Payload** 等核心概念

### 2017 年：工业界开始关注

- **Apple** 注意到 USD 的潜力，开始与 Pixar 合作推动移动端 3D 格式
- **Autodesk** 在 Maya 中开始集成 USD
- 影视行业逐渐形成共识：USD 可能成为下一代场景数据标准

### 2018 年：加入 Academy Software Foundation

USD 成为 **Academy Software Foundation（ASWF）** 旗下的开源项目之一，与 OpenVDB、OpenColorIO、MaterialX 等并列。

意义：
- 获得好莱坞主要工作室（迪士尼、梦工厂、维塔、工业光魔等）的支持
- 治理结构更加开放
- 成为影视 VFX 和动画行业的标准候选者

---

## 三、生态扩张期（2019-2021）

### 2019 年：Apple 推出 USDZ

Apple 在 WWDC 2019 发布 **USDZ**，这是 USD 的压缩打包格式，专为移动端 AR 设计。

- USDZ 是**只读**的 zip 格式，可直接嵌入 iOS App
- 与 ARKit、Reality Composer 深度集成
- 推动了 USD 在消费级 AR/VR 领域的应用

### 2020 年：NVIDIA Omniverse

NVIDIA 宣布 **Omniverse** 平台，将 USD 作为核心场景描述格式。

- Omniverse 提供 USD 协作服务器（Nucleus）
- 支持 Maya、3ds Max、Blender、UE、Revit 等 DCC 实时协作
- 把 USD 从影视 VFX 推向工业设计、建筑、数字孪生

### 2021 年：USD 与游戏引擎

- **Unreal Engine 4.27 / UE5** 开始支持 USD Stage Actor
- **Unity** 推出 USD 导入工具
- 游戏行业开始关注 USD 作为中间格式，尤其是在影视级游戏和开放世界中

---

## 四、标准化与联盟阶段（2022-2024）

### 2022 年：OpenUSD 概念提出

Pixar 联合 **Adobe、Apple、Autodesk、NVIDIA** 等公司提出 **OpenUSD**，强调 USD 的开放性、互操作性和标准化。

### 2023 年：Alliance for OpenUSD（AOUSD）成立

2023 年 8 月，**Alliance for OpenUSD（AOUSD）** 正式成立，创始成员包括：

- Pixar
- Adobe
- Apple
- Autodesk
- NVIDIA
- Linux Foundation
- 以及后续加入的 Siemens、Sony、Intel、Meta、Samsung 等

**AOUSD 的目标**：
- 推动 USD 成为**国际标准**
- 制定 USD 规范、测试套件和认证流程
- 促进 USD 在**影视、游戏、AEC、制造、汽车、机器人**等行业的采用

### 2024 年：USD 标准化加速

- USD 开始进入 **ISO/IEC 标准化流程**
- 更多行业工具原生支持 USD（Houdini Solaris、Katana、Mari、Substance 等）
- 3D 生成式 AI 工具开始直接输出 USD 格式

---

## 五、近期趋势（2025-2026）

### 1. USD 成为 AIGC 3D 的关键中间格式

随着生成式 3D 模型的发展，USD 成为：
- 文本/图像生成 3D 资产的输出格式
- 3D Gaussian Splatting 与传统 Mesh 场景融合的容器
- AI 驱动的程序化生成与手工资产整合的桥梁

### 2. 空间计算与 Apple Vision Pro

Apple Vision Pro 和 visionOS 进一步推动 USD/USDZ 在：
- 空间视频
- 沉浸式应用
- 3D UI 和空间交互

中的应用。

### 3. 数字孪生与工业元宇宙

- 汽车、航空、建筑行业采用 USD 作为数字孪生基础格式
- NVIDIA Omniverse 与 Siemens Xcelerator、Bentley、Adobe 等深度整合
- USD 与 IoT、仿真、AI 推理的结合

### 4. 游戏行业的深入渗透

- 开放世界游戏开始用 USD 管理大地图资产
- UE5 的 USD 支持持续增强
- PCG 工具（如 Houdini）与 USD 原生集成，形成 Houdini→USD→UE 管线

---

## 六、USD 发展时间线

| 年份 | 事件 |
|------|------|
| 2010-2012 | Pixar 内部开发 USD 雏形，配合 Presto 动画系统 |
| 2016 | Pixar 在 SIGGRAPH 开源 USD |
| 2017 | Apple、Autodesk 开始集成 USD |
| 2018 | USD 加入 Academy Software Foundation |
| 2019 | Apple 推出 USDZ，用于 ARKit |
| 2020 | NVIDIA 发布 Omniverse，以 USD 为核心 |
| 2021 | UE5 / Unity 开始支持 USD |
| 2022 | OpenUSD 概念提出 |
| 2023 | Alliance for OpenUSD（AOUSD）成立 |
| 2024 | USD 进入 ISO 标准化流程，AIGC 3D 工具广泛采用 |
| 2025-2026 | USD 扩展至空间计算、数字孪生、机器人、生成式 3D |

---

## 七、USD 为何能成功？

1. **Pixar 的真实需求驱动**：不是实验室产物，而是为了解决实际生产问题
2. **开放的组合架构**：Reference、Payload、Variant 让大规模协作成为可能
3. **DCC 中立**：不绑定任何单一软件
4. **性能优先**：二进制格式 `.usdc` 加载快，支持延迟加载
5. **程序化友好**：Python/C++ API 完善，适合自动化和 PCG
6. **大厂联盟推动**：Apple、NVIDIA、Adobe、Autodesk 共同背书
7. **恰逢 AIGC 和空间计算浪潮**：3D 数据交换需求激增

---

## 八、参考资源

- [OpenUSD 官方历史](https://openusd.org/release/index.html)
- [Pixar USD 开源公告（2016）](https://openusd.org/release/dl_usd.html)
- [Alliance for OpenUSD](https://aousd.org/)
- [Academy Software Foundation - USD](https://www.aswf.io/projects/openusd/)
- [NVIDIA Omniverse USD](https://www.nvidia.com/en-us/omniverse/usd/)
- [Apple USDZ 文档](https://developer.apple.com/documentation/arkit/usdz)

---

## 相关笔记

- [[00_作品展示/05_TechNew/USD_流程概念]]
- [[00_作品展示/02_PCG研究/3DGS_最新发展_2026]]
