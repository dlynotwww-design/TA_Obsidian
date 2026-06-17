---
tags:
  - 项目文档
  - PCG
  - UE5
  - Houdini
  - 管线
  - 性能优化
  - 美术管线
  - 作品集
created: 2026-06-18
status: 方案设计
related:
  - "[[场景大世界管线详解]]"
  - "[[UE5游戏项目流程]]"
---

# 🏯 《山海卷》— 东方奇幻城镇 PCG 管线

> **项目定位**：一个约 300m×300m 的东方奇幻风格城镇片区，完整展示 PCG 从 Houdini 到 UE5 的工业化落地流程。**核心看点不是"做了什么"，而是"管线怎么跑通——美术怎么用、TA 怎么串、性能怎么闭环"。**
>
> **对标参考**：米哈游璃月港/异环城市片区 · 腾讯天美秦朝古都 PCG 方案
>
> **技术栈**：Houdini SOP · VEX · HDA · UE5 PCG Framework · ISM/Nanite/LOD · World Partition
>
> **管线框架**：基于 [[场景大世界管线详解|场景大世界管线]] 六阶段流程（概念→白盒→地形→PCG→打磨→性能）

---

## 一、项目定位

### 1.1 为什么不做完整游戏

面试官想看的是你**做 PCG 管线的能力**，不是做游戏的能力。一个能跑通、美术能用、性能能闭环的 PCG 管线方案，远比一个粗糙的"游戏 Demo"有说服力。

更重要的是——**管线不是一个人的事**。这个文档展示的是你如何让整个美术团队高效运转：概念定方向 → 白盒验空间 → 地形打底 → PCG 铺量 → 手工精修 → 性能收束。

### 1.2 对标标准

| 维度 | 对标 |
|------|------|
| 管线框架 | [[场景大世界管线详解]] — 六阶段全流程 |
| 建筑生成 | UE5 Cassini Grammar 体积建筑 |
| 城市布局 | 腾讯天美秦朝古都 — 三阶段 PCG 工具集 |
| 资产管线 | 黑客帝国 CitySample — Houdini → UE 数据规范 |
| 性能 | ISM 合批 · Nanite · LOD 全链路 · World Partition |

### 1.3 面试一句话

> "我搭建了一个 300m×300m 的东方奇幻城镇 PCG 管线——从概念阶段就介入，Houdini 做路网和地块划分，Grammar 做建筑立面变体，UE5 PCG Framework 做最终散布。美术只需要调参数、标记排除区，不用离开编辑器。性能闭环：生成完立刻 Profile，超标就反推参数重生成。60fps，DrawCall < 500。"

---

## 二、场景设计

### 2.1 片区描述

> 一个依山傍水的东方奇幻风格临水城镇，包含码头、集市、居住区、山顶祭坛四个功能区。

### 2.2 规模指标

| 指标 | 数值 |
|------|------|
| 片区尺寸 | 300m × 300m |
| 建筑数量 | 约 200-300 栋（PCG 生成） |
| 建筑变体 | 每种基础模块 → 20+ 变体（Grammar + Seed） |
| 植被实例 | 约 5000+ 棵（HISM） |
| 道路总长 | 约 800m |
| 帧率目标 | 60fps（PC 1080p） |
| DrawCall 上限 | < 500 |
| 显存上限 | < 3GB |
| World Partition | 4 个 Cell（75m × 75m 每 Cell） |

### 2.3 场景分区

```
功能区划分：
├── 🚢 码头区（临水）
│   ├── 栈桥 + 渔船 + 水边吊脚楼
│   └── 特点：建筑密度低，水面开阔
│
├── 🏪 集市街区（中部）
│   ├── 主街沿线商铺 + 街边摊棚
│   └── 特点：建筑密集，道路最宽，行人/道具散布多
│
├── 🏠 居住区（缓坡）
│   ├── 依山而建的小型住宅群落
│   └── 特点：顺应地形，密度中等，巷道窄
│
└── ⛩️ 山顶祭坛（制高点）
    ├── 祭祀广场 + 石柱阵
    └── 特点：标志性建筑，手动精修（POI，不参与 PCG）
```

---

## 三、管线全景：六阶段全流程

