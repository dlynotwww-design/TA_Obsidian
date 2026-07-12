---
title: "The Matrix Awakens: Generating a World | Tech Talk | State of Unreal 2022"
source: https://www.youtube.com/watch?v=usJrcwN6T4I
tags:
  - PCG
  - unreal-engine
  - houdini
  - city-generation
  - wave-function-collapse
created: 2026-07-11
---

# The Matrix Awakens: Generating a World | Tech Talk | State of Unreal 2022

> **演讲者：** Quentin Marmier、Robert Osborne、Julien Marchand (Epic Games) / Mai Ao (SideFX)
> **时长：** 59:59
> **关键词：** 程序化城市生成、Houdini、MassAI、Nanite、波函数坍缩、ZoneGraph

---

## 一、项目概览

### 1.1 城市规模

| 指标 | 数据 |
|------|------|
| 城市宽度 | 4-5 km |
| 街道总长 | 260 km |
| 人行道（带设施） | 512 km |
| 独特建筑 | 7,000+ |
| 行驶车辆 | 18,000 |
| 行人 | 35,000 |
| Nanite 实例 | 800 万 |

> **00:53** 这是一座栩栩如生的独立城市，宽度约4-5千米，街道全长260千米，设施齐全的人行道长512千米，还有7千多幢迥然不同的建筑和1万8千多辆载具，以及3万5千名彼此感知、遵守交规的行人。
> This is a living autonomous city, 4 by 5 kilometers wide, with 260 kilometers of streets and 512 kilometers of furnished sidewalks, more than 7,000 unique buildings, 18,000 traffic vehicles, and 35,000 pedestrians aware of each other and respecting traffic rules.

### 1.2 核心目标

- 充分利用 UE5 的 **Nanite**、**Lumen** 和 **开放世界** 功能
- 创建一个完全程序化的城市生成器
- 利用少量简单输入（基础样条）即可在运行时生成美式城市
- 城市被反复再生了 **53 次**，不断优化程序化规则

> **01:43** 我们希望充分利用虚幻引擎5的Nanite、Lumen和开放世界功能，尽可能为大家提供最详细的虚拟体验。
> We've tried to use the full potential of Nanite Lumen Open World with Unreal Engine 5 to offer the most detailed virtual experience we could.

---

## 二、Houdini 与 SideFX

> **演讲者：Mai Ao (SideFX Labs 首席技术美术师)**

### 2.1 Houdini 核心理念

- Houdini 是一款高端、全面的 **程序化节点架构** 3D 解决方案平台，有 25 年发展史
- **管线 = 工厂，节点 = 机器**：节点连接形成复杂网络，如同工业流水线
- 管线可精简为 **HDA (Houdini Digital Asset)**，暴露控制项，其余全自动
- 核心目的：**为美术师服务**，提供创造性控制，减少返工

> **02:53** 如何设计这些流水线完全由你决定。管线可以进一步精简并纳入工厂管理，又叫 HDA。你只需关心暴露的控制选项，其余都是完全自动的。
> The designs of these assembly lines are entirely up to you. Finally, the pipelines can be streamlined and organized into factories, aka, HDAs. All the controls you care about are exposed, and the rest is fully automated.

### 2.2 Houdini Engine 插件

- HDA 通过 **Houdini Engine 插件** 在虚幻引擎编辑器中使用
- Houdini Engine 现已免费向虚幻引擎提供商业许可
- 小型开发团队（2人）维护的工具可供大型团队直接使用

### 2.3 SideFX Labs

- 提供 200+ 免费开源 Houdini 工具
- 涵盖建模、摄影测量、UV、纹理生成、资产导出、第三方集成等
- 可视为团队研发的外部延伸

---

## 三、城市生成管线

> **演讲者：Quentin Marmier (Epic Games 特殊项目团队首席技术美术师)**

### 3.1 设计决策

#### 为什么不使用 OpenStreetMap？
- 数据不规则，地区大小和形状独一无二
- 转化和调整工作量大，会产生过多特殊资产
- 创建巨型城市网格体的方案在目标细节程度下不可行

