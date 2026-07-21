---
title: 3D Gaussian Splatting 历史发展
date: 2026-07-01
tags:
  - 3DGS
  - NeRF
  - 历史
  - PCG
  - TA
---

# 3D Gaussian Splatting 历史发展

> 3D Gaussian Splatting（3DGS）是 2023 年横空出世的新视角合成与场景表示技术，以其**显式表示、实时渲染、高质量重建**三大特点迅速成为计算机视觉和图形学领域的主流方向。

---

## 一、前传：NeRF 开启神经渲染时代

### 2020 年：NeRF 诞生

Mildenhall 等人发表 **NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis**，提出用 MLP 隐式建模 3D 场景。

**NeRF 的核心贡献**：
- 用神经网络编码体积密度和颜色
- 通过体渲染生成新视角图像
- 开启了**神经辐射场**研究方向

**NeRF 的局限**：
- 训练和渲染速度慢
- 需要大量视角
- 是隐式表示，难以编辑和交互

### 2020-2022：NeRF 的爆发期

- **Instant-NGP**（NVIDIA, 2022）：用哈希编码加速 NeRF
- **Plenoxels**：用稀疏体素网格替代 MLP
- **Mip-NeRF 360**：抗锯齿和无限远场景
- **TensoRF**：张量分解压缩 NeRF
- **NeRFstudio**、**nerfies**、**HyperNeRF** 等动态 NeRF 方法

这些工作都在探索：**如何在保持质量的同时提升速度和可编辑性**。

---

## 二、3DGS 的诞生（2023）

### 2023 年 8 月：3D Gaussian Splatting 论文发布

Kerbl、Kopanas、Leimkühler、Drettakis 在 **SIGGRAPH 2023** 发表论文：

**"3D Gaussian Splatting for Real-Time Radiance Field Rendering"**

### 核心创新

1. **显式 3D 高斯表示**
   - 用数百万个 3D 高斯椭球表示场景
   - 每个高斯包含：位置、协方差、颜色（球谐函数 SH）、不透明度

2. **可微分光栅化**
   - 定制 CUDA 光栅化管线
   - 避免 NeRF 的逐像素光线 marching
   - 实现 **1080p 实时渲染**

3. **自适应密度控制**
   - 从 SfM 点云初始化
   - 通过梯度控制高斯的克隆与分裂
   - 自动填补空洞、去除浮点

4. **高质量 + 实时**
   - 在质量接近 NeRF 的同时，渲染速度提升数个数量级

### 影响

- 被视为 NeRF 之后最重要的 3D 重建方向
- 迅速被计算机视觉、图形学、机器人、SLAM、AIGC 等领域吸收
- 催生了大量开源实现和商业应用

---

## 三、2023 下半年：生态初步建立

### 开源实现爆发

- **官方实现**（graphdeco-inria/gaussian-splatting）
- **nerfstudio gsplat**
- **UnityGaussianSplatting**（Aras Pranckevičius）
- **Splat Viewer**、**Gauzilla** 等 Web 查看器

### 技术方向萌芽

- **压缩**：减少存储和显存占用
- **动态场景**：从静态 3DGS 到 4DGS
- **编辑**：分割、风格化、对象操作
- **SLAM**：用 3DGS 做实时建图

---

## 四、2024 年：多方向快速演进

### 1. 压缩与轻量化

目标：让 3DGS 能在移动端、Web、AR 上运行。

代表工作：
- **Mip-Splatting**：解决 3DGS 的混叠问题
- **Scaffold-GS**：用锚点高斯减少冗余
- **Compact-3DGS**、**LightGaussian**、**GaussianPro**、**EAGLES**
- **SPLATTING 压缩格式**：如 .splat、.spz、.ksplat

### 2. 动态/4D Gaussian Splatting

- **D-3DGS**、**4D Gaussian Splatting**：用变形场或 4D 神经体扩展时间维度
- **Deformable 3DGS**：用 MLP 学习时序变形
- 应用于：人物表演、动态物体、自由视角视频

### 3. 3DGS + SLAM

- **Gaussian Splatting SLAM**（Imperial College）
- **SplaTAM**、**GS-SLAM**、**Photo-SLAM**
- 3DGS 开始挑战传统点云/体素 SLAM 方案

### 4. 3DGS 编辑与风格化

- **GaussianEditor**、**Gaussian Grouping**：语义编辑
- **SplaTAM**、**PhysGaussian**：物理交互
- **DreamGaussian**、**GaussianDreamer**：文本/图像生成 3DGS

### 5. 工业界采用