> 本管线完全对标 [[场景大世界管线详解]] 的 Phase A→F 框架。每个阶段都标注了**美术干什么、TA 提供什么、产出什么**。

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    《山海卷》PCG 管线 — 六阶段全景                            │
│                                                                          │
│  Phase A          Phase B         Phase C          Phase D               │
│  概念 & 规划       白盒验证        地形制作         PCG 程序化生成 🔥        │
│  ─────────       ────────        ────────         ──────────────          │
│                                                                          │
│  概念美术：        关卡美术：        TA：             Houdini TA：           │
│  ├ 情绪版          ├ UE5 基础几何   ├ Gaea 高度图     ├ 路网 HDA            │
│  ├ 关键帧           │   快速搭白盒    │   自动侵蚀      ├ 地块划分 HDA         │
│  ├ 配色方案        ├ 路网 Spline    ├ 导入 Landscape  ├ Grammar 建筑 HDA    │
│  ├ 建筑风格参考     │   草绘走向      ├ 自动分层材质    ├ 植被散布 HDA         │
│  └ 区域规划图      ├ 关键地标定位    │   (Height/     └ 道路 Sweep HDA       │
│                    ├ 跑测验证       │    Slope/          │                │
│  TA：              │   空间尺度      │    Curvature)     UE5 PCG TA：       │
│  ├ 技术可行性评审   └ 天际线检查     └ RVT 配置         ├ PCG Graph 搭建     │
│  ├ 资产预算初算                                          ├ 自定义 PCG 节点    │
│  └ 参考《黑客帝国》                                      ├ ISM 合批策略       │
│      CitySample                                         └ Data Asset 配置   │
│      管线标准                                            │                  │
│                                                          关卡美术/地编：     │
│                                                          ├ 调 PCG 参数      │
│                                                          ├ 标记排除区域      │
│                                                          ├ 选择风格变体      │
│                                                          └ Cook → 即时预览  │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────── │
│  Phase E                     Phase F                                      │
│  手工打磨 & 灯光              性能优化 & 闭环 🔥                            │
│  ─────────────               ────────────────                             │
│                                                                          │
│  关卡美术/地编：              TA：                                         │
│  ├ Hero Asset 手工摆放       ├ stat unit / RenderDoc 抓帧                  │
│  │  (山顶祭坛/码头主建筑)     ├ ProfileGPU 定位热点                         │
│  ├ Lumen 灯光布置            ├ Unreal Insights → Game/Render Thread       │
│  │  (TOD 预设：清晨/正午/黄昏)├ 超标 → 反推 PCG 参数 → 重生成               │
│  ├ Post Process Volume       │   ├ DrawCall 超 → 提高 ISM 合并阈值         │
│  │  Color Grading / Bloom    │   ├ 面数超 → 调低散布密度 / LOD Screen Size │
│  └ 雾效 (Exponential Height  │   ├ 显存超 → 降低贴图分辨率 / Atlas 合并     │
│     Fog + 体积雾)             │   └ 三角面超 → 开启 Nanite（建筑/石头）     │
│                              ├ LOD 审核（植被 3 级 + Imposter）            │
│                              ├ Cull Distance 逐资产校准                    │
│                              └ 更新性能规范文档                             │
│                                                                          │
│  产出：视觉完成的关卡          产出：性能达标报告 + 优化后的管线参数           │
└──────────────────────────────────────────────────────────────────────────┘
```

> **核心循环**：PCG 生成 → 性能 Profile → 超标则反推参数 → 重生成 → 再 Profile → 收敛。这就是管线闭环。

---

## 四、Phase A — 概念 & 规划

### 4.1 美术做什么

| 角色 | 工作内容 | 具体产出 |
|------|---------|---------|
| **概念美术** | 东方奇幻城镇风格探索 | 情绪版（Mood Board）：参考凤凰古城+张家界地貌+宫崎骏色彩 |
| **概念美术** | 关键帧绘制 | 3-4 张 Key Art：码头黄昏/集市正午/居住区清晨/祭坛夜景 |
| **概念美术** | 配色方案 | 木质暖色系（建筑）+ 青灰石板（路面）+ 墨绿（植被）+ 朱红（点缀） |
| **概念美术** | 建筑风格参考 | 吊脚楼（码头）+ 木构商铺（集市）+ 硬山民居（居住）+ 重檐歇山（祭坛） |
| **关卡策划** | 区域规划图 | 四个功能区的边界、主路径走向、关键地标位置 |

### 4.2 TA 做什么

| 工作内容 | 产出 |
|---------|------|
| 技术可行性评审 | Nanite/Lumen/WP 在 300m×300m 规模下的性能预估 |
| 资产预算初算 | 建筑模块数（6-8 种）、植被种类（15-20 种）、贴图总量上限（< 2GB） |
| 管线标准对齐 | 对标 [[03_PCG研究/典型案例/UE5 《黑客帝国》PCG案例分析1：资产与内容管线\|《黑客帝国》CitySample]] 的资产命名/Pivot/UV 规范 |

---

## 五、Phase B — 白盒验证

### 5.1 美术做什么

```
关卡美术（地编）在 UE5 内操作：
├── 用基础几何体（Box/Cylinder/Plane）快速搭出城镇体块
│   ├── 建筑用地块用 Box 占位（标注高度：1F/2F/3F）
│   ├── 道路用拉长的 Box 表示宽度等级（12m/6m/3m）
│   └── 关键地标用特殊颜色标记（码头/祭坛/集市中心）
│
├── 手绘路网 Spline（在 UE5 中直接画）
│   ├── 主干路：入口 → 集市 → 码头
│   ├── 次干路：从主干路分叉到居住区
│   └── 水系 Spline：湖岸线
│
├── 跑测验证：
│   ├── 从入口走到祭坛需要多久？（目标 2-3 分钟）
│   ├── 天际线是否好看？（从水面望向城镇）
│   └── 遮挡关系是否合理？（集市不能完全挡住码头视线）
│
└── 标记 POI 区域：
    ├── 山顶祭坛 = 纯手工区域（PCG 不碰）
    └── 码头主建筑 = 半手工（PCG 生成 + 手工替换）