#### 替代方案：量化世界
- 创建自己的建筑模块来构建世界
- 尽可能依赖 **实例化 (Instancing)**
- 完全控制城市几何体，严格控制任意程度

> **07:17** 我们要做的是量化世界，创造自己的建筑模块来构建世界，然后尽可能依赖实例化。
> What we need to do is quantify the world and make our own construction set to build it. We would then relay as much as possible on instancing.

### 3.2 Nanite 带来的新挑战

- Nanite 消除了多边形限制：1 m² 最多可容纳 **100 万个三角形**
- 16 km² 城市可能拥有 **16 万亿三角形**
- **新瓶颈：磁盘上的资产大小和数量** → 需要巧妙切割世界

> **06:31** 现在1平方米最多可以有100万个三角形，而且不需要担心性能。一个16平方千米的城市可能有16万亿三角形。但是这也带来了新的问题：磁盘上的资产大小和数量成为了一个限制因素。
> Now 1 meter squared can have up to a million triangles without worrying about performances. A city of 16 kilometer squared would have 16 trillion triangles. This brings a new problem: the size and the amount of assets on disk becomes a limiting factor.

### 3.3 城市布局工具 (City Layout Tool)

**输入：**
- 基础形状
- 主干线（样条）

**输出：**
- 美式城市布局
- 道路网络、地块定义、人行道网络
- 道路连通性、交通密度、行人密度等元数据

> **07:57** 你只需要输入两种数据：基础形状和道路或者说主干线。通过修改个别属性和选项，调整道路网络设置，你就获得一个美式城市布局。剩下的就由工具来计算。
> You would only require two main inputs to start — a basic shape and the path or the main arteries. With few attributes and option available to adjust the road network setup, it would give you an American city layout. The rest is figured out by the tool.

**技术细节：**
- 使用 Houdini **最短路径节点** 构建干线
- 工具计算最合适的网格模式匹配用户输入

### 3.4 城市分区 (City Zoning)

- 定义区域属性（商业区、居民区等）
- 本质上是城市的 **垂直建模工具**
- 使用 Houdini Engine 插件直接在引擎中设计
- 与美术总监、过场动画部门反复迭代

### 3.5 依赖关系图：三阶段流水线

```
城市基础 (City Base)  →  城市核心 (City Core)  →  场景布置 (Set Dressing)
```

这决定了在特定阶段改变规则时需要在何处重新生成城市。

### 3.6 道路处理 (Road Processing)

**道路层级：** 三级道路层级（20m / 10m / 5m 模块）

**处理流程：**
1. 根据道路连接角度精确切割每个路段
2. 为交叉路口留出空间
3. 用 9 种基础砖块填充道路几何体
4. 替换为高分辨率对应模块
5. 输出点云用于在虚幻引擎中实例化

**道路模块特征：**
- 两组 UV
- 储存为顶点颜色的相对顶点位置
- 边缘楔形设计（平滑连接）
- 一定弯曲度（增加逼真感）

> **11:22** 道路处理器会输出一个点云，用于实例化虚幻引擎中的模块，使用道路处理器样条。
> The road processor would then output a point cloud that would be used to instance the module inside Unreal using our road processor pipeline.

### 3.7 交通信息提取

- 使用道路元数据追踪每条车道的样条
- 连接形成基础交通网格
- 通过点云导入虚幻引擎 → 转换为 **ZoneGraph（区域图）**

### 3.8 高速公路生成 (Freeway Generation)

**特点：**
- 追逐场景的核心场地
- 有机的、触手状外观
- 2 个闭环 + 1 个悬垂通道 + 55 个入口匝道
- 可用高速公路总长 **25 km**

**技术方案：**
- 路面程序化生成为大型网格体 (Mega Mesh)
- 之后分为 100m 的小型网格块（适配开放世界流送 + Lumen）
- 路障、柱子、标牌、杂物等为 Nanite 实例

> **13:43** 鉴于高速公路的有机性，路面必须程序化生成为一个大型网格体。这个例子表明在创建城市的过程中我们不能完全依赖模块实例化。
> Because of its organic nature, the deck had to be procedurally generated as a mega mesh. This is one case in the city where we couldn't entirely rely on modular instancing.

### 3.9 地块与建筑体积 (Lots & Building Volumes)