- **NVIDIA**：将 3DGS 集成到 Omniverse、Neuralangelo 后续工作
- **Google**：在地图、AR 中探索 3DGS
- **Meta**：用于 Codec Avatars、空间视频
- **Apple**：Vision Pro 空间计算相关探索
- **游戏行业**：Unity/Unreal 插件、3D 扫描资产管线

---

## 五、2025 年：从研究走向生产

### 1. 生成式 3DGS 成熟

- 图像/文本直接生成 3DGS 资产
- 与扩散模型、多视图生成模型结合
- 3DGS 成为 AIGC 3D 的主流输出格式之一

### 2. 大世界与自动驾驶

- **Street Gaussians**、**DrivingGaussian**
- 用 3DGS 重建城市街道、动态车辆
- 与自动驾驶仿真结合

### 3. 数字人与化身

- **Gaussian Avatars**、**GaussianHead**
- 高保真可驱动数字人
- 单目视频驱动 3DGS 头像

### 4. 工具链完善

- **SuperSplat**、**SplatTransform** 等编辑工具
- Blender、Houdini 插件
- 商业扫描 App 开始输出 3DGS

---

## 六、2026 年：全面工程化与跨领域融合

根据 2026 年 6 月的最新 arXiv 论文趋势，3DGS 已进入**全面工程化**阶段：

### 1. SLAM 与大尺度场景

- **KiloGS-SLAM**：千米级室外 SLAM
- **MyGO-Splat**：RGB-only 闭环几何反馈
- **Spectral GS-SLAM**：退化鲁棒跟踪

### 2. 移动端与实时系统

- **Monte Carlo Energy Aggregation for Mobile 3DGS**
- **ACE-GS**、**ACEsplat**：轻量、紧凑、高效

### 3. 动态/4D 深化

- **L2D2-GS**：前馈动态重建
- **Multi4D**、**SemDynReg**、**Temporally Aware Densification**
- 动态 3DGS 开始支持**物理模拟和编辑**

### 4. 物理交互与可编辑性

- **Scene-Level Heterogeneous Physics Simulation with 3DGS**
- **MeGAS**：热力学相变编辑
- **RAGA**：实时高斯阴影投射
- **CubifyGS**：物体级场景维护

### 5. 与 USD/PCG/引擎的深度整合

- Houdini、UE5、Unity 的 3DGS 插件成熟
- 3DGS 资产通过 USD 进入传统 DCC 管线
- PCG 生成 + 3DGS 扫描的混合工作流出现

---

## 七、3DGS 发展时间线

| 时间 | 事件 |
|------|------|
| 2020 | NeRF 诞生，开启神经渲染时代 |
| 2022 | Instant-NGP、Plenoxels 等加速 NeRF 方法出现 |
| 2023.08 | 3D Gaussian Splatting 论文在 SIGGRAPH 发布 |
| 2023 H2 | 开源实现爆发，Web/Unity/Unreal 查看器涌现 |
| 2024 | 压缩、动态 3DGS、SLAM、编辑方向快速发展 |
| 2025 | 生成式 3DGS、大世界自动驾驶、数字人应用成熟 |
| 2026 | SLAM 大尺度、移动端、物理交互、USD/引擎整合成为主流 |

---

## 八、3DGS 为什么成功？

1. **显式表示**：比 NeRF 的隐式 MLP 更容易理解、编辑和导出
2. **实时渲染**：定制 CUDA 光栅化达到实时帧率
3. **高质量**：在新视角合成上媲美或超越 NeRF
4. **可扩展性**：容易扩展到动态、SLAM、生成、物理等领域
5. **开源生态**：官方代码质量高，社区迅速跟进
6. **工程友好**：可与现有图形管线、游戏引擎、DCC 工具整合

---

## 九、与相关技术的关系

```text
NeRF (2020)
  ↓ 加速与显式化
Instant-NGP / Plenoxels (2022)
  ↓ 完全显式 + 可微光栅化
3D Gaussian Splatting (2023)
  ↓ 扩展时间、物理、生成
4DGS / Dynamic GS / GS-SLAM / Generative GS (2024-2026)
  ↓ 工业集成
USD / UE5 / Unity / Houdini / Omniverse (2025-2026)
```

---

## 十、参考资源

- [3D Gaussian Splatting 官方论文](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
- [官方 GitHub 实现](https://github.com/graphdeco-inria/gaussian-splatting)
- [Awesome 3D Gaussian Splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting)
- [NeRF 论文](https://www.matthewtancik.com/nerf)
- [arXiv 3DGS 搜索](https://arxiv.org/search/?query=%223D+Gaussian+Splatting%22&searchtype=all&source=header&order=-announced_date_first)

---

## 相关笔记

- [[USD_历史发展]]
- [[USD_流程概念]]
