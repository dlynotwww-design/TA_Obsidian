# dd_Ivy 常春藤生成器 — 技术文档

**HDA 类型：** `sop/dd_Ivy`
**路径：** `/obj/geo1/Ivy1`
**节点总数：** 83（8 个 NetworkBox 分组 + 24 个未分组节点）
**用途：** 在任意输入几何体表面自动生成常春藤（枝干 + 叶子）

---

## 一、外部参数

| 文件夹 | 参数 | 类型 | 默认 | 当前值 | 说明 |
|--------|------|------|------|--------|------|
| Base Settings | Input_Remeshing | Float | — | **0.055** | 输入几何体 remesh 的边长大小 |
| Base Settings | dist2 | Float | — | **0.1** | 裁剪容差距离 |
| Base Settings | offset | Float | — | **0.0** | 整体偏移 |
| Base Settings | densityscale | Float | — | **150.0** | 种子点散布密度缩放系数 |

---

## 二、管线总览

```
输入几何体
    │
    ▼
┌─────────────────────────────────────────────────────┐
│  Stage 1  重建网格                                    │
│  remeshgrid1 → peak1 → INPUT_Remeshed               │
│  基底重网格化 + 微膨胀                                │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  Stage 2  散布种子点（三层筛选）                       │
│  clip1 → attribnoise1 → blast1 →                    │
│  attribnoise2 → scatter1                            │
│  几何裁剪 → 生长遮罩 → 密度控制                        │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  Stage 3  生成主体枝干（核心）                         │
│  sort1 → grouprange1 → random_selection1 →          │
│  connectadjacentpieces1 → findshortestpath1 →       │
│  delete_small_parts1 → carve                        │
│  最短路径算法连接散点形成枝干网络                       │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  Stage 4  重建分支线 + 统一方向                        │
│  [foreach: resample1 → fuse1 → polypath1 →          │
│   resample2 → attribpromote1 → attribremap1]        │
│  逐条处理：重采样 → 融合 → 路径化 → 统一方向           │
└──────────┬──────────────────────────┬───────────────┘
           │                          │
           ▼                          ▼
┌──────────────────────┐  ┌──────────────────────────┐
│  Stage 5  次级分支     │  │  Stage 6  筛选垂挂部分    │
│  主枝干上随机选点      │  │  检测 N_copy.y < 0       │
│  生成小分支曲线        │  │  标记垂挂点               │
└──────────┬───────────┘  └────────────┬─────────────┘
           │                           │
           │                           ▼
           │              ┌──────────────────────────┐
           │              │  Stage 7  垂挂分支         │
           │              │  在垂挂点上生成向下分支    │
           │              └────────────┬─────────────┘
           │                           │
           └───────────┬───────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  Stage 8+9  枝干3D化 + 叶子粘贴 + 材质输出            │
│  merge → sweep1(枝干成管) → color → connectivity →  │
│  vertex_colors → unreal_material                    │
│  copytocurves1(叶子) ← Pre-made_leaves(stash)       │
│  → merge5 → output0                                 │
└─────────────────────────────────────────────────────┘
```

**管线一句话总结：** 输入几何体 → 重网格化 → 三层筛选散布种子 → 最短路径连枝干 → 逐条规范化 → 主分支 / 垂挂分支并行生成 → sweep 成管 + 贴叶 + 材质输出

---


## 三、各阶段概览

### Stage 1 — 重建网格

| 节点 | 关键参数 | 功能 |
|------|---------|------|
| remeshgrid1 | Input_Remeshing=0.055 | 将任意输入几何体重网格化，使布线均匀 |
| peak1 | — | 沿法线微膨胀，防止枝干穿插基底 |
| INPUT_Remeshed | null 标记 | 输出节点，供后续引用 |

### Stage 2 — 散布种子点（三层筛选）

| 层 | 节点 | 属性 | 筛选逻辑 |
|----|------|------|---------|
| 1. 几何裁剪 | clip1 | 物理空间 | origin=(0,-0.51,0)，只保留 Y>-0.51 的墙面区域 |
| 2. 生长遮罩 | attribnoise1 → blast1 | @mask | 粗噪波标记可生长区，删掉 @mask>0.4 的点 |
| 3. 密度控制 | attribnoise2 → scatter1 | @density | 分形噪波生成密度，scatter1 按密度散布（densityscale=150，relax=10） |

**结果：** 在可生长区域内生成约 1000×150 个种子点，分布疏密有致。

### Stage 3 — 生成主体枝干 ⭐核心