**地块处理流程：**
1. 移除高速公路占地区域
2. 多层几何体清理和过滤
3. 算法细分（权衡建筑高度 vs 可用表面）
4. 低层建筑自动划分为纽约风格交错式地块

### 3.10 建筑 DNA 系统 (Building DNA)

每幢建筑用自定义 DNA 描述，包含：

| DNA 属性 | 说明 |
|----------|------|
| 足迹 (Footprint) | 17 种预定义形状 |
| XY 轴尺寸 | 大小 |
| 位置和空间方向 | 定位 |
| 延伸高度 | 分为三层 |
| 造型选项 | 方顶 (Cubified) 或交错式 (Staggered) |
| 建筑风格 | 特定风格分配 |

> **15:35** 城市中的每幢建筑都会用自定义 DNA 来描述。DNA 首先包含足迹。我们创建了17种形状，城市中的每幢建筑都以其中一种形状为基础。这样我们就知道最终会得到什么。
> Each building of the city would be described by a custom DNA. The DNA starts with a footprint. We have created 17 of those, and any building in the city would have one of these shapes as a base. So we would always know what to expect.

### 3.11 地面与人行道 (Ground & Sidewalks)

**人行道：**
- 利用城市布局工具提供的人行道样条网络
- 自适应散布模块
- 分别处理外角和内角（内角使用非均匀缩放）

**地面：**
- 减去建筑覆盖面积
- 预替换 Megascan 地面 + 位移贴图
- 每块地砖多达 **50 万三角形**
- 地砖被重复利用 **250 万次**
- 仅地面就有 **1.25 万亿三角形**

> **19:09** 没错，仅地面就有1.25万亿个三角形。我们希望所有物体看上去都很真实。
> Yeah, that is 1.25 trillion triangles for the ground itself. We wanted things to look sharp and good.

### 3.12 场景布置 (Set Dressing)

**三种剩余区域类型：**
- 商场类型 (Plaza)
- 高速公路类型 (Freeway)
- 停车场类型 (Parking)

**生态群落 (Biomes)：** 预先组装好的资产包，使用实例打包蓝图工作流。

**填料散布器 (Packing Scatterer)：**
- 测量每块区域的最长边作为方向参照
- 以最佳方式组合生物群落
- 确保实例不会相互重叠
- 广泛应用于整个城市图（包括建筑屋顶）

> **20:55** 我们可以从这个有趣的示例中看到填料散布器将如何以有序的方式覆盖各类区域，并且不需要担心实例会相互重叠。
> This shows you a fun example of what the packing scatterer can do to cover any type of area with organized pattern, without any fear of overlapping instances.

### 3.13 道路贴花 (Road Decals)

- 实例化平面 + 贴花材质
- 大型图块（人行横道、轮胎印记）使用 Mega Mesh 方案——投射到道路几何体上匹配拓扑结构
- 复杂交叉路口：程序化分析车道系统，创建逼真标志和道路绘制

### 3.14 音频数据

- 在最终城市表面覆盖 **3m 密度点云**
- 储存元数据：混响量、音效类型等
- 利用城市代理几何体的环境遮蔽

### 3.15 关键统计

| 指标 | 数据 |
|------|------|
| Houdini 图表生成时间 | 约 25 分钟 |
| 城市再生次数 | 53 次 |
| 最终版本导入+处理 | 数小时内完成 |
| 理论上每日可创建新城市版本 | 多次 |

> **24:16** 在项目的制作过程中，这个城市被反复生成了53次。每一次生成，我们都会雕刻城市，探索值得改进的程序规则，修复漏洞，添加细节，最后再重新生成城市。
> Over the course of the project, we have regenerated the city 53 times. For every generation, we would sculpt the city and look for what we can improve in the procedural rules, fix bugs, add details to it, and finally regenerate the city.

---

## 四、程序化建筑生成

> **演讲者：Robert Osborne (Epic Games 高级技术美术师)**

### 4.1 原型开发

- 使用 Houdini + Houdini Engine 进行快速迭代
- **建筑模块模板生成器**：按需快速创建特定大小的建筑模块代理
- 需要 **建筑形状语法系统** 使建筑生成尽可能随机化

