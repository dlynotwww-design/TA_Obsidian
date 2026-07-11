---
title: "Messenger-Copy 项目分析"
source: "https://github.com/arafays/messenger-copy"
created: 2026-06-26
tags:
  - case-study
  - three.js
  - sveltekit
  - reverse-engineering
---

## 项目概述

**arafays/messenger-copy** 是一个 AI 辅助的学习重建项目，目标是复现 [Messenger](https://messenger.abeto.co/)（abeto 出品）的 3D 浏览器游戏。该项目下载了原版生产环境的资产文件，然后围绕它们用 SvelteKit + Three.js 重建游戏逻辑。

> **性质**：逆向工程 + 学习项目，非商业用途。参考资产版权归 abeto 所有。

**仓库规模**：约 1.3GB（主要来自 `reference/` 目录中的原版资产镜像）

---

## 技术栈

| 层 | 选择 |
|----|------|
| 框架 | SvelteKit 2 / Svelte 5 |
| 3D | Three.js r184 |
| 语言 | TypeScript 6.0, GLSL, Python（工具脚本）, Shell |
| 样式 | Tailwind CSS 4 |
| 测试 | Vitest + Playwright |
| 构建 | Vite 8 |

**代码量**（不含参考资产）：

| 语言 | 大小 |
|------|------|
| GLSL | 293 KB |
| TypeScript | 52 KB |
| Svelte | 13 KB |
| Python | 4.4 KB |
| Shell | 3.8 KB |

---

## 场景架构

三个场景模式，通过 Svelte 状态切换：

- **Intro** — 标题画面，星球旋转入场
- **Gameplay** — 主游戏场景（球面行走、NPC 交互、送信任务）
- **NPC** — NPC 对话特写模式

---

## 资产管线

项目通过浏览器 DevTools 从 `messenger.abeto.co` 提取生产环境资源，并提供配套工具链：

```
pnpm reference:discover   # 从 JS bundle 中发现资源 URL
pnpm reference:download   # 下载缺失的参考文件
pnpm reference:shaders    # 从 JS bundle 中提取 GLSL 着色器
```

### 资产分类

| 类别 | 格式 | 内容 |
|------|------|------|
| 音频 | OGG | 6 种环境氛围（base/beach/city/factory/forest/temple/waterfalls）、脚步声、跳跃、对话气泡、UI 音效、背景音乐 |
| 3D 几何体 | Draco (.drc) | 17 种 NPC（含骨骼+动画）、星球 LOD 分块（10 级）、投递物品、鸟类 |
| 纹理 | KTX2 (Basis) | 角色面部（眼/嘴）、植被、云噪声、水纹、LUT 色彩分级、粒子精灵 |
| 字体 | .font | REM-Medium、UglyDave、heading、planet |
| 着色器 | GLSL | 100+ 个从原始 App3D bundle 提取的着色器程序 |
| UI 图标 | .icon | 表情（10 种）、任务图标、NPC 图标、侧边按钮图标 |

---

## 核心技术要点

### 1. Draco 几何压缩

所有 3D 模型使用 Google Draco 压缩（`.drc`），通过 Web Worker (`dracoworker`) 异步解压。每个 NPC 包含：
- 主网格（`.drc`）
- 骨骼（`-bones.drc`）
- 待机动画（`-idle.drc`）
- 说话/行走动画变体（部分 NPC）

### 2. 纹理压缩

使用 KTX2 + Basis Universal 格式，通过 WASM 模块 `basis_transcoder` 在浏览器端解码，直接上传为 GPU 压缩纹理，节省 VRAM。

### 3. Web Worker 架构

重型任务全部卸载到 Worker：

| Worker | 大小 | 功能 |
|--------|------|------|
| collisionworker | 125 KB | 碰撞检测 |
| geometryworker | 54 KB | 几何处理 |
| charactergeoworker | 77 KB | 角色几何/动画 |
| glyphworker | 91 KB | 文字渲染（MSDF） |
| exrworker | 85 KB | HDR 图像处理 |
| msdfworker | 3.5 KB | 有符号距离场字体 |
| bitmapworker | 3.6 KB | 位图处理 |

### 4. 星球 LOD 系统

星球几何体分为 10 个 LOD 块（`full_0` ~ `full_9`），大小从 324KB 到 7KB 递减，实现视距相关的细节层次切换。

### 5. 着色器系统

从原版 JS bundle 中提取了 100+ 个 GLSL 程序，涵盖：
- 水面渲染（含瀑布 VFX）
- 植被（树叶 LOD 着色器）
- 天空/大气散射
- 角色材质
- 粒子效果
- 后处理

---

## 与「癫狂的世界」对比

| 维度 | messenger-copy | 癫狂的世界 |
|------|---------------|-----------|
| 框架 | SvelteKit | 纯 TypeScript + Vite |
| 资产 | 下载原版 Draco/KTX2 资产 | 全部程序化几何体 |
| 音频 | 原版 OGG 音频文件 | Web Audio API 合成 |
| NPC 系统 | 17 种带骨骼动画的 NPC | 无（后续迭代计划） |
| 任务系统 | 送信任务（原版逻辑） | 无（后续迭代计划） |
| 物理 | collisionworker（推测 Rapier） | 自定义球面重力 |
| 构建体积 | 极大（完整资产） | ~141KB gzip |
| 球面世界 | Draco 压缩的星球几何 | 程序化球体 + 建筑 |
| 动画 | 骨骼动画（角色 idle/talk/walk） | 静态建筑 |
| 着色器 | 100+ 专业 GLSL | 基础材质 |

### 可供借鉴的技术点

1. **Draco + KTX2 管线**：如果未来引入外部模型，可参考其 Worker 解压架构
2. **场景模式切换**：Intro → Gameplay → NPC 的状态机模式值得借鉴
3. **LOD 系统**：星球分块 LOD 是球面世界渲染的关键优化
4. **MSDF 字体渲染**：glyphworker 用于 UI 文字的 SDF 方案
5. **脚本工具链**：`reference:discover/download/shaders` 展示了自动化资产管线

---

> **总结**：messenger-copy 最大的价值在于展示了 Messenger 原版的**完整资产结构和技术架构**——它是一个优秀的"解剖标本"，揭示了商业级浏览器 3D 游戏的内部运作方式。对于「癫狂的世界」的开发，最有参考价值的是其场景管理、Worker 架构和 LOD 系统设计。
