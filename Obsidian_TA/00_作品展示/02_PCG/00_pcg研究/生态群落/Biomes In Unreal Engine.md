---
source: https://www.youtube.com/watch?v=gGhcohcq5WY&t=396s
tags:
  - Houdini
  - PCG
  - 生态群落
  - NotebookLM
---
> 📁 [UE工程](file:///D:/TA/houdini/biome_demo_unreal)
## NOTE

### labs生态群落案例

---


这段视频由 Side Effects Labs 的 Bailey 演示，详细介绍了一套**将 Houdini Biome 工具组生成的Terrain（地形）和植物实例（Plant Instances）通过 Houdini Engine 导入 Unreal Engine (UE)** 的完整工作流程。

## Biomes In Unreal Engine

### 1. 项目准备与环境搭建

- **示例文件获取**：演示项目可从 GitHub 的 **Side Effects Labs Examples** 仓库下载，具体位于 `projects/dryad_beta/biome_demo_unreal` 目录下。
- **软件安装**：需要安装最新的 **Houdini 每日构建版本** 以及配套的 **Houdini Engine for Unreal 插件**。
- **UE 项目配置**：
    - 创建一个 UE 第三人称模版项目，将下载的 `biomes` 文件夹（包含 HDA、材质、网格和贴图）复制到项目的 `Content` 目录下。
    - 将 Houdini Engine 插件文件夹复制到项目根目录下的 `Plugins/Runtime` 文件夹中，以确保项目运行特定版本的插件。
    - 在 UE 中启动 Houdini Engine 会话，将 HDA 拖入场景即可看到初步生成的地形和植被。

### 2. HDA 参数与交互控制

在 UE 中，HDA 提供了多个关键参数来控制生成结果：

- **路径关联**：包括 **Meshes folder path**（指向 UE 植物模型文件夹）、**Landscape material path**（地形材质路径）和 **Plant material path**（植物材质路径）。
- **随机化与优化**：**Shuffle biome seed** 能够随机化生物群落的分布；**Water toggle** 按钮可开关水域生成以加快计算速度。
- **纹理渲染**：通过 **Render textures** 按钮，可以触发 Houdini 内部的 **Copernicus (COPs)** 网络，将渲染出的 Base Color 和 Roughness 贴图直接导出到本地。

### 3. Houdini 内部逻辑：地形与群落定义

- **群落划分**：首先在平坦的 **Heightfield（高度场）** 上定义不同的群落区域，这些区域作为图层驱动后续生成。
- **程序化地貌建模 (Terraformation)**：
    - **沙漠**：生成梯田地貌（Terrace）。
    - **萨瓦纳**：生成平顶山（Mesas）。
    - **温带森林**：生成起伏的丘陵。
    - **北方森林与苔原**：生成雄伟的山脉。
- **纹理生成 (COPs)**：利用 **Geometry to Layer** 节点将高度场图层转换为图像层，在 Copernicus 中根据地形特征生成材质贴图。

### 4. 植被系统与分布规则

视频重点介绍了 **Labs Biome Toolset** 的使用：

- **属性演化 (Biome Attributes Evolve)**：地形属性会根据几何形状动态调整。例如，**温度随海拔升高而降低**；山脉会产生**雨影区 (Rain shadow)** 导致背风坡干燥；**陡坡会移除土壤**；此外还利用噪声模拟土壤质量的差异。
- **植物定义 (Plant Define)**：
    - **生境偏好**：为每种植物设置对温度和降水量的忍受范围。
    - **物理规则**：定义 **Crown radius（树冠半径）** 防止树木重叠，定义 **Trunk radius（树干半径）** 允许灌木在树下生长（只要不碰到树干）。
    - **模型变体与 Age（年龄）**：植物被分配一个 0 到 1 的归一化 Age 属性。根据该数值，系统会自动分配不同的模型（如 0-0.33 为幼苗，0.66-1 为大树）。
    - **UE 资产映射**：通过 `unreal_instance` 属性直接指向 UE 内部的资产路径，实现精准的模型替换。

### 5. 数据传递与 Unreal 材质驱动

为了实现丰富的视觉变化，HDA 将关键属性传递给 UE：

- **地形层混合**：高度场图层在 UE 中被识别为 **Landscape Layers**。材质通过 `Landscape Layer Blend` 节点将这些图层（如沙漠、森林、雪地）与不同的颜色或纹理进行混合。
- **每实例自定义数据 (Per Instance Custom Data)**：
    - HDA 将植物的 **Age（年龄）**、**Noise（空间噪声）** 和 **Unique ID（唯一 ID）** 分别存储在自定义数据索引 0、1、2 中。
    - **Age 驱动**：在 UE 材质中读取索引 0，使幼苗颜色更冷/更鲜嫩，老树颜色更深。
    - **Unique ID 驱动**：利用随机浮点数节点读取索引 2，为每个实例提供独立的明度（Value）变化。
    - **Noise 驱动**：读取索引 1，模拟类似云影覆盖的全局颜色偏移。
- **性能优化**：所有的材质颜色变化都在**顶点级别（Per-vertex）**进行，并使用 `Vertex Interpolator` 节点进行优化。
- **碰撞控制**：通过 `unreal_uproperty_collision_profile_name` 属性，设置树木为“Block All”（阻挡玩家），灌木为“No Collision”（允许玩家穿过）。

通过这套流程，用户可以在 Houdini 中控制复杂的生态逻辑，并在 Unreal 中获得高性能、高细节且具有高度随机性的自然环境。
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