```

### 5.2 TA 提供什么

| 工具/规范 | 说明 |
|----------|------|
| 白盒几何体模板 | 预设建筑体块尺寸（4m×4m/4m×8m/8m×8m），对齐到 1m Grid |
| Spline 导出脚本 | 地编画的 Spline → 导出 JSON → Houdini 读取（后续 Phase D 用） |
| World Partition 初始配置 | 4 个 Cell，Cell Size = 75m，Loading Range = 200m |

### 5.3 产出

> 可跑测的白盒关卡 + 路网 Spline JSON + POI 标记列表

---

## 六、Phase C — 地形制作

### 6.1 美术做什么

| 步骤 | 工具 | 说明 |
|------|------|------|
| 高度图生成 | Gaea / Houdini | 300m×300m，一侧山体（20-50m 高）+ 缓坡过渡到水面 |
| 侵蚀模拟 | Gaea (Hydraulic/Thermal) | 让山体边缘自然，形成溪流沟壑 |
| 导入 UE5 | Landscape Import | 分辨率 2017×2017，4 个 Component |

### 6.2 TA 提供什么

```
自动分层材质系统（母材质 ML_LandscapeAuto）：

Layer 分配（由 Height / Slope / Curvature 驱动）：
├── Layer 0（水面以下 < 0m）         → 河床泥 (Riverbed_Mud)
├── Layer 1（0-5m, slope < 10°）    → 草地 (Grass_Base)
├── Layer 2（0-15m, slope 10-25°）  → 碎石草地 (Grass_Gravel)
├── Layer 3（5-25m, slope 25-40°）  → 岩石裸露 (Rock_Exposed)
├── Layer 4（> 25m, slope > 40°）   → 悬崖岩壁 (Cliff_Face)
└── Layer 5（手动涂刷）              → 砂土路面 (Dirt_Path)

RVT (Runtime Virtual Texture) 配置：
├── RVT Volume 覆盖全场景
├── 地形材质写入 BaseColor/Normal/Height 到 RVT
└── 后续 PCG 散布的石头/植被采样 RVT 做高度匹配
```

### 6.3 产出

> Landscape + 自动分层材质 + RVT 设置

---

## 七、Phase D — PCG 程序化生成 🔥

> **这是管线最核心的阶段。Houdini TA 开发离线生成工具，UE5 PCG TA 搭建实时散布图，美术在编辑器内调参。**

### 7.1 整体架构：四层生成 + 双向分工

```
┌──────────────────────────────────────────────────────────────────┐
│                   Phase D：PCG 四层生成架构                          │
│                                                                  │
│  Houdini TA（离线开发 HDA）          UE5 PCG TA（编辑器集成）         │
│  ─────────────────────────         ─────────────────────────     │
│                                                                  │
│  Layer 1: 路网 + 地块                                              │
│  ┌──────────────────────┐         ┌────────────────────────┐     │
│  │ 读入 Phase B 的 Spline│         │ PCG Spline Sampler     │     │
│  │ A* 最小坡度路径寻路    │──.json─→│ 读取路网 Spline         │     │
│  │ Voronoi 地块细分      │──.json─→│ 按地块标记采样点         │     │
│  │ 地块类型自动分类       │         │ Bounds Modifier 裁剪    │     │
│  └──────────────────────┘         └────────────────────────┘     │
│                                                                  │
│  Layer 2: 建筑变体                                                │
│  ┌──────────────────────┐         ┌────────────────────────┐     │
│  │ Grammar HDA          │──.fbx──→│ Static Mesh 资产库      │     │
│  │ 模块拼装 + UV + 碰撞  │──.csv──→│ PCG Point Cloud 读取    │     │
│  │ 地块类型→Grammar 映射 │         │ Static Mesh Spawner     │     │
│  └──────────────────────┘         │ ISM 自动合并            │     │
│                                   └────────────────────────┘     │
│                                                                  │
│  Layer 3: 植被与道具                                              │
│  ┌──────────────────────┐         ┌────────────────────────┐     │
│  │ Poisson Disk 采样     │──.csv──→│ Surface Sampler (地形)  │     │
│  │ 避让建筑/道路/已有点  │         │ Density Filter (坡度)   │     │
│  │ 生态群落标签          │         │ Transform Modifier      │     │
│  └──────────────────────┘         │ HISM Spawner            │     │
│                                   └────────────────────────┘     │
│                                                                  │
│  Layer 4: 路面 + 街道家具                                          │
│  ┌──────────────────────┐         ┌────────────────────────┐     │
│  │ 道路截面 Sweep        │──.fbx──→│ Spline Mesh (路面)      │     │
│  │ 等距采样 + 法线偏移   │──.csv──→│ Spline Sampler (等距)   │     │
│  │ 家具散布点云          │         │ 路灯/行道树/摊位散布     │     │
│  └──────────────────────┘         └────────────────────────┘     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 7.2 Layer 1 — 路网与地块（Houdini TA 主导）

#### 美术输入（来自 Phase B 白盒阶段）

```
地编在 UE5 中已完成的：
├── 用地边界 Spline（闭合曲线）
├── 关键节点位置：码头 / 集市中心 / 山顶祭坛 / 主入口
├── 水系 Spline（湖岸线）
└── POI 排除区域标记（祭坛广场 = 不参与地块划分）
```

#### Houdini TA：路网生成算法

**目标**：读入美术的 Spline + 关键节点，自动生成三级路网。

```
算法流程：
1. 主干路：连接关键节点（入口→集市→码头），沿地形最小坡度路径（A* 寻路）
2. 沿水道路：平行于水系 Spline，偏移 5-8m（留出码头栈桥空间）
3. 次干路：从主干路分叉出来，覆盖居住区，保证每个地块可达
4. 巷道：在剩余空间填充，连接次干路
```