> **25:23** 如果想评估概念，那么迭代速度就非常重要。我们做了大量的原型开发工作和迭代工作。
> Iteration speed is king when you want to evaluate concepts. We did a lot of prototyping and iterating.

### 4.2 建筑定义文件 (BDF)

- 使用 JSON 格式保存建筑定义
- 生产阶段实现自动化 BDF 管线
- 人类可读数据，可快速编辑验证和调试
- 输入：带 BDF 标签的建筑体积

### 4.3 形状语法 (Shape Grammar)

**语法符号说明：**

| 符号 | 含义 |
|------|------|
| `\|` | 模块桶，定义模块放置行为 |
| 字母 (A-Z) | 字典键，查找模块元数据（宽度、高度） |
| `( )` | 无限可重复宏模式 |
| `[ ]` | 固定重复宏模式 |
| `*` | 桶中所有模块可缩放匹配建筑立面长度 |

**选择逻辑：**
- 完整迭代一次的总长度最接近建筑立面长度
- 衔接缝隙最小，且不超过或等于建筑立面长度

> **28:50** 选择衔接缝隙最小且不超过或等于建筑立面长度的形状语法。
> The shape grammar with the smallest fit gap not greater or equal to the facade length is selected.

### 4.4 模块遮挡剔除

- 相连建筑墙体上的被遮挡模块需要移除
- 使用布尔包壳 (Boolean Shell) 代表接触墙高度
- 每个模块的额外采样点用于相交测试
- 保守处理，实现了约 **25% 的模块/道具/贴花减少**

> **30:21** 即使是这样的保守处理，也能减少25%的建筑模块、道具、贴花。
> Even with this conservatism a 25% reduction in building modules, props, and decals is achieved.

### 4.5 窗户系统

**窗户立方体贴图 (Window Cubemap)：**
- 在每个模块立面构建连接性数组
- 确定可放置房间的最大尺寸
- 按楼层 ID → 房间 ID → 房间大小逐级点亮灯光

**窗户处理 (Window Treatments)：**
- 1 层模块添加窗户辅助对象
- 定义窗户表面数据

**窗户标记 (Window Signage)：**
- 利用建筑入口位置，在最近窗户放置标记
- 复合布局（霓虹灯招牌等）替代普通窗户结霜实例

### 4.6 屋顶生成

- 所有屋顶几何体来自输入建筑体积
- UV 生成和缩放控制（处理无法实例化的独特屋顶）
- 分割式屋顶支持（处理复杂方形体积）
- 推拉插入物函数隐藏间隙

### 4.7 扩展性与优化

**生成规模：**
- 近 7,000 幢建筑（含道具、遮挡、窗户处理、立方体贴图、贴花、屋顶几何体）
- 在单台 X3990 Threadripper PC 上用 PDG **30 分钟**内完成

**体积管理器 (Volume Curator)：**
- 项目后期精细调整
- 降低特定高度范围的城市景观高度（避免蝴蝶效应）
- 锁定有问题的特定建筑体积
- 支持多重 BDF 体积，隐藏建筑风格过渡

### 4.8 BugItGo 工作流

- 使用 UE 编辑器命令行 `BugIt` 截取兴趣点 (POI)
- BugItGo 字符串可粘贴到 Houdini 中生成指示符
- **往返传输**：Houdini → 剪贴板 → UE 编辑器
- 用于快速定位边缘案例、逐步调试、烟雾测试

> **37:17** 粘贴一个BugItGo字符串到BugIt代码HDA就可以让它在Houdini世界场景中生成一个指示符。你可以往返传输这个数据，将来源于当前有效的Houdini 3D场景视图的BugItGo位置传回到剪切板。
> Pasting a BugItGo string into the BugIt code HDA will generate an indicator in Houdini world space. You can round-trip this data, passing a BugItGo location derived from the currently active Houdini 3D Scene view back to the clipboard.

**体积过滤器 HDA：**
- 按目标体积集合输入建筑生成器
- 无需加载整座城市即可进行烟雾测试
- 大幅提高迭代速度

---

## 五、波函数坍缩 (Wave Function Collapse)

> **演讲者：Robert Osborne**

