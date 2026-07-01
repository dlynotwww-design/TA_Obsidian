目前游戏开发中，**UI（界面设计）** 和 **UX（交互设计）** 用的平台，与互联网产品有些相似，但更偏向游戏引擎和游戏工作流。

## 一、UI设计（视觉界面）

主要工具：

|工具|使用程度|用途|
|---|---|---|
|Figma|⭐⭐⭐⭐⭐|主流UI设计、组件库、设计规范|
|Adobe Photoshop|⭐⭐⭐⭐|UI贴图、美术绘制|
|Adobe Illustrator|⭐⭐⭐|Icon、矢量资源|
|Adobe After Effects|⭐⭐⭐|UI动画演示|
|Rive|⭐⭐⭐⭐|可交互UI动画|

目前绝大多数游戏公司（腾讯、米哈游、网易、Epic）都已经大量使用 **Figma** 做UI设计。

---

## 二、UX设计（交互设计）

UX更多不是画界面，而是：

- 新手引导
    
- HUD布局
    
- 操作反馈
    
- 菜单层级
    
- 战斗交互
    
- 手柄映射
    
- 输入体验
    
- 可访问性（Accessibility）
    

常用工具：

|工具|用途|
|---|---|
|Figma|流程图、原型|
|FigJam|玩家流程、脑图|
|Miro|用户旅程(User Journey)|
|Whimsical|Flow Chart|
|Axure RP|少量大型项目仍使用|

---

## 三、真正落地是在游戏引擎

设计完成后，并不会直接发布，而是在引擎中实现。

### Unreal Engine

使用：

- Unreal Engine UMG
    
- Widget Blueprint
    
- Common UI
    
- Slate（编辑器UI）
    
- Motion Design（UE5.4+）
    

流程：

```
Figma
    ↓
切图/Icon
    ↓
导入UE
    ↓
UMG搭UI
    ↓
蓝图/C++
    ↓
动画
    ↓
数据绑定
```

---

### Unity

使用：

- Unity UI Toolkit
    
- uGUI
    
- UI Builder
    

流程几乎一样。

---

## 四、大型游戏公司的流程

例如米哈游、腾讯、Epic通常是：

```
UX设计师
    │
    ├──玩法流程
    ├──交互说明
    ├──原型
    ▼
UI设计师
    │
    ├──视觉稿
    ├──Icon
    ├──组件
    ▼
TA/UI程序
    │
    ├──切图
    ├──导入引擎
    ├──制作Widget
    ├──动画
    ▼
策划
    │
    ├──配置
    ▼
程序
    │
    ├──数据接口
    ▼
QA
```

很多公司还会有专门的 **UI Technical Artist（UI TA）**，负责将设计稿高质量地还原到引擎中，并优化性能和适配。

---

## 五、现在越来越流行的平台

AI 已开始进入游戏 UI/UX 工作流，常见组合包括：

|环节|平台|
|---|---|
|UI设计|Figma|
|AI生成界面|Galileo AI、Uizard|
|图标生成|Adobe Firefly|
|UI动画|Rive|
|引擎实现|Unreal Engine / Unity|
|AI辅助开发|Claude Code、Cursor|

---

### 如果你的目标是进入 UE 游戏开发

结合你之前关注的 **UE、Houdini、TA 和 AI 辅助开发**，建议优先掌握这套组合：

- **设计与原型**：Figma（组件、Auto Layout、变量、Design System）
    
- **交互与动画**：Rive（适合菜单、HUD、按钮等动态效果）
    
- **引擎实现**：Unreal Engine UMG + Common UI + Motion Design
    
- **自动化与工具开发**：Python + Editor Utility Widget + Claude Code/Cursor 辅助开发
    
- **资源制作**：Photoshop 或 Illustrator（UI 素材）、After Effects（复杂演示动画）
    

这也是目前许多 UE5 项目（尤其是中大型项目）较为主流的 UI/UX 技术栈。