**VEX 实现**：

```vex
// 主干路路径生成 — 基于关键节点和地形的最小成本路径
// 输入：起点 @start_pt，终点 @end_pt，地形高度场 @height

int find_min_cost_path(int start_pt; int end_pt; string height_attr) {
    // 使用 A* 在高度场上寻路
    // 成本 = 距离 + 坡度惩罚 × slope_weight
    // 保证道路不穿过悬崖（坡度 > 阈值 → 成本无穷大）
    // ...
}

// 坡度成本计算
float slope = abs(point(1, "slope", candidate_pt));
float cost = distance + slope * chf("slope_penalty");
```

#### Houdini TA：地块划分算法

**目标**：在路网围合区域内，自动划分建筑地块。

```
算法：路网 → 封闭面 → Voronoi 细分 → 沿路回缩 → 类型分类
1. 路网 → 封闭多边形面（PolyFill / Boolean）
2. 面内 Voronoi 细分（控制地块面积 50-200m²）
3. 每个地块沿路边回缩 1-3m（Setback）
4. 地块自动分类：
   ├── 沿主干路 → commercial（面宽大、进深浅）
   ├── 沿次干路 → mixed
   ├── 内陆 → residential
   └── 手动标记 → plaza / dock / temple（跳过自动分类）
```

**VEX 实现**：

```vex
// 在路网围合区域内生成 Voronoi 细胞
// 输入：区域多边形面 prim，种子点数量 n_seeds

// 1. 在面内散播种子点
for (int i = 0; i < n_seeds; i++) {
    float seed_x = fit01(rand(i * 123.456), bbox_min.x, bbox_max.x);
    float seed_y = fit01(rand(i * 789.012), bbox_min.y, bbox_max.y);
    if (in_polygon(seed_x, seed_y, prim)) {
        add_point(geoself(), set(seed_x, 0, seed_y));
    }
}

// 2. 每个面元上的点，分配最近种子 = 地块归属
int nearest = nearpoint(1, @P);
i@parcel_id = nearest;

// 3. 地块沿路边回缩 → 用 PolyExpand2D 向内侧偏移
```

#### 输出到 UE 的数据格式

```json
{
  "parcels": [
    {
      "id": 42,
      "type": "commercial",
      "polygon_vertices": [[x1,y1], [x2,y2], ...],
      "area": 85.3,
      "setback_distance": 1.5,
      "max_height": 12.0,
      "road_access": "primary"
    }
  ]
}
```

### 7.3 Layer 2 — 建筑 Grammar 变体（Houdini TA 开发，UE 侧读取）

#### 美术准备（3D 场景美术）

```
建筑模块库（手工建模 6-8 个基础模块）：

墙体模块（尺寸标准化，确保拼接无缝）：
├── 墙体基座 4m×3m（宽×高）
├── 墙体标准段 4m×3m
├── 墙体转角 1m×3m
├── 墙体开口段（门窗预留）2m×3m

屋顶模块：
├── 歇山顶（大型公共建筑/商铺门头）
├── 悬山顶（住宅）
├── 硬山顶（仓库/工坊）

门窗模块：
├── 商铺门面（大开口，3 种样式）
├── 住宅门窗（小开口，2 种样式）
├── 吊脚楼窗（码头区特有）

装饰模块：
├── 飞檐翘角（屋顶边缘）
├── 灯笼（分离为单独 Mesh，Phase D Layer 3 散布）
├── 木格栅（阳台/栏杆）
```

> **美术只需要做 6-8 个基础模块**，200+ 变体由 Houdini Grammar 自动拼装。

#### Houdini TA：Grammar 语法定义

```yaml
语法规则（借鉴 UE5 Cassini Grammar）：
  MainFloor  → [Wall, Window, Wall, Window, Door, Wall]
  Second     → [Wall, Window, Wall, Wall, Window, Wall]
  Third      → [Wall, Window, Wall]
  Roof       → GableRoof | HipRoof | FlatRoof

  终端替换（概率驱动）：
  Wall       → basic_wall (70%) | decorated_wall (30%)
  Window     → square_window | round_window | latticed_window
  Door       → shop_door | residential_door
```

**面向地块类型的 Grammar 映射表**：

| 地块类型 | Grammar | 层数 | 屋顶 | 风格标签 |
|----------|---------|:---:|------|----------|
| commercial | MainFloor(Shop), Second, Roof | 2-3 | 歇山顶 | 大红灯笼 + 雕花门面 |
| mixed | MainFloor, Second, Roof | 2 | 悬山顶 | 简约木构 |
| residential | MainFloor, Roof | 1-2 | 硬山顶 | 小院 + 木格栅 |
| stilt_house | StiltFloor, MainFloor, Roof | 2 | 悬山顶 | 吊脚 + 开敞阳台 |

**VEX 实现 Grammar 拼装**：

```vex
// 将 Grammar 字符串解析为模块序列，沿横截面依次放置
string grammar = "MainFloor,Second,Roof";
string main_floor[] = {"Wall", "Window", "Wall", "Door", "Wall"};

float cursor = 0;
for (int i = 0; i < len(main_floor); i++) {
    string module_type = main_floor[i];
    float width = get_module_width(module_type);  // 查模块宽度表
    matrix xform = ident();
    translate(xform, set(cursor, 0, 0));
    s@module_names[i] = module_type;
    f@module_widths[i] = width;
    cursor += width;
}
```