### 5.1 基本原理

- 源自量子力学概念：波函数从叠加态坍缩为本征态
- 在游戏开发中应用为 **约束满足算法**
- 应用：纹理合成、模型合成、地图生成、游戏玩法

### 5.2 算法流程

```
初始化 → 观察（选择最小熵图块，随机选择选项）→ 传播（递归调整相邻图块域）→ 重复直到全部坍缩
```

**关键概念：**
- **约束 (Constraint)**：键选项 + 邻接方向 + 邻接选项
- **空白选项 (Empty)**：确保网格边界不会形成开放式求解
- **熵 (Entropy)**：图块剩余选项数量

### 5.3 Epic 的实现特点

- 从任意布局中 **直观地创建** WFC 模型（而非基于标签）
- 使用网格 Actor 蓝图直观显示边界框
- 可根据网格中的静态网格体 Actor 获取起始选项
- **美术方向 + 程序主义** 的结合

### 5.4 城市屋顶应用

| 指标 | 数据 |
|------|------|
| 独特屋顶结构 | 2,600+ |
| WFC 模型约束数 | 5,000+ |
| 可平铺网格体 | 仅 33 个 |

- 从点云数据获取网格进行求解
- 编辑器工具控件进行求解后处理
- 利用相邻规则放置墙上道具
- 屋顶道具在 Houdini 中散布，通过点云在 UE 中重新组装

> **43:15** 波函数坍缩模型保存的约束条件有5000多个，总共只有33个可平铺网格体。
> The wave function collapse model contained just over 5,000 constraints, all of this with only 33 tileable meshes.

> **44:31** 波函数坍缩插件由特殊项目团队的高级技术美术师 Joji Tsuruga 制作，之后会以试验性插件的形式在虚幻引擎5中提供。
> The wave function collapse plug-in was created by Joji Tsuruga, senior technical artist on the special project team. It will be available as an experimental plug-in in Unreal Engine 5.

---

## 六、为城市赋予生命力：人群与交通系统

> **演讲者：Julien Marchand (Epic Games 工程总监)**

### 6.1 Mass Framework 概述

**三个插件层级：**

```
MassEntity (数据导向基础框架)
    ↓
MassGameplay (将实体带入游戏世界)
    ↓
MassAI (导航、动画、行为)
```

#### MassEntity 核心设计

| 传统 Actor-Component 模型 | Mass Framework |
|---------------------------|----------------|
| 代码和数据不连贯（顺序更新） | **片段 (Fragment)**：小型数据结构 |
| 组件在内存中不保证连续 | 类似构成的实体片段**连续储存** |
| 访问导致高速缓存缺失 | 减少缓存缺失，简化并发执行 |
| 组件可能臃肿 | 实体不含指向不需要数据的指针 |

**关键组件：**
- **实体查询 (Entity Query)**：过滤需要执行逻辑的实体
- **处理器 (Processor)**：批量更新发生的地方

> **47:58** 这种分离能够增强数据和代码的一致性，减少高速缓存缺失，简化未来的并发执行。这是限制可以一次性模拟的实体数量的基础。
> This segregation is what enforces data and code coherency, minimize cache misses, and will trivialize concurrent execution in the future. These are the fundamentals that are pushing the limits on the numbers of entities we can simulate at once.

#### Mass Spawner

- 放置在关卡中的常规 Actor
- 两个核心问题：**生成什么？在哪里生成？**

### 6.2 ZoneGraph（区域图）

- 轻量级设计驱动型 AI 工作流
- **替代传统 AI 导航网格体**
- 逐点廊道结构 + 交叉点连接的生态系统
- 存储可操作标签（静态：行人/交通道识别；动态：开放/封闭车道）

### 6.3 人群系统 (Crowd System)

**数据驱动：**
- 合并行人密度程序数据 + 人行道网络 → 互联的区域图
- 包含人行横道、人行道、十字路口道的注释
- 基于密度的分布

**状态树 (StateTree)：**
- 可扩展的通用型状态机，决策树结构呈现
- 行人状态：漫步、闲逛、奔跑等
- 自上而下评估入口条件，运行参数化任务
- 与 Mass Framework 内存高效融合