| 步骤 | 节点 | 功能 |
|------|------|------|
| 排序分组 | sort1 → grouprange1 | 为寻路准备 |
| 选起终点 | random_selection1 | 随机选起始点和终止点，写入 beginPts / endPts 组 |
| 构建图网络 | connectadjacentpieces1 | 邻域半径 0.1、锥角 90°、每点最多 1 连接 |
| 最短路径 | findshortestpath1 | Dijkstra/A* 寻路，multiplicity=2（双路径分叉） |
| 清理裁切 | delete_small_parts1 → carve | 删短分支，carve(0.25→0.916) 裁切首尾 |

### Stage 4 — 重建分支线 + 统一方向

For-Each 循环（按 @startpt 迭代，最多 10 条）：

```
resample1 → fuse1 → polypath1 → resample2 → attribpromote1 → attribremap1
```

| 步骤 | 作用 |
|------|------|
| resample1 | 曲线点均匀分布 |
| fuse1 | 融合重合点 |
| polypath1 | 多段线合并为一条折线 |
| resample2 | 再次重采样，保证点数一致 |
| attribpromote1 + attribremap1 | 属性类型提升 + 值重映射 |

**目的：** 每条枝干曲线采样密度一致、朝向统一，为 sweep 做准备。

### Stage 5 — 次级分支

在主枝干上随机选点，复制小分支曲线模板：

| 关键节点 | 功能 |
|---------|------|
| random_selection2 | 随机选附着点 |
| orientalongcurve1 | 计算曲线方向 |
| attribrandomize1 | 随机化分支旋转 |
| copytopoints1 | 将 drawcurve1 模板复制到附着点 |

### Stage 6 — 筛选垂挂部分

将枝干点投影到基底表面，传递法线，检测朝下的点：

```vex
if ( v@N_copy.y < 0 )
{
    @group_hangingPts = 1;
}
```

**结果：** 基底下表面 / 垂直面向下的分支被标记为 `hangingPts` 组。

### Stage 7 — 垂挂分支

在垂挂点上生成朝下的分支，模拟常春藤翻过墙沿垂挂的效果：

| 关键节点 | 功能 |
|---------|------|
| blast3 | 只保留垂挂点 |
| random_selection3 | 随机选 9 条分支 |
| line1 → copytopoints2 | 垂直线段模板复制到垂挂点 |
| mountain1(attribnoise) | 添加噪波弯曲，避免笔直下垂 |

### Stage 8+9 — 枝干3D化 + 叶子粘贴 + 材质输出

**枝干 sweep：**

| 参数 | 值 | 说明 |
|------|----|------|
| radius | 0.019 | 枝干管径 |
| cols | 8 | 环绕分段数 |
| scaleramp | 0→1, 0.183→0.594, 1→0.979 | 根粗末细渐变 |
| endcaptype | 2 | 末端封盖 |

**叶子粘贴（copytocurves1）：**

| 参数 | 值 | 说明 |
|------|----|------|
| incyaw | 29.0° | 叶子环绕枝干的偏航角增量 |
| pitch | 14.0° | 叶子与枝干的夹角 |
| rollper | 4 | 旋转周期 |
| pivot | 1 | 叶柄对齐曲线 |

**叶子模板：** `Pre-made_leaves (Stash)` — 冻结缓存的叶子几何体，通过 copytocurves1 复制到所有枝干。

**材质输出：**

```vex
// vertex_colors (Point Wrangle)
float random_value = rand(@class);
@Cd.g = random_value;
@Cd.b = 1;
```

- `color1` → 枝干基础色 RGB(0.682, 0.433, 0.184) 棕褐
- `connectivity1` → 按连通性分组 @class
- `vertex_colors` → 按 @class 随机绿色调
- `unreal_material` → Unreal Engine 材质通道标记

---

## 四、重点技术解析

### 4.1 三层筛选：从「能不能长」到「长多密」

```
clip1 (几何裁剪)
  → 只保留墙面，去掉地面
  → 回答：这个区域允许生长吗？

attribnoise1 + blast1 (生长遮罩)
  → 粗噪波 @mask，删掉 @mask>0.4 的区域
  → 回答：这个位置适合生长吗？

attribnoise2 + scatter1 (密度控制)
  → 分形噪波 @density，按密度散布种子
  → 回答：这里该长多密？
```

| 层 | 噪波特征 | 设计意图 |
|----|---------|---------|
| 遮罩层 | amplitude=1.0, elementsize=1.0, fractal=关 | 大尺度二元划分：能长 / 不能长 |
| 密度层 | amplitude=1.37, elementsize=0.65, fractal=开(3层) | 细尺度连续变化：疏密渐变 |

**关键区别：** 两层噪波使用不同种子（offset 0 vs 5），互不相关，避免遮罩和密度同频叠加产生规律感。