#### UV 策略

```
UV 两套体系（对标 CitySample）：
├── UV0：主材质 UV（0-1 空间，世界对齐纹理）
├── UV1：生成时烘焙的 AO + Dirt Mask（Houdini 中预计算）
└── Texel Density：统一 512px/m
```

### 7.4 Layer 3 — 植被与道具散布

#### 散布策略总览（Houdini TA 设计算法，UE 侧执行）

```
散布层级（从大到小）：
Layer A — 行道树（沿道路 Spline 等距 8m，UE Spline Sampler 直接做）
Layer B — 大乔木（Poisson Disk，间距 ≥ 3m，Houdini 预计算点云 → CSV）
Layer C — 灌木（基于大乔木位置边缘填充，UE Density Filter + Noise 做）
Layer D — 地表花草（随机 + 密度噪声，UE Surface Sampler 做）
Layer E — 街道道具（灯笼/摊位/木箱/渔网，UE Spline Sampler 做）
```

#### Poisson Disk 采样（Houdini 侧 VEX）

```vex
// Poisson Disk Sampling — 保证最小间距的随机散布
float r_min = chf("radius_min");  // 3m（大乔木）
int k = 30;                       // 每个点 30 次尝试

// 1. 初始化：随机放第一个点
vector first = random_point_in_bounds(bbox);
add_point(geoself(), first);

// 2. 迭代：从活跃列表中随机选点，生成候选
int active_list[] = {0};
int spatial_grid[];  // 空间哈希网格（加速最近点查询）

while (len(active_list) > 0) {
    int idx = active_list[floor(rand(seed++) * len(active_list))];
    vector center = point(geoself(), "P", idx);
    
    int found = 0;
    for (int attempt = 0; attempt < k; attempt++) {
        float angle = rand(seed++) * 2 * PI;
        float dist = r_min + rand(seed++) * r_min;
        vector candidate = center + set(cos(angle)*dist, 0, sin(angle)*dist);
        
        if (in_bounds(candidate) && !too_close(candidate, r_min, spatial_grid)) {
            int new_pt = add_point(geoself(), candidate);
            append(active_list, new_pt);
            found = 1;
            break;
        }
    }
    if (!found) removeindex(active_list, idx);
}
```

#### 避让算法（VEX）

```vex
// 散布时避让建筑、道路、已有大乔木
int obstacles[] = pcfind(1, "P", @P, chf("avoid_radius"), 1);
if (len(obstacles) > 0) {
    @density = 0.0;  // 不放置
    return;
}

// 距离衰减（离障碍物越近越稀疏）
float min_dist = 9999;
for (int i = 0; i < len(obstacles); i++) {
    vector obst_pos = point(1, "P", obstacles[i]);
    float d = distance(@P, obst_pos);
    min_dist = min(min_dist, d);
}
@density = smooth(0, chf("avoid_radius"), min_dist);
```

### 7.5 Layer 4 — 道路与街道家具

#### 道路截面参数化

```
主干路（12m 宽，两车道 + 两侧人行道）：
├── 车行道 8m（居中）→ 石板路面
├── 人行道 每侧 2m → 卵石路面
└── 排水沟 每侧 0.3m

次干路（6m 宽）：
├── 车道 4m
└── 人行道 每侧 1m

巷道（3m 宽）：
└── 石板路 3m（人车混行）
```

#### 街道家具自动散布（UE Spline Sampler）

```
沿道路 Spline 等距散布：
├── 路灯（间隔 25m，沿法线偏移 1.5m 到路肩）
├── 行道树（间隔 8m，树种按街区风格切换）
├── 摊位（集市主街专用，间隔 10-15m，随机微调 ±2m）
├── 灯笼串（横跨街道，间隔 30m）
└── 码头区：系船柱 + 渔网架 + 木箱堆

算法：
1. Resample Spline → 等距采样点
2. 沿法线偏移到路肩
3. 采样地形高度
4. ±10% 间距抖动（避免机械感）
```

### 7.6 UE5 PCG Graph 节点网络（UE PCG TA 搭建）

```
PCG Graph: Town_Generator

Inputs:
├── Landscape (Height Data)
├── Parcel Splines (从 Houdini 导入 JSON → Spline)
├── Road Splines (从 Houdini 导入)
└── Water Body Spline (地编手动放置)

Graph 结构：

[Landscape Height] ──→ [Surface Sampler (按 Slope/Height 分区)]
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
     [Density Filter]  [Density Filter]  [Density Filter]
       slope < 25°       slope 25-40°      slope > 40°
       建筑/植被区         灌木过渡区          岩壁区
              │               │               │
    ┌─────────┼─────────┐     │               │
    ↓         ↓         ↓     ↓               ↓
[Bldg A]  [Bldg B]  [Bldg C] [Shrub]    [Rock Wall]
(商业)     (混合)     (住宅)  散布        散布
    │         │         │
    └─────────┼─────────┘
              ↓
    [Bounds Modifier] ← 按地块边界裁剪
              │
    [Transform Modifier] ← 随机旋转 ±15°, 缩放 0.9-1.1×
              │
    [Static Mesh Spawner] ← 根据属性 mesh_asset 分发
              │
    [ISM 自动合并] ← 同 Mesh 实例 → HISM

[Road Splines] ──→ [Spline Sampler (等距)]
    ├──→ [Transform Modifier] → [SM Spawner] → 路灯
    ├──→ [Transform Modifier] → [SM Spawner] → 行道树
    └──→ [Spline Mesh (沿路径)] → 路面 Mesh
```

