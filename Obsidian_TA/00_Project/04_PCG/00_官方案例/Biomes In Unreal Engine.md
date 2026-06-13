---
source: https://www.youtube.com/watch?v=gGhcohcq5WY&t=396s
tags:
  - Houdini
  - PCG
  - 生态群落
  - NotebookLM
---
> 📁 [UE工程](file:///D:/TA/houdini/biome_demo_unreal_7)

这段视频由 Side Effects Labs 的 Bailey 演示，详细介绍了一套**将 Houdini Biome 工具组生成的Terrain（地形）和植物实例（Plant Instances）通过 Houdini Engine 导入 Unreal Engine (UE)** 的完整工作流程。

## 以下是视频内容的详细拆解：

### 1. 项目准备与环境搭建

- **示例文件获取**：用户可以从 GitHub 的 "Side Effects Labs Examples" 仓库下载演示项目，路径位于 `projects/dryad_beta/biome_demo_unreal`。
- **软件安装**：需要安装最新的 Houdini 每日构建版本以及 **Houdini Engine for Unreal 插件**。
- **UE 项目配置**：在 Unreal 中创建一个第三人称项目，将 HDA、材质、网格和贴图文件夹复制到 `Content` 目录下，并将插件放入项目的 `Plugins/Runtime` 文件夹中。

### 2. HDA 的参数与实时交互

在 UE 中将 HDA 拖入场景并连接 Session 后，可以通过 HDA 的参数进行控制：

- **路径关联**：设置网格文件夹、景观材质和植物材质的路径，确保 HDA 能正确引用 UE 中的资产。
- **地形控制**：通过 `Shuffle biome seed` 可以**随机化生物群落（Biomes）的分布**。此外还包含水域开关、纹理渲染按钮等参数。
- **实时反馈**：HDA 会在 UE 中生成带有材质的地形以及具有碰撞属性的植物实例（如树木设置为阻挡，灌木设置为无碰撞以便玩家穿过）。

### 3. Houdini 内部节点网络（地形生成）

- **生物群落定义**：在 Houdini 中，首先在平面 Heightfield 上定义生物群落区域，这些区域作为 Heightfield Layer 驱动后续所有生成步骤。
- **地形建模**：根据区域生成特定的地貌，例如**沙漠的梯田、草原的平顶山、温带森林的起伏丘陵以及北方森林的山脉**。
- **Copernicus (COPs) 纹理生成**：利用 Houdini 的 Copernicus 网络，根据地形形状生成 Base Color 和 Roughness 贴图，并通过 `ROP image outputs` 直接渲染导出。

### 4. 植被散布系统 (Biome Toolset)

- **Biome Configure Multibiomes**：这是核心工具，它将植物散布与地形的属性（如温度、降水量）结合起来。
- **地形属性演化**：工具会根据地形高度降低温度，或根据山脉形成的雨影区创建干燥区域，甚至根据坡度移除土壤。
- **植物定义 (Plant Define)**：
    - 用户可以为不同物种定义**生境偏好**（温度、降水）以及**生长规则**（如树木之间不能重叠，但灌木可以在树下生长）。
    - 支持为同一物种设置不同的模型变体（如幼苗、中型树、大型树），并根据 **Age（年龄）属性**自动分配模型。
    - 通过 `Unreal Engine asset path` 属性，可以直接在 Houdini 中指定 UE 项目内的资产路径，实现精准实例替换。

### 5. Unreal 专用属性与材质驱动

为了让 UE 正确识别数据，HDA 在输出前添加了特殊的 Unreal 属性：

- **景观属性**：通过 `unreal_uproperty_collision_profile_name` 设置碰撞，并将 Heightfield 图层映射为 UE 景观材质的 **Target Layer（目标层）**。
- **Per Instance Custom Data（每实例自定义数据）**：
    - HDA 将植物的 **Age（年龄）、Noise（噪声）和 Unique ID（唯一标识符）** 存储在 `unreal_per_instance_custom_data` 中。
    - 在 UE 材质中，利用 `PerInstanceCustomData` 节点读取这些值，从而实现**植物颜色的随机偏移（Hue Shift）**、模拟云层覆盖的阴影效果，以及根据年龄改变色调。
- **地形材质方案**：视频展示了两种方案：一种是基于景观层混合的简单材质，另一种是使用 Copernicus 渲染出的全局贴图的高细节材质。

通过这一流程，开发者可以利用 Houdini 的程序化力量生成复杂的生物群落，并无缝地在 Unreal Engine 中实现具有丰富视觉变化和正确物理属性的环境。


---

## 如何设计一个生态群落系统
设计一个完整的生态群落系统（Biome System）是一个程序化生成的过程，需要将地形地貌、气候属性与植物分布规则有机结合。根据视频源码，该系统的设计可以分为以下核心阶段：

### 1. 基础地形与群落区域定义

系统设计的起点是在 Houdini 中通过 **Heightfield（高度场）** 定义不同的群落区域。

- **区域划分**：首先在平坦的高度场上定义生物群落区域，这些区域作为高度场图层（Layers）驱动后续的所有生成步骤。
- **程序化建模（Terraformation）**：根据不同群落的特性进行地形塑造。例如，为沙漠生成梯田地貌（Terrace），为萨瓦纳生成平顶山（Mesas），为温带森林生成起伏丘陵，并为北方森林生成山脉。
- **属性混合与水域**：将不同地貌进行混合，并根据地形自然积水的逻辑在低洼处添加水域。

### 2. 生态属性系统的构建

生态群落的核心在于模拟环境对植物生长的影响。

- **关键属性**：通过 `biome define` 节点定义每个群落的**温度（Temperature）**和**降水量（Precipitation）**。
- **属性演化（Evolve）**：环境属性应随地形动态变化。例如，温度随海拔升高而降低；山脉会形成“雨影区”导致背风坡干燥；陡峭的悬崖会移除土壤属性；利用噪声模拟土壤质量的差异。

### 3. 植物物种的程序化定义

在系统中，每种植物不仅是模型，更是一组生长规则的集合。

- **生境偏好**：利用 `plant define` 节点设置物种对温度、降水和土壤的忍受度与偏好程度。
- **生长规则与间距**：
    - 定义植物的**树冠半径（Crown radius）**以避免树木重叠。
    - 定义**树干半径（Trunk radius）**，允许灌木（Shrubs）生长在树冠下，只要不碰到树干。
- **年龄阶段与变体**：设置归一化的 **Age（年龄）** 属性。系统根据年龄区间自动分配不同的网格模型（如 0-0.33 为幼苗，0.66-1.0 为大树）。

### 4. 植被散布与匹配机制

利用 `biome plant scatter` 节点进行“相亲式”匹配：

- **自动化散布**：系统会将植物的偏好与地形当前的生态属性（温度、降水）进行对比，只在最适合的地方生成植物点云。
- **群落限制**：可以强制将某些物种限制在特定群落内，防止在模糊的地带出现不合理的混交。

### 5. Unreal Engine 的集成与视觉驱动

为了在引擎中实现最终效果，需要通过 **Houdini Engine** 传递关键属性：

- **实例替换**：使用 `unreal_instance` 属性指向 UE 项目中的资产路径，实现精准的模型替换。
- **材质变体驱动**：通过 `unreal_per_instance_custom_data` 传递 **Age**、**Noise** 和 **Unique ID** 到 UE 材质中。
    - **Age** 驱动色调变化，反映生长阶段。
    - **Noise** 驱动全局噪声，模拟云影或群体色差。
    - **Unique ID** 作为非归一化的随机种子，为每个实例增加独特的细节差异。
- **碰撞控制**：通过 `unreal_uproperty_collision_profile_name` 设置碰撞属性，例如让玩家可以穿过灌木但会被大树阻挡。

通过这种设计，系统不仅能生成视觉丰富的景观，还能确保植被分布符合逻辑规律，且在 Unreal Engine 中具备高度的可控性和实时性能。