### 4.2 最短路径枝干生成算法

这是整个 HDA 的核心，用图论方法模拟植物生长：

```
散布种子点
    │
    ▼
connectadjacentpieces1    ← 构建图：邻域半径内连边
    │                        锥角90°限制方向
    │                        每点最多1条连接
    ▼
findshortestpath1         ← 在图上寻路
    │                        beginPts → endPts
    │                        multiplicity=2 → 双路径分叉
    ▼
枝干网络
```

**为什么用最短路径而非随机连接？**

| 方法 | 拓扑 | 自然度 |
|------|------|--------|
| 随机连接 | 网格状，无层级 | 低 — 像蜘蛛网 |
| 最短路径 | 树状，有主干+分支 | 高 — 模拟植物寻找阻力最小路径 |

**connectadjacentpieces1 的参数协同：**

- `searchradius=0.1` + `maxsearchpoints=8` → 只连接近邻，图网络稀疏
- `coneangle=90°` → 避免回头连接（枝干不会绕回自身）
- `maxconnections=1` → 每个点只连一条边，保持树的简单性
- `findshortestpath1 multiplicity=2` → 每对起终点寻 2 条路径，产生自然分叉

### 4.3 枝干渐细：sweep scaleramp 解析

```
t=0.0   → scale=1.0     ████████████  根部：最粗
t=0.183 → scale=0.594   ██████        中段：快速收细
t=1.0   → scale=0.979   ██████████    末端：略回粗
```

这个三段渐变模拟了真实植物枝干的形态：
- **根部粗** — 承载整条枝干的重量
- **中段快速收细** — 远离根部后迅速变细
- **末端略回粗** — 模拟枝端膨大（如节部或花蕾着生处）

### 4.4 垂挂检测：法线方向判定

```vex
if ( v@N_copy.y < 0 )
{
    @group_hangingPts = 1;
}
```

**数据来源链：**

```
原始几何体 → normal1 → attribute1(@N_copy) → attribtransfer1 → select_hanging_parts
                                                        ↑
枝干点 ← ray1(投影到基底) ← resample4/5 ──────────────┘
```

法线 Y 分量 < 0 意味着表面朝下 — 常春藤翻过墙沿后，基底法线翻转，自然触发垂挂分支生成。这是一种**隐式几何语义检测**，无需手动标记。

### 4.5 叶子螺旋分布：叶序模拟

`copytocurves1` 的角度参数组合实现了类似真实植物的叶序排列：

| 参数 | 值 | 作用 |
|------|----|------|
| incyaw | 29.0° | 每片叶沿枝干偏转 29° — 接近黄金角(137.5°)的 1/5 缩放 |
| pitch | 14.0° | 叶片与枝干成 14° 夹角 — 微微外展 |
| rollper | 4 | 每 4 片叶完成一个旋转周期 |
| applyroll | 1 | 启用旋转翻滚 |

**效果：** 叶片不会对生或轮生在同一方向，而是沿枝干螺旋上升，最大化光照面积 — 这正是真实植物叶序的进化优势。

---

## 五、参数速查

| 调什么 | 参数 | 方向 |
|--------|------|------|
| 枝干密度 | densityscale | ↑ 更密 / ↓ 更疏 |
| 枝干长度 | domainu2 | ↑ 更长 / ↓ 更短 |
| 基底精度 | Input_Remeshing | ↓ 更精细但更慢 |
| 叶子大小 | scale | ↑ 更大 |
| 随机模式 | seed | 换值换模式 |
| 叶子差异 | minx / maxx | 收窄→均匀，拉宽→参差 |

---

## 六、性能瓶颈与输出属性

**性能瓶颈：**

| 节点 | 原因 | 建议 |
|------|------|------|
| remeshgrid1 | 高面数输入重网格化慢 | Input_Remeshing 不过小 |
| scatter1 | densityscale=150 + relax=10 | 视情况降低密度或迭代 |
| findshortestpath1 | 大图寻路计算密集 | 控制 seed 点数 |
| sweep1 | 多曲线同时 sweep 面数大 | cols=8 可降为 6 |
| copytocurves1 | 叶子数量多 | 降低 count 或叶子比例 |

**输出属性：**

| 属性 | 来源 | 用途 |
|------|------|------|
| @Cd | vertex_colors | 随机绿色顶点颜色 |
| @unreal_material | unreal_material | UE 材质通道标记 |
| @mask | attribnoise1 | 生长遮罩（调试） |
| @density | attribnoise2 | 散布密度（调试） |
| @startpt | findshortestpath | 枝干路径起点 ID |
| @class | connectivity | 枝干连通性分组 ID |