### 7.7 自定义 PCG 节点（蓝图扩展）

> **展示 UE 底层能力的加分项**

```
自定义 PCG 节点 1：Distance To Water
  - 输入：Water Spline
  - 输出：每个点 float 属性 "dist_to_water"
  - 用途：临水建筑风格切换、水面反射距离控制

自定义 PCG 节点 2：Building Grammar Lookup
  - 输入：地块类型（从属性 "parcel_type" 读取）
  - 输出：建筑资产列表（mesh_assets 数组）+ 层数 + 屋顶类型
  - 用途：地块 → Grammar 的查找表

自定义 PCG 节点 3：Slope Based Filter
  - 输入：Landscape + 采样点
  - 输出：符合坡度条件的点 + slope 属性
  - 用途：建筑只放缓坡，植被可放中坡
```

### 7.8 美术在 PCG 阶段的日常操作

```
地编/关卡美术在 UE 编辑器内（不打开 Houdini）：

1. 打开 Town_Generator PCG Component
2. 调全局参数：
   ├── Seed = 42           ← 换个种子看不同布局
   ├── Building Density = 1.0  ← 加减密度
   ├── Tree Coverage = 70%     ← 调节植被
   └── Style Variant = 1       ← 切换模块组风格
3. 选中某个区域 → 标记为 "Exclusion Zone" → PCG Cook 时跳过
4. 选中某个地块 → 覆盖 Grammar 类型（手动改为 plaza）
5. 点击 "Cook" → 等待数秒 → 场景刷新
6. 不满意？→ 调参 → 再 Cook → 即时迭代

TA 确保：
  - Cook 时间 < 10 秒（全场景）
  - 参数修改后增量更新（只重算变化区域）
  - 手动摆放的 Hero Asset 不被 Cook 覆盖
```

---

## 八、Phase E — 手工打磨 & 灯光

### 8.1 美术做什么

| 工作内容 | 说明 |
|---------|------|
| **Hero Asset 摆放** | 山顶祭坛（石柱阵 + 祭坛主体 + 香炉）、码头主建筑（替换 PCG 生成的）、集市入口牌坊 |
| **Lumen 灯光** | Directional Light（模拟太阳）+ Sky Light + Sky Atmosphere + 局部补光（集市灯笼点光源） |
| **TOD 预设** | 清晨（暖金色低角度）/ 正午（高对比度）/ 黄昏（橙红长阴影）/ 夜景（灯笼自发光 + 月光） |
| **后处理** | Post Process Volume：Color Grading LUT（暖色倾向）、Bloom（灯笼高光）、Vignette |
| **雾效** | Exponential Height Fog（山腰雾气层）+ 局部 Volumetric Fog（码头水面晨雾） |

### 8.2 TA 提供什么

| 工具/规范 | 说明 |
|----------|------|
| TOD 灯光预设 Data Asset | 4 套灯光参数（清晨/正午/黄昏/夜景），地编一键切换 |
| LUT 调色方案 | Photoshop 调色 → 导出 LUT 贴图 → UE Color Grading |
| 雾效参数模板 | Height Fog 衰减曲线、体积雾 Density 预设 |

---

## 九、Phase F — 性能优化 & 闭环 🔥

> **这是管线闭环的关键：生成 → Profile → 超标 → 反推参数 → 重生成。**

### 9.1 优化三层策略

```
性能优化分层：

┌─── 资产层（Phase C-D 前定规范）───┐
│ 1. 面数规范    │ 建筑 LOD0 < 5000△, 植被 LOD0 < 500△
│ 2. 材质规范    │ 统一 Master Material, 每实例 1-2 Texture Sample
│ 3. 贴图规范    │ 512px/m, 最大 2K, Texture Atlas 优先
│ 4. 碰撞规范    │ 建筑 Box 碰撞, 植被无碰撞, 地面 Mesh 无碰撞
└──────────────┘
        ↓
┌─── 引擎层（PCG Graph 配置）───┐
│ 5. ISM/HISM   │ 同种植物→HISM, 同建筑模块→ISM
│ 6. Nanite     │ 建筑/石头 Mesh 开启 Nanite
│ 7. LOD        │ 植被 3 级 + Imposter, 建筑 2 级
│ 8. Culling    │ 小道具 Cull 50m, 路灯 Cull 80m, 建筑 Cull 150m
└──────────────┘
        ↓
┌─── 场景层（World Partition）───┐
│ 9. World Partition │ 4 Cell (75m), Loading Range 200m
│ 10. Lightmap   │ 静态建筑 Lightmap, 仅主光动态
│ 11. Shadow     │ CSM 3 级: 0-20m / 20-80m / 80-300m
│ 12. HLOD       │ 远景 LOD→HLOD 合并（Nanite 后此步可能不需要）
└──────────────┘
```

### 9.2 性能目标