**动画特性：**
- 多种走路风格和速度
- 平滑开始和停止动画
- 头部朝向 + 上半身方向（独立于速度）
- 对玩家和其他行人做出反应
- 新的**基于力的避让机制**（处理动态和静态障碍）
- 身体碰撞响应（播放一次性动画后恢复行为）

**LOD 系统：**

| LOD 级别 | 数量上限 | 描述 |
|----------|---------|------|
| 高 (LOD0) | 10 | 完整 MetaHuman Actor，带面部动画 |
| 中 (LOD1) | 20 | 完整 MetaHuman Actor，减少面部动画 |
| 低 (LOD2) | 500 | 轻量级顶点动画网格体 |
| 不可见 | 其余 | 不渲染 |

**持久性：** 无论 LOD 如何切换，始终保持当前行为，走远了再回来还能找到同一个角色。

### 6.4 交通系统 (Traffic System)

**数据驱动：**
- 合并交通密度程序数据 + 交通道网络
- 城市车道 + 高速公路车道 → 互联网络

**核心行为（Mass Processor 编程实现）：**
- 沿车道陆续前进
- 十字路口等待
- 沿车道排列（队列机制）
- 根据前车距离调整车速
- 障碍物响应（玩家、车祸场景）

**车道变更与合并：**
- 检测邻近空车道 → 创建幽灵实体 → 变道完成后移除原车道参考
- 特别适用于进出高速公路

**LOD 系统：**

| LOD 级别 | 数量上限 | 描述 |
|----------|---------|------|
| 高 (LOD0) | 10 | 完整物理车辆 Actor，可形变、销毁、交互 |
| 中 (LOD1) | 150 | 运行物理效果，简化悬架，Mass Framework 内模拟 |
| 低 (LOD2) | 5,000 | 实例化静态网格体，简单曲线和位置更新 |
| 不可见 | 其余 | 不渲染 |

**停放的车辆：**
- 通过点云在每个位置直接生成
- 每辆都可以供玩家乘坐、驾驶、丢弃、重新驾驶

> **57:58** 注意，停着的车辆不光是为了好看。每一辆都可以供玩家乘坐、驾驶、丢弃，之后还可以重新驾驶。
> Note that the parked vehicles are not just there to be pretty. The player can hop in any one of them, drive around, abandon them, and get back to them later on.

### 6.5 交叉口协调器 (Intersection Coordinator)

- 管理车道开放/关闭时机
- 控制行人通行、车辆转弯
- 大量交叉口配置增加了复杂性
- 管理人流和车流密度（防止市中心人口逐渐变少）

> **59:04** 总之，要想创建一个栩栩如生的世界，保持高密度可以奠定一个良好的基础。Mass Framework能帮助你轻松实现这一点。如果密度很大，那么保持密度就是关键。
> To conclude, to bring life to any world, it is true that having a high density is a great foundation. And the Mass Framework helped achieve that easily. However, if density is great, persistency is king.

---

## 七、总结

| 维度 | 技术方案 |
|------|---------|
| 城市布局 | Houdini 最短路径 + 网格匹配 |
| 道路 | 9 种基础模块 → 实例化点云 |
| 建筑 | DNA 系统 + 形状语法 + BDF |
| 屋顶 | 波函数坍缩 (33 网格体 → 2,600+ 结构) |
| 地面 | Nanite 预替换地砖 (250 万实例) |
| 场景布置 | 生态群落 + 填料散布器 |
| 人群 | MassAI + StateTree + 状态树 (35,000 人) |
| 交通 | MassAI + ZoneGraph + 队列机制 (18,000 辆) |
| 调试 | BugItGo 往返工作流 |
| 整个过程 | Houdini → 点云 → UE 实例化，约 25 分钟生成完整城市 |

> **59:36** 这是我们的最终成果，从无到有，利用程序化生成的数据，再到同时模拟出 100,000 个 MassEntity，包括行人和交通工具。这就是我们为城市赋予生命力的方式。
> This is the result we ended up with — starting small, leveraging the generated procedural data, all the way to simulating upwards of 100,000 mass entities at once, to the crowd and the traffic system. This is how we brought life to the city.