```
性能目标：
  Game Thread:   < 6ms
  Render Thread: < 10ms
  GPU:           < 12ms
  DrawCall:      < 500
  Triangles:     < 2M (可视范围内)
  显存:          < 2.5GB

验证工具：
  stat fps / stat unit           → 帧率 + 线程耗时
  stat scenerendering           → DrawCall / Triangle Count
  stat rhi                       → 显存使用
  ProfileGPU                     → GPU Pass 耗时分解
  Unreal Insights                 → CPU 瓶颈定位
  Nanite Visualization → Triangles → Nanite 面数
```

### 9.3 ISM 合批量化

```
同物种植被 HISM：
  未合批：5000 棵松树 = 5000 DrawCall
  合批后：1 个 HISM Component = 1 DrawCall
  内存：每个实例 4×4 矩阵 = 64 bytes × 5000 ≈ 320KB

建筑 ISM：
  未合批：200 栋 × 平均 5 模块 = 1000 DrawCall
  合批后：按 Mesh 类型合并 → 约 30 ISM Component = 30 DrawCall

策略：
  - Houdini 导出时每 Mesh 打 InstanceGroup 标签
  - PCG Graph → Static Mesh Spawner → "Use ISM"
  - PCG Component: bUseInstancePartitioning = true
```

### 9.4 性能闭环工作流

```
完整迭代循环：

  Cook PCG →
  ┌──────────────────────────────────────────────┐
  │ 在编辑器内跑 stat unit / stat scenerendering  │
  │ ProfileGPU 抓一帧                             │
  └──────────────┬───────────────────────────────┘
                 ↓
  ┌──────────────────────────────────────────────┐
  │ 分析结果 vs 预算：                             │
  │                                               │
  │ ✅ 全都达标 → 通过，冻结参数                    │
  │ ❌ DrawCall > 500 →                            │
  │    → 提高 ISM 合并阈值（允许更大批）             │
  │    → 降低散布密度 10%                          │
  │    → 重 Cook                                   │
  │ ❌ Triangles > 2M →                            │
  │    → 调低建筑 LOD0 面数上限                     │
  │    → 减小 Cull Distance（近处才显示高模）        │
  │    → 重 Cook                                   │
  │ ❌ 显存 > 2.5GB →                              │
  │    → 贴图降分辨率（2K→1K）                      │
  │    → Texture Atlas 合并（减少贴图数量）          │
  │    → 重导入资产                                 │
  │ ❌ Game Thread > 6ms →                         │
  │    → Unreal Insights 定位 Tick 热点             │
  │    → 减少 PCG Component 每帧更新的 Cell 数       │
  └──────────────┬───────────────────────────────┘
                 ↓
  ┌──────────────────────────────────────────────┐
  │ 重生成 → 再 Profile → 直到达标                  │
  │                                               │
  │ 一般 2-3 轮收敛                                │
  └──────────────────────────────────────────────┘
```

---

## 十、数据管线：Houdini → UE 全链路

> 对标 [[03_PCG研究/典型案例/UE5 《黑客帝国》PCG案例分析1：资产与内容管线\|《黑客帝国》CitySample]] 的 USD 管线，本项目用简版 JSON/CSV/FBX 组合。

### 10.1 数据格式规范

```
1. 地块数据 → JSON
   - 多边形顶点数组 + 属性（类型/面积/限高/临路等级）

2. 建筑资产 → FBX
   - Static Mesh（含 LOD 0-2）
   - Pivot 在底面中心
   - 碰撞体：Box 简化碰撞
   - 材质 ID：按物理材质分类（玻璃=1, 木材=2, 石材=3）

3. 散布点云 → CSV
   - Position/Rotation/Scale
   - mesh_asset 引用路径
   - 自定义属性：species, biome_tag, density, seed

4. 道路 Spline → JSON（控制点 + Tangents）
```

### 10.2 Houdini 自动化导出（Python）

```python
# 批量 Cook HDA + 导出所有资产
import hou
import json

def cook_and_export_town(hda_path, output_dir, seed=42):
    hda = hou.node("/obj").createNode("town_generator")
    hda.parm("seed").set(seed)
    hda.parm("map_size").set(300)
    hda.cook(force=True)
    
    # 导出建筑 FBX
    building_node = hda.node("output_buildings")
    for i, prim in enumerate(building_node.geometry().prims()):
        building_name = prim.attribValue("building_name")
        rop = hou.node("/out").createNode("rop_fbx")
        rop.parm("sopoutput").set(f"{output_dir}/buildings/{building_name}.fbx")
        rop.render()
    
    # 导出地块 JSON
    parcels = []
    parcel_node = hda.node("output_parcels")
    for prim in parcel_node.geometry().prims():
        parcels.append({
            "id": prim.attribValue("parcel_id"),
            "type": prim.attribValue("parcel_type"),
            "vertices": [list(v.point().position()) for v in prim.vertices()],
            "area": prim.attribValue("area")
        })
    with open(f"{output_dir}/parcels.json", "w") as f:
        json.dump({"parcels": parcels}, f, indent=2)
```

---

## 十一、美术可控性：编辑器集成

### 11.1 参数暴露设计

```
暴露给美术的 PCG 全局参数（直接在 PCG Component 上调）：
├── Seed              — 全局随机种子（换一个 = 全新布局）
├── Building Density  — 建筑密度 0.5-1.5（乘数）
├── Tree Coverage     — 植被覆盖率 0-100%
├── Road Width Scale  — 道路宽度缩放
└── Style Variant     — 风格变体 0-3（不同建筑模块组）

暴露给美术的局部参数（放到 PCG Data Asset）：
├── 建筑 Grammar 字符串
├── 允许的模块列表
├── 高度范围
└── 材质覆写
```

### 11.2 PCG Data Asset — 面向地编的配置化

```
UPCG_BuildingRules (Data Asset)：
  地块类型 → Grammar 映射表：
    "commercial"  → { layers: ["MainFloor_Shop", "Second", "Roof_Gable"],
                      mesh_library: ["wall_shop", "door_large", "roof_gable_A"],
                      max_height: [10, 15],
                      color_variant: [0.8, 1.2] }
    "residential" → { ... }
    "stilt_house" → { ... }
```

### 11.3 美术日常操作一览

```
美术在整个项目中只需要做：

Phase A（概念）：
  └── 画 Mood Board + Key Art + 区域规划图

Phase B（白盒）：
  └── 在 UE 里用 Box 搭白盒 + 手绘路网 Spline + 跑测

Phase C（地形）：
  └── Gaea 调参生成高度图 → 导入 UE（一键）
     （TA 已配好自动分层材质，导入即生效）

Phase D（PCG）：
  └── 调 PCG 参数 → Cook → 不满意再调 → 再 Cook
     （全程在 UE 编辑器中，不需要打开 Houdini）

Phase E（打磨）：
  └── 手工摆放 Hero Asset + 灯光 + 后处理 + 跑测

Phase F（性能）：
  └── 开 stat unit 看一眼（TA 已配好预算表）
     超标 → 告诉 TA → TA 反推参数 → 重生成
```

---

## 十二、管线开发时间线（5 周）

| 周 | 阶段 | 任务 | 产出 |
|:---:|------|------|------|
| W1 | Phase A-B | 概念设计 + 白盒搭建 | Mood Board / 白盒关卡 / Spline JSON |
| W2 | Phase C-D | 地形 + Houdini HDA 开发 | Landscape + 路网/地块/建筑 HDA 原型 |
| W3 | Phase D | UE5 PCG Graph 搭建 + 集成 | 四层生成在 UE 中跑通、美术可调参 |
| W4 | Phase E-F | 手工打磨 + 性能优化循环 | 灯光/后处理/性能达标 60fps, DC<500 |
| W5 | 收尾 | 参数暴露 + Data Asset + 文档 | 美术操作指南 + 性能规范文档 + 技术文档 |

---

## 十三、与已有项目的差异化定位

| | 已有工作项目 | 《山海卷》 |
|------|----------|----------|
| 性质 | 工作产出（片段展示） | 个人作品（完整管线） |
| 管线视角 | 某个功能模块 | 六阶段全流程（概念→性能闭环） |
| 美术流程 | 没讲美术怎么用 | 每阶段标注美术/TA 分工 |
| 性能 | 定性描述 | 量化指标 + 反推闭环 |
| 文档 | 散落在各文件夹 | 一篇结构化管线文档 |
| 面试 | 靠嘴说 | 打开 Obsidian 直接展示每个阶段的产出和规范 |

---

## 十四、简历呈现

> **《山海卷》— UE5 PCG 城镇管线 | 个人项目 | 2026**
>
> - 对标 [[场景大世界管线详解|场景大世界管线]] 六阶段框架，搭建 300m×300m 东方奇幻城镇 PCG 管线，覆盖 4 功能区（码头/集市/居住/祭坛），200+ 栋建筑程序化生成
> - Houdini 侧：VEX 实现 A* 路网寻路（坡度惩罚）、Voronoi 地块细分（50-200m²）、Poisson Disk 植被散布（空间哈希加速）、Grammar 建筑变体（4 套语法规则 × 6-8 基础模块 = 200+ 变体）
> - UE5 侧：PCG Graph 完整节点网络 + 3 个蓝图自定义节点（Distance to Water / Grammar Lookup / Slope Filter），ISM 合批将植被 DrawCall 从 5000+ 降至 < 50
> - 管线闭环：生成 → stat unit/RenderDoc 抓帧 → 超标则反推参数重生成 → 收敛至 60fps, DrawCall < 500, 显存 < 2.5GB
> - 美术全过程可在 UE 编辑器内完成（调参/Cook/标记排除区），无需打开 Houdini；TOD 灯光预设+Data Asset 配置化

---

> [!TIP] 相关知识库
> - 管线框架 → [[场景大世界管线详解]] / [[UE5游戏项目流程]]
> - PCG 案例 → [[03_PCG研究/典型案例/UE5 《黑客帝国》PCG案例分析1：资产与内容管线|《黑客帝国》PCG 案例]] / [[03_PCG研究/技术大会/游戏程序化生成（PCG）之路：重建秦朝古都|腾讯天美秦朝古都]]
> - 算法参考 → [[03_PCG研究/相关算法/UE PCG项目源码全拆解（总览）|UE PCG 源码拆解]] / [[03_PCG研究/相关算法/技术美术 技美篇（十一）：【PCG TA】WFC 波函数坍塌 （一）|WFC 算法]]
> - 软件技能 → [[03_PCG研究/软件技能/00_Houdini底层架构与技术解析|Houdini 底层架构]] / [[03_PCG研究/软件技能/UE5.5新PCG场景Cassini分析-02 Grammar（续）|Cassini Grammar]]
