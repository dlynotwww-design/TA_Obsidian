---
tags:
  - 面试
  - 技术美术
  - TA
  - PCG
  - Houdini
  - UE5
  - 面经
  - 网易
created: 2026-06-10
target: PCG 方向技术美术
company: 网易上海
salary: 15-25K
---

# PCG 技术美术面试题集

> [!IMPORTANT] 目标岗位：网易上海 — TA搭建PCG管线流程
> 
> 薪资范围：**15-25K** | 工作地点：上海青浦
> 
> 完整 JD 见 → [[岗位JD#上海网易]]
> 
> | JD 要求 | 对应模块 |
> |---------|----------|
> | 搭建标准化 PCG 管线和流程 | [[#🎯 JD 定制一：PCG 管线与流程设计]] |
> | 地形/植被/河流/岩壁 PCG 算法 | [[#🎯 JD 定制二：自然场景 PCG 算法]] |
> | 精通 Houdini 程序化建模 | [[#🎯 JD 定制三：Houdini 深度考察]] |
> | AI 结合 PCG（植被/城市/室内智能排布） | [[#🎯 JD 定制四：AI+PCG 前沿]] |
> | VEX / Python 编程 | [[#🎯 JD 定制五：编程能力]] |
> | Unreal 引擎 + 美术开发流程 | [[#🎯 JD 定制六：UE 与美术流程]] |
> | 美术修养 + DCC 工具 | [[#🎯 JD 定制七：美术与 DCC]] |

---

## 🎯 JD 定制一：PCG 管线与流程设计

> **对应 JD**：「协调开发和美术，搭建标准化的 PCG 管线和流程」

### JD-Q1: 你如何从零搭建一套 PCG 管线？请描述完整流程。

**考察点**：系统性思维、跨部门协调能力、工业化意识

**答题框架**：
```
Phase 1 — 需求对齐
├── 与美术沟通：确定需要程序化的内容范围（地形/植被/建筑/道路）
├── 与程序沟通：确定引擎侧加载方案、性能预算
└── 产出一份「PCG 管线设计文档」

Phase 2 — 工具链搭建
├── Houdini 侧：HDA 模板库（地形生成器/植被散布器/建筑生成器）
├── 引擎侧：UE5 PCG 框架集成 / Houdini Engine 部署
├── 数据格式：定义中间数据规范（JSON/USD/点云）
└── 版本管理：HDA 版本号 + 参数兼容性

Phase 3 — 流程标准化
├── 规范文档：HDA 使用手册 + 参数说明
├── 命名约定：HDA 命名/参数命名/输出命名
├── QA 流程：自动检查（点密度/性能/碰撞）
└── CI/CD：HDA 自动 Cook → 自动导入引擎 → 自动截图对比

Phase 4 — 迭代优化
├── 收集美术反馈 → 调整参数暴露
├── 性能 Profile → 优化 Cook 时间
└── 培训美术使用 HDA
```

### JD-Q2: 跨部门（美术/程序）协作中，遇到过什么矛盾？如何解决？

**考察点**：沟通能力、换位思考、解决问题

**参考思路**：
- 美术要效果、程序要性能 → PCG TA 是平衡点
- 举例：美术想要每棵树都独一无二 → 你通过 Seed 变体+随机缩放，在 5 个基础模型上生成 200 种变体
- 举例：程序说 PCG Cook 太慢 → 你拆分为分块 Cook + 异步加载

### JD-Q3: 如何让美术团队接受并使用你搭建的 PCG 工具？

- 工具易用性：参数少而精，有好默认值
- 即时反馈：Cook 后引擎实时预览
- 文档+培训：录制使用视频，写图文教程
- 先用小范围试点（如只做植被散布），验证效果后再推广

### JD-Q4: 如何评估一个 PCG 管线的质量？

| 维度 | 指标 |
|------|------|
| **效率** | Cook 时间、美术摆放时间节省比例 |
| **质量** | 程序化生成 vs 手摆的视觉差异 |
| **可控性** | 参数覆盖度、艺术家可干预程度 |
| **稳定性** | Cook 成功率、跨版本兼容性 |
| **性能** | 引擎侧 FPS 影响、内存占用 |
| **可维护性** | HDA 节点复杂度、文档完备度 |

---

## 🎯 JD 定制二：自然场景 PCG 算法

> **对应 JD**：「根据需求实现 PCG 相关算法，包括不限于：地形，植被，河流，岩壁等」

### JD-Q5: 设计一套程序化地形生成系统

**必须覆盖的层次**：
```
1. 基础地形
   ├── HeightField Noise（Perlin/Simplex/Voronoi）
   ├── 侵蚀模拟（水力侵蚀/热力侵蚀）
   └── 分层控制：大尺度山脉 → 中尺度丘陵 → 小尺度细节

2. 地形材质
   ├── 基于高度/坡度/曲率的自动分层
   ├──  Height → 雪线以上 = 雪
   ├──  Slope → 陡坡 = 岩壁，缓坡 = 草地
   └──  Curvature → 山脊 = 岩石，山谷 = 泥土

3. 输出到引擎
   ├── Heightmap (16-bit RAW)
   ├── Weight Maps (多图层混合)
   └── Splat Map / Virtual Texture
```

### JD-Q6: 程序化植被散布的核心算法？

**分层散布策略**：
```
Layer 1 — 大乔木（森林骨架）
├── 条件：坡度 < 30°、海拔 200-800m、非水面
├── 算法：Poisson Disk Sampling（保证最小间距）
└── 密度：受湿度/光照 Mask 调制

Layer 2 — 灌木（过渡层）
├── 条件：林缘 + 开阔地边缘
├── 算法：基于乔木位置的边缘填充
└── 聚集度：Clustered Noise

Layer 3 — 花草/地表（填充层）
├── 条件：空地 + 光照充足
├── 算法：纯随机 + Density Noise
└── 避免：排除乔木/灌木/岩石的 Bounds
```

**常见算法对比**：

| 算法 | 适用 | 优点 | 缺点 |
|------|------|------|------|
| **Random** | 花草 | 简单快速 | 可能扎堆 |
| **Poisson Disk** | 乔木 | 均匀不重叠 | 计算量大 |
| **Density Noise** | 过渡 | 自然感强 | 需要调参 |
| **Wang Tiles** | 重复模式 | 无痕拼接 | 预处理复杂 |
| **WFC** | 生态群落 | 满足复杂约束 | 性能开销大 |

### JD-Q7: 程序化河流生成的算法思路？

```
1. 河流路径生成
   ├── 从高海拔 → 低海拔，沿最陡下降方向（梯度下降）
   ├── 支流汇入：多源头 → 汇合 → 干流
   └── 避免局部最小值（Fill Sinks）

2. 河流形态
   ├── 宽度 = f(流量) → 下游更宽
   ├── 曲率 = 自然蜿蜒（Sinuosity）
   └── 河床深度随宽度变化

3. 河流影响区
   ├── 侵蚀带（河流两侧 Deform 地形）
   ├── 植被变化（河岸植被带）
   └── 湿度扩散（影响周围生态）

4. Houdini 实现
   ├── HeightField Flow Field → 流向计算
   ├── Find Shortest Path → 河道路径
   ├── PolyFrame + Sweep → 河道几何体
   └── Attribute Transfer → 湿度/侵蚀属性扩散
```

### JD-Q8: 程序化岩壁/悬崖生成的方案？

```
方案 A — 基于地形坡度
├── 坡度 > 60° → 暴露岩壁材质
├── HeightField Mask by Slope → 岩壁遮罩
├── Copy to Points → 沿岩壁边缘散布碎石
└── 法线扰动 → 岩壁表面细节

方案 B — 程序化岩壁 Mesh
├── 沿样条线生成岩壁带状 Mesh
├── Noise 扰动顶点（增加自然感）
├── 分层：顶部泥土 → 中层岩石 → 底层碎石堆积
└── 支持 LOD 切换
```

---

## 🎯 JD 定制三：Houdini 深度考察

> **对应 JD**：「熟练使用 Houdini，精通程序化建模」

### JD-Q9: 你做过最复杂的 Houdini 程序化建模是什么？详细拆解。

**答题结构**（STAR）：
- **S**：场景需求 → 大世界需要 500+ 变体建筑
- **T**：你的任务 → 用一个 HDA 生成所有变体
- **A**：技术方案 → 模块化设计 + 语法规则 + 随机化
- **R**：结果 → 2 天完成 500 变体，Cook 时间 < 30s/栋

### JD-Q10: HDA 参数设计中有哪些容易踩的坑？

1. **参数爆炸**：暴露太多参数 → 美术不敢用 → 只暴露 5-8 个关键参数
2. **参数耦合**：改 A 导致 B 失效 → 用 Enable/Disable When 条件控制
3. **没有默认值**：空白参数 → Cook 失败 → 所有参数设好默认
4. **不兼容更新**：新版 HDA 改了参数 → 旧场景炸了 → 版本号 + 兼容映射
5. **Cook 超时**：复杂 HDA 每次调参 Cook 10 分钟 → 分 LOD Cook + Cache

### JD-Q11: VEX 实战 — 写一段在高度场上沿等高线散布石块的代码

```vex
// 输入：HeightField + 采样点
// 目标：只在坡度 30°-60° 且等高线密集处放石块

float slope = degrees(atan(@height_slope));  // 坡度（度）
float curvature = abs(@height_curvature);     // 曲率（等高线密度）

// 筛选条件
if (slope > 30 && slope < 60 && curvature > 0.1) {
    @density = 1.0;  // 放置
    // 随机缩放和旋转
    float scale_rand = fit01(rand(@ptnum + 123), 0.8, 1.5);
    @pscale = scale_rand;
    
    vector4 rot = quaternion(rand(@ptnum + 456) * 2 * PI, {0, 1, 0});
    @orient = rot;
} else {
    @density = 0.0;  // 不放置
}
```

### JD-Q12: Houdini 中程序化建模的核心技巧总结

| 技巧 | 说明 |
|------|------|
| **模块化** | 每个 HDA 只做一件事（如"沿样条线放栅栏"） |
| **属性驱动** | 所有逻辑靠 Attribute 传递，不靠硬编码 |
| **Seed 体系** | 统一的 Seed 管理，确保可复现 |
| **Fallback** | 输入不合法时有兜底输出（不报错、不断线） |
| **性能意识** | 用 Mesh Instancer 代替 Copy to Points（万级以上） |
| **文档内嵌** | HDA 的 Help 面板写清楚每个参数的含义 |

---

## 🎯 JD 定制四：AI+PCG 前沿

> **对应 JD**：「探索 AI 结合的 PCG 方案，包括但是不限于：植被，城市等；智能排布如室内、城市和景观等」

### JD-Q13: 你对 AI+PCG 有哪些了解？能具体说说技术方案吗？

**当前主流方向**：

| 方向 | 技术方案 | 应用场景 |
|------|----------|----------|
| **Wave Function Collapse** | 基于约束求解的拼图式生成 | 城市街区、室内布局、像素画 |
| **ML 辅助放置** | 训练模型学习人类摆放偏好 | 植被/装饰物自然散布 |
| **GAN/扩散模型** | 生成高度图/布局图 | 地形草图 → 细化 |
| **LLM + PCG** | 自然语言 → PCG 参数 | 「生成一片松树林」→ 自动调参 |
| **强化学习** | Agent 学习最优放置策略 | 城市道路规划、房间布局 |
| **Neural SDF** | 隐式几何表示 | 有机形态（钟乳石/珊瑚） |

### JD-Q14: 如果让你做一个 AI 智能排布室内家具的系统，你会怎么设计？

```
方案设计：
1. 输入：房间轮廓（Polygon）+ 家具库（3D Model + 语义标签）
2. 约束定义：
   ├── 硬约束：不穿墙、不重叠、门附近留空、动线通畅
   ├── 软约束：沙发面向电视、床头靠墙、餐桌在厨房附近
   └── 美学约束：对称性、视觉平衡、风格统一
3. 算法选型：
   ├── 方案 A：WFC（Wave Function Collapse）— 网格化 + 约束传播
   ├── 方案 B：遗传算法 — 随机放置 → 适应度评分 → 迭代优化
   └── 方案 C：RL（强化学习）— Agent 逐步放置，奖励合理布局
4. 输出：3D 场景（UE 可直接打开）
5. 人工干预：用户可手动拖拽调整，系统自动重新优化周围布局
```

### JD-Q15: WFC（Wave Function Collapse）算法的原理？在 PCG 中怎么用？

```
核心思想：
- 输入：一小块样本（如 4x4 的像素拼图）
- 输出：任意大的、满足相同局部约束的结果

步骤：
1. 提取规则：从样本中学习"什么可以挨着什么"
2. 初始化：每个格子 = 所有可能状态的叠加
3. 迭代：
   a. 选择熵最小的格子（可能性最少的）
   b. 随机坍缩为一个确定状态
   c. 传播约束：更新相邻格子的可能状态
   d. 重复直到所有格子确定或冲突

PCG 应用：
- 2D：像素艺术、Tile Map 地形、室内平面图
- 3D：城市街区（建筑类型分布）、模块化建筑立面
- Houdini 实现：已有 WFC Solver（SideFX Labs）
```

### JD-Q16: 你怎么看待 AI 会取代 PCG TA 这种说法？

**高分答法**：
- AI 是**工具增强**而非替代，类似 Houdini 没有取代建模师
- PCG TA 的核心价值是**理解美术需求 + 设计生成规则 + 平衡质量与性能**，这是 AI 做不到的
- AI+PCG 是**新机遇**：用 AI 加速规则提取、参数调优、自动化质检
- 表达学习意愿：持续关注前沿，不抗拒拥抱新技术

---

## 🎯 JD 定制五：编程能力

> **对应 JD**：「熟悉 VEX，Python」

### JD-Q17: VEX 和 Python 在 Houdini 中各自的适用场景？

| 场景 | VEX | Python |
|------|:--:|:------:|
| 逐点/逐面操作（Wrangle） | ✅ 最佳 | ❌ 太慢 |
| 创建/修改节点网络 | ❌ | ✅ |
| 文件 I/O / 批量处理 | ❌ | ✅ |
| 数学运算 / 噪声 | ✅ | ✅ |
| HDA 参数自动化 | ❌ | ✅ |
| 自定义 Shelf 工具 | ❌ | ✅ |
| 实时 Cook 中的逻辑 | ✅ | ❌ (慢) |

**关键结论**：Wrangle 里用 VEX，管线脚本用 Python，两者互补。

### JD-Q18: 写一个 Python 脚本，批量处理 100 个建筑 HDA 的 Cook 并导出 FBX

```python
import hou
import os

def batch_cook_and_export(hda_path, output_dir, building_count=100):
    """
    批量 Cook 建筑 HDA 并导出 FBX
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # 加载 HDA
    hda_node = hou.node("/obj").createNode(hda_path.split('/')[-1])
    
    results = []
    for i in range(1, building_count + 1):
        try:
            # 设置变体参数（不同 Seed 产生不同建筑）
            hda_node.parm("seed").set(i)
            hda_node.parm("building_height").set(
                hou.hmath.fit01(hou.hmath.rand(i + 100), 3, 15)
            )
            
            # Cook
            hda_node.cook(force=True)
            
            # 导出
            export_path = os.path.join(output_dir, f"building_{i:03d}.fbx")
            rop = hou.node("/out").createNode("filmboxfbx")
            rop.parm("sopoutput").set(export_path)
            rop.parm("execute").pressButton()
            rop.destroy()
            
            results.append({"id": i, "status": "success", "path": export_path})
            
        except Exception as e:
            results.append({"id": i, "status": "failed", "error": str(e)})
    
    # 生成报告
    success = [r for r in results if r["status"] == "success"]
    failed = [r for r in results if r["status"] == "failed"]
    print(f"Done: {len(success)} success, {len(failed)} failed")
    
    hda_node.destroy()
    return results
```

### JD-Q19: `@ptnum` vs `@id` 的区别？

- `@ptnum`：当前帧的点编号，**每帧可能变化**（点被删除/新增后重新编号）
- `@id`：点的**唯一 ID**，跨帧不变（粒子系统中追踪同一粒子）
- PCG 场景：如果要跨多个节点追踪同一个点，用自定义 `@id` 属性，不要依赖 `@ptnum`

### JD-Q20: Houdini 中 `detail()` vs `point()` vs `prim()` 函数的区别？

```vex
// detail() — 读取 Detail（全局）属性
float global_seed = detail(0, "seed");

// point() — 读取指定点的属性
vector pos = point(0, "P", 42);  // 读第 42 号点的位置

// prim() — 读取指定面的属性
int mat_id = prim(0, "material_id", 10);  // 读第 10 号面的材质 ID
```

---

## 🎯 JD 定制六：UE 与美术流程

> **对应 JD**：「熟悉 Unreal 引擎，熟悉游戏美术开发流程」

### JD-Q21: Houdini 内容到 UE5 的完整工作流？

```
Houdini 侧                         UE5 侧
─────────                         ─────
1. 建模/生成                       
   ├── SOP 节点 → 几何体           
   ├── HeightField → 地形          
   └── Point Cloud → 散布点        
                                   
2. 导出策略                        3. 导入/加载
   ├── HDA → Houdini Engine        ├── Houdini Engine Plugin
   ├── FBX/USD → 静态资产           ├── Interchange / Datasmith
   ├── Heightmap → Landscape       ├── Landscape Import
   └── Point Cache → PCG Data      └── PCG Framework
                                   
4. 材质映射                        5. 实例化渲染
   ├── Houdini Material → UE Mat   ├── ISM/HISM 自动合并
   └── Attribute 驱动材质参数       └── PCG Static Mesh Spawner
                                   
6. 迭代                            7. 调优
   ├── Houdini 改参 → 重新 Cook     ├── LOD 自动生成
   └── 引擎侧实时预览               └── Nanite/VT 适配
```

### JD-Q22: 游戏美术开发的完整流程？TA 在哪些环节介入？

```
概念设计 → 原画
    ↓
3D 建模（Maya/Blender/ZBrush）
    ↓  ← TA 介入点①：DCC 工具/脚本加速建模
贴图/材质（Substance/Mari）
    ↓  ← TA 介入点②：智能材质/程序化贴图
绑定/动画
    ↓  ← TA 介入点③：程序化绑定/动画工具
导入引擎（UE/Unity）
    ↓  ← TA 介入点④：自动化导入/材质映射/碰撞生成
场景搭建
    ↓  ← TA 介入点⑤：PCG 程序化场景/HDA 工具
灯光/后处理
    ↓  ← TA 介入点⑥：LUT/后处理材质
性能优化 → 打包上线
    ↓  ← TA 介入点⑦：LOD/合批/Shader 优化
```

### JD-Q23: UE5 PCG 框架中 Surface Sampler 的工作原理？

```
1. 输入：Landscape / Static Mesh 表面
2. 采样：在表面按指定密度生成候选点
3. 属性计算：
   ├── Position（3D 坐标）
   ├── Normal（表面法线 → 可转坡度）
   ├── Density（可被后续节点调制）
   └── Custom Attributes（材质信息等）
4. 筛选：可结合 Point Filter 按属性筛选
5. 输出：传递给 Spawner 生成实际物体
```

---

## 🎯 JD 定制七：美术与 DCC

> **对应 JD**：「良好的美术修养，熟练使用 3D DCC 建模工具，如 Blender/Maya」

### JD-Q24: 你觉得一个好的 PCG 生成结果，美术上应该满足什么标准？

- **自然感**：避免明显的重复模式（通过 Seed 变化 + Noise 扰动）
- **层次感**：大/中/小尺度物体搭配（乔木→灌木→花草）
- **构图感**：疏密有致、视觉焦点、引导线
- **风格统一**：所有程序化内容在同一视觉语言下
- **经得起镜头**：特写没有穿模/浮空/Z-Fighting

### JD-Q25: 如果你发现 PCG 生成的场景某个区域"看起来不对但说不出来"，会怎么排查？

1. **对比参考**：找真实照片/优秀游戏截图做对照
2. **逐层关闭**：关植被 → 关岩石 → 关地表，定位问题层
3. **检查属性**：看该区域的高度/坡度/密度分布是否合理
4. **参数微调**：调 Density Curve、Noise Scale、随机 Seed
5. **加手工修正**：必要时用手绘 Mask 覆盖该区域

### JD-Q26: Blender/Maya 中你最常用的建模技巧？如何辅助 PCG 工作？

- **模块化建模**：按"拼装"思路建模，方便 Houdini 组合
- **命名规范**：Mesh 命名符合 Houdini 解析规则（`Wall_01`/`Window_03`）
- **Pivot 设置**：确保 Pivot 位置适合程序化放置（墙体底部居中、窗户居中）
- **材质 ID**：预分配 Material Slot，方便程序化替换材质
- **LOD 准备**：手动创建或标注 LOD 级别

---

> [!NOTE] 来源
> 内容整理自小红书、牛客网、知乎、Epic 官方文档、Tech-Artists.Org 等渠道，覆盖 2024-2026 年 PCG TA 方向最新面试趋势。
> 内容整理自小红书、牛客网、知乎、Epic 官方文档、Tech-Artists.Org 等渠道，覆盖 2024-2026 年 PCG TA 方向最新面试趋势。

---

## 一、公司真题速览

### 🔷 腾讯光子 — 工具向 TA

- 怎么理解 Houdini 中的 **Instance**？
- 如果不用 Houdini Engine，**如何联动 Houdini 与 UE**？考察点：如何将 Houdini 实例点传入引擎
- 结果：挂得很快（考察深度超出预期）

### 🔷 网易互娱 — 程序向 TA

**笔试** → **一面**，内容覆盖：

- Python 八股（高级特性、底层逻辑）
- Houdini 实操（点云、HDA、属性传递）
- 图形学八股（合批、渲染管线）
- 管线流程理解

### 🔷 莉莉丝 — TA 实习生

- 渲染管线、Forward+/Deferred 区别
- G-Buffer 压缩方案
- 显存带宽概念与优化
- **Houdini 点云与管线流程**
- **USD 管线落地**（高频加分题！）

### 🔷 字节跳动 — 技术美术

- **Boids 算法**动态避障
- Houdini 地形实时交互优化
- 顶点法线变换（切线空间 → 世界空间）
- C++ 能力考察
- USD 管线看法

### 🔷 PCG/程序化方向常见公司

| 公司 | PCG 方向 |
|------|----------|
| 腾讯天美/光子 | Houdini TA、工具链 TA |
| 网易互娱/雷火 | 程序化场景生成、Pipeline TA |
| 米哈游 | 开放世界 PCG、Houdini 大世界 |
| 莉莉丝 | PCG 管线、USD 流程 |
| 叠纸 | 大世界程序化 |

---

## 二、Houdini 核心面试题

### 🔶 2.1 基础概念

> **Q1: 怎么理解 Houdini 中的 Instance（实例化）？**
>
> - Instance 是引用而非拷贝，多个实例共享同一几何体数据，仅存储 Transform 矩阵
> - 在 Houdini 中通过 `instancepath` / `instancefile` 属性控制
> - 引擎侧对应 HISM/ISM 机制，大幅减少 DrawCall 和内存
> - 面试时要能讲清：**属性传递 → 引擎解析 → 实例化渲染** 的完整链路

> **Q2: 如果不用 Houdini Engine，如何联动 Houdini 与 UE？**
>
> - 导出点云/Transform 数据（JSON/CSV/USD）
> - 引擎侧读取数据 + Instance Static Mesh
> - 或用 HDA 烘焙为静态资源导出
> - 考察对 **数据流** 和 **引擎加载机制** 的理解

> **Q3: 怎么对撒点的物体进行随机旋转？**
>
> ```vex
> // VEX: 用四元数给 @orient 随机赋值
> vector4 rot = quaternion(rand(@ptnum) * 2 * PI, {0, 1, 0});
> @orient = rot;
> ```

> **Q4: Houdini 点云（Point Cloud）的理解？**
>
> - 点云 = 带有属性的空间采样点集合
> - PCG 的核心数据载体：每个点携带 Transform、Density、法线、颜色等属性
> - 在 UE PCG 框架中，Point 是最基本的数据单元
> - `pcfind()` / `pcopen()` 用于点云查询，是程序化布局的核心函数

> **Q5: Houdini 管线流程的理解？**
>
> - 讲清楚从 SOP → DOP → VOP → ROP 的数据流向
> - 材质/UV/属性如何在节点间传递
> - **HDA 封装**：参数暴露、版本管理、跨软件协作
> - **引擎端**：HDA 的加载、参数传递、Cook 机制

### 🔶 2.2 实操/设计题

> **Q6: 用 Houdini 程序化生成一片"梯田"风格场景，要求实时加载到 UE5 且内存 < 30MB**

考察思路：

```
HeightField → Remap（梯度分层）
    → Copy to Points 实例化（每层放置石块/植被）
    → Mesh Instancer（替代 Copy，大量 Instance 性能更好）
    → LOD HDA（自动生成多级 LOD）
    → Nanite + Virtual Texture（UE5 内存优化）
```

关键答分点：**实例化优先、LOD 策略、贴图流式加载、不做重复几何体**

> **Q7: Houdini 做好的高度数据/地形层数据如何在客户端加载？**
>
> - HeightField → 导出为 16-bit RAW 或 Texture2D
> - 引擎侧：Landscape Import / Runtime Virtual Texture
> - 分层材质：Weight Map 控制图层混合
> - PCG 框架：基于高度/坡度/曲率驱动植被/岩石散布

> **Q8: Houdini 地形实时交互的优化策略？**
>
> - 分块（Tiling）+ LOD 金字塔
> - HeightField 压缩与解压
> - 仅 Cook 视口可见/编辑区域
> - GPU 加速（OpenCL）的 HeightField 操作

> **Q9: 创建动态破碎玻璃效果的设计思路**
>
> ```
> Voronoi Fracture → 生成碎片
> nParticles → 触发碰撞体
> 碎片属性：@mass, @bounce, @friction
> Noise → 随机化碎片形状
> 导出 Alembic/USD → 引擎播放
> ```

### 🔶 2.3 VEX / Python 编程

> **Q10: VEX 脚本控制属性衰减（如闪电亮度）**
>
> ```vex
> // 基于距离的指数衰减
> float dist = length(@P - chv("center"));
> @Cd = chv("color") * exp(-dist * chf("decay"));
> ```

> **Q11: Python 在 Houdini 中的常用场景？**
>
> - 批量创建/修改节点（`hou.node().createNode()`）
> - HDA 参数自动化（`hou.parm().set()`）
> - 文件 I/O 与管线集成（导入导出批量资产）
> - 自定义 Shelf Tool / 右键菜单
> - 与外部 DCC（Maya/Blender）的数据交换

> **Q12: Python 高级特性八股（高频）**
>
> - 装饰器（`@property`、`@staticmethod`）原理
> - 生成器（`yield`）与迭代器
> - `__init__` vs `__new__` 区别
> - 上下文管理器（`with` 语句 / `__enter__` `__exit__`）
> - GIL 与多线程/多进程

> **Q13: C++ 能力要求（渲染/PCG 方向）**
>
> - 能看懂 UE 源码（至少能 Trace 调用链）
> - 理解 UE 的反射系统（`UPROPERTY` / `UFUNCTION`）
> - 知道如何扩展 PCG 自定义节点（`UPCGSettings` / `UPCGNode`）
> - 智能指针、STL、虚函数机制

---

## 三、UE5 PCG 框架面试题

### 🔶 3.1 核心概念

> **Q14: UE5 PCG 框架的基本原理？**
>
> - **点云驱动**：所有生成基于空间中的采样点
> - **节点化数据流**：类似材质编辑器，数据在节点间流动
> - **图表（PCG Graph）**：定义生成规则的有向无环图
> - **属性系统**：每个点携带 Transform、Density、Bounds、自定义属性
> - **生成器（Spawner）**：在点位置实例化 Static Mesh / Actor

> **Q15: PCG 框架中 Point Density 的含义？**
>
> - 0-1 浮点值，表示该点位置存在生成物的**概率/权重**
> - 被 Filter 节点用于筛除不需要的点
> - Density Noise / Density Remap 用于引入自然随机性

> **Q16: PCG 常用属性（Attribute）有哪些？**
>
> | 属性 | 类型 | 说明 |
> |------|------|------|
> | `$Density` | float | 点密度/概率 |
> | `$Position` | Vector3 | 点位置 |
> | `BoundsMin/Max` | Vector3 | 点的空间范围 |
> | `Color` | Vector4 | 颜色（植被染色、调试） |
> | `Steepness` | float | 陡度（地形坡度） |
> | `Seed` | int | 随机种子 |

### 🔶 3.2 节点分类与用途

> **Q17: UE5 PCG 节点分类体系？每类举例 2 个节点。**

| 类别 | 说明 | 代表节点 |
|------|------|----------|
| **Sampler** | 从空间数据源生成点 | Surface Sampler、Volume Sampler |
| **Filter** | 基于条件过滤点 | Point Filter、By Density Filter |
| **Density** | 影响点密度 | Density Noise、Density Remap |
| **Point Ops** | 影响点和点属性 | Transform Points、Copy Points |
| **Spatial** | 创建空间关系 | Distance、Self Pruning |
| **Spawner** | 在点位置创建资产 | Static Mesh Spawner、Spawn Actor |
| **Subgraph** | 复用图表逻辑 | Subgraph Input/Output |
| **Shape Grammar** | 基于语法规则生成结构 | Spline to Segment、Subdivide Segment |
| **Debug** | 调试辅助 | Print String |

### 🔶 3.3 Shape Grammar（形状语法）

> **Q18: UE5.5+ Shape Grammar 的语法规则有哪些？**

| 符号 | 含义 | 示例 |
|------|------|------|
| `A` | 放置模块 A | `A` |
| `A, B` | A 和 B 放在一起 | `Wall, Window` |
| `*` | 尽可能多地放置 | `Fence*` |
| `+` | 至少一次，然后尽可能多 | `Pillar+` |
| `[A, B]` | 组合放置 | `[Wall, Window]` |
| `[A, B]*` | 尽可能多地组合 | `[Wall, Window]*` |
| `[A, B]2` | 放置指定次数 | `[Wall, Window]2` |
| `{A, B, C}` | 随机排列（可设权重） | `{TreeA, TreeB, TreeC}` |
| `<A, B, C>` | 条件选择（空间够放 A → B → C） | `<BigRock, SmallRock, Grass>` |

**关键 Shape Grammar 节点**：
- `Spline To Segment`：样条线分段
- `Subdivide Segment`：基于语法细分
- `Duplicate Cross-Section`：沿挤出方向复制
- `Select Grammar`：条件选择语法字符串

> **Q19: Shape Grammar 的典型应用场景？**
>
> - 程序化建筑：沿墙体放置窗户、门、装饰
> - 道路系统：路灯、护栏、标线
> - 栅栏/围墙：柱子 + 栏杆 + 装饰
> - 桥梁：桥墩 + 桥面段 + 护栏

### 🔶 3.4 实用技巧

> **Q20: 如何在 PCG 图表中实现层级结构？**
>
> 使用 `CopyPointsWithHierarchy` + `ApplyHierarchy` 节点
> - 先创建父级布局（如建筑基础轮廓）
> - 子级在父级框架内重采样
> - 保留 `$Hierarchy` 属性的层级信息

> **Q21: 如何在地形上检测平坦区域？**
>
> - **Flat Area Detector** 节点
> - 多点采样 + 法线阈值（`NormalThreshold`）
> - 高度阈值（`HeightThreshold`）
> - 输出：标记平坦区域 vs 陡坡区域

> **Q22: 如何让 PCG 生成物面朝特定目标？**
>
> - **LookAt** 节点
> - 设置目标点（通过 `GetActorProperty` 或手动指定位置）
> - 自动调整生成物的 Rotation 朝向目标
> - 适用于：广告牌、路灯朝向道路中心、NPC 面向玩家

---

## 四、性能优化专题

### 🔶 4.1 实例化渲染

> **Q23: HISM vs ISM vs Static Mesh Component 的区别？**

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| **Static Mesh Component** | 单个 Mesh，独立 DrawCall | 少量独特物体 |
| **ISM（Instanced Static Mesh）** | 同材质/Mesh 合并为 1 个 DrawCall | 中等量重复物体 |
| **HISM（Hierarchical ISM）** | ISM + 层级剔除（自动 LOD + Culling） | 大量植被/石头（万级以上） |
| **Foliage System** | 专门优化的植被工具 | 传统植被摆放 |

> **Q24: PCG 中如何实现大量生成时的性能优化？**

核心策略：
1. **HISM/ISM 实例化**：同 Mesh 合并 DrawCall
2. **LOD 系统**：远处用低模/imposter，配合 PCG LOD HDA
3. **分块生成（Chunked Generation）**：按区域懒加载
4. **Cull Distance**：远处不渲染
5. **Nanite + Virtual Texture**：UE5 级别优化
6. **Seed 控制**：同一区域同一种子，避免每次 Cook 全量重置

> **Q25: PCG Actor 为什么比手动 ISM 快？**
>
> - PCG 图表结果可缓存，Cook 后视为静态数据
> - 自动合并同 Mesh/材质到同一 ISM Component
> - 内置空间分区和剔除优化
> - 减少引擎 Tick 开销

> **Q26: 显存带宽的概念与优化？**
>
> - 显存带宽 = GPU 从显存读取数据的速度瓶颈
> - 优化手段：贴图压缩（ASTC/BC）、MipMap 减少采样、减少 G-Buffer 带宽
> - PCG 场景：Virtual Texture 流式加载、减少材质复杂度

### 🔶 4.2 LOD 策略

> **Q27: LOD 系统关键问题？**
>
> - 何时切换 LOD？→ 基于屏幕空间占比（Screen Size）
> - LOD 级数一般多少？→ 3-5 级（含 Imposter/Card）
> - 如何生成 LOD？→ Simplygon / Houdini LOD HDA / 手动
> - LOD 切换时材质/逻辑如何处理？→ 材质实例参数一致，逻辑需额外处理

---

## 五、渲染/图形学交叉考题

> [!TIP] PCG TA 也需要掌握的图形学基础

> **Q28: 渲染管线全流程？**
>
> ```
> CPU应用阶段 → 几何阶段（VS → Tessellation → GS → 裁剪 → 屏幕映射）
> → 光栅化（三角形设置 → 三角形遍历 → FS → 深度/模板/混合）→ 屏幕输出
> ```

> **Q29: Forward+ vs Deferred 区别？G-Buffer 压缩方案？**
>
> - **Forward+**：分 Tile 的光源剔除，适合移动端/VR
> - **Deferred**：先渲染 G-Buffer，再计算光照，适合大量动态光源
> - **G-Buffer 压缩**：BC6H/BC7、降精度（FP16→R8G8B8A8）、Octahedron 编码法线

> **Q30: DrawCall 优化方法？PCG 场景下的合批策略？**
>
> - 静态合批（Static Batching）→ 场景不动的物体
> - 动态合批（Dynamic Batching）→ 同材质小 Mesh
> - GPU Instancing → 大量同 Mesh（PCG 主力方案）
> - SRP Batcher（Unity）/ Auto Instancing（UE）
> - PCG 场景：合理设置 Spawner 的 Mesh 分组，减少材质种类

> **Q31: 顶点法线变换，切线空间 → 世界空间？**
>
> - 法线需要用 Model 矩阵的**逆转置矩阵**变换
> - TBN 矩阵：`[T B N]` 将切线空间向量转到世界空间
> - PCG 中涉及程序化 Mesh 的法线计算

> **Q32: Mipmap 原理？为什么不直接降低贴图分辨率？**
>
> - MipMap = 预计算的贴图金字塔，每级是上一级的 1/4
> - GPU 根据像素在屏幕上的覆盖面积自动选择合适级别
> - 直接降低分辨率 = 远处也采高精度 → 纹理走样（Moire 纹）
> - 三线性插值：相邻两级 MipMap 之间混合

> **Q33: PBR 的核心思想？**
>
> - 基于物理的渲染：能量守恒 + 微表面模型
> - BRDF 三要素：**D**（法线分布）、**F**（菲涅尔）、**G**（几何遮蔽）
> - 金属度/粗糙度工作流 vs 高光/光滑度工作流
> - PCG 场景：程序化生成的材质需要支持 PBR，程序化控制粗糙度/金属度参数

---

## 六、工具链/管线专题

### 🔶 6.1 HDA（Houdini Digital Asset）

> **Q34: HDA 的制作流程？**
>
> ```
> 1. 在 Houdini 中搭建节点网络
> 2. 选择要暴露的参数 → Create Digital Asset
> 3. 定义参数界面（类型、范围、分组）
> 4. 设置 LOD 生成策略（可选）
> 5. 保存 .hda 文件 → 加载到 UE/Unity
> 6. 引擎侧参数联动 + Cook
> ```

> **Q35: HDA 参数暴露的最佳实践？**
>
> - 暴露尽量少的参数（KISS 原则）
> - 参数要有合理的默认值和范围限制
> - 用文件夹/标签组织参数
> - Float 参数配 Slider、Int 参数配下拉菜单
> - 文档化每个参数的含义

### 🔶 6.2 USD（Universal Scene Description）

> **Q36: USD 管线落地有哪些困难？**
>
> - 团队学习成本高（USD 概念复杂）
> - 需要资深 Pipeline TD 主导搭建
> - DCC 间 USD 版本兼容性问题
> - 存量资产迁移成本高
> - 小型团队投入产出比不高
>
> **加分回答**：聊到具体方案（如 UE 的 USD Stage Actor / Interchange）、增量迁移策略、非破坏性编辑工作流

> **Q37: 什么时候选择 USD 管线？**
>
> - 多个 DCC 软件协作（Maya → Houdini → UE）
> - 大型团队并行制作
> - 需要非破坏性编辑和版本管理
> - 程序化场景的中间数据交换

### 🔶 6.3 程序化 vs 手工

> **Q38: 什么时候该用程序化流程 vs 手动制作？**
>
> | 程序化 ✅ | 手工 ✅ |
> |-----------|---------|
> | 重复性高（植被、石头、建筑群） | 一次性 Hero Asset |
> | 变异需求多（大量变体） | 需要精确艺术控制 |
> | 频繁迭代（策划天天改布局） | 独特视觉焦点 |
> | 大世界开放场景 | 过场动画/特写镜头 |
>
> **核心判断**：平衡**开发效率**与**维护成本**，程序化不是万能的

---

## 七、开放题与系统设计

> **Q39: 设计一套 UE5 大世界植被 PCG 系统**

答题框架：
```
1. 数据层：Landscape 高度图 + 材质 Layer Weight Map
2. 采样：Surface Sampler 基于坡度/高度/水距离筛选
3. 密度：Density Noise 引入自然随机 → Density Remap 控制聚集度
4. 种类：By Attribute Filter 分区域 → 不同生态区不同植被组合
5. 变体：Multiple Mesh Spawner + 随机旋转/缩放
6. 层级：大乔木(HISM) → 灌木(ISM) → 花草(ISM)，按距离 Culling
7. 性能：Chunked Generation + Cull Distance + Nanite
8. 艺术控制：暴露 Density/Scale/Variation 参数 + 手绘 Mask 区域
```

> **Q40: 设计一套程序化城市道路系统**

```
1. 道路网络：Spline 定义主干道 → 分支 → 小区路
2. 交叉路口：检测 Spline 交叉点 → 自动放置十字路口 Mesh
3. 沿路生成：Shape Grammar → 路灯/护栏/标线/行道树
4. 建筑区域：道路围合的多边形 → Building Footprint → 程序化建筑
5. LOD：远处建筑用 Box+贴图替代，中距简化立面，近距全细节
6. 变体：Seed 控制街区风格/建筑颜色/高度范围
```

> **Q41: 如何保证 PCG 生成结果的艺术可控性？**
>
> - **参数暴露**：关键参数可调节（密度、缩放、颜色、种子）
> - **Seed 控制**：同一区域同一 Seed = 可重复结果
> - **Mask/Weight Map**：手绘区域控制，程序化 + 手工混合
> - **预制模块约束**：提供边界条件控制随机范围
> - **分层架构**：大结构规则驱动 → 细节随机填充
> - **艺术家反馈循环**：快速迭代 → 调整参数 → 重新 Cook

> **Q42: 开放世界：美术要"电影级体积云 + 60fps"，如何设定性能预算并反推美术规范？**
>
> - 先定总帧预算：60fps = 16.67ms，云不能超过 2-3ms
> - 体积云方案：Volumetric Cloud（UE）+ Temporal Upsampling
> - 反推分辨率：云体积贴图不超过 512³，Ray March Step 优化
> - 美术规范：云层预制 Shape + 最多 2 层叠加 + LOD 切换
> - **PCG 相关**：天空/大气状态也可程序化驱动（时间系统、天气系统）

> **Q43: AI 辅助 PCG 的方向有哪些？**
>
> - **Wave Function Collapse（WFC）**：基于约束的拼图式生成
> - **ML 辅助放置**：训练模型学习人类摆放偏好
> - **PCG + LLM**：自然语言描述 → 参数调整
> - **Neural SDF**：隐式表示用于地形生成
> - **Style Transfer**：参考图 → 程序化参数

---

## 八、编程能力专题

### 🔶 8.1 Python 真题

> **Q44: 装饰器（Decorator）的原理？写一个计时装饰器**

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.3f}s")
        return result
    return wrapper

@timer
def cook_hda(hda_path):
    # HDA Cook 逻辑
    pass
```

> **Q45: 生成器（Generator）vs 列表？何时用生成器？**

```python
# 列表：一次性加载全部到内存
squares_list = [x**2 for x in range(1000000)]

# 生成器：惰性求值，节省内存
squares_gen = (x**2 for x in range(1000000))

# PCG 场景：处理百万级点云数据时用生成器避免 OOM
def iter_pcg_points(pcg_data):
    for point in pcg_data.points:
        if point.density > 0.5:
            yield point
```

> **Q46: `__init__` vs `__new__` 的区别？**
>
> - `__new__`：创建实例（分配内存），静态方法，返回实例
> - `__init__`：初始化实例（设置属性），实例方法，返回 None
> - `__new__` 先调用，`__init__` 后调用
> - 单例模式需要覆写 `__new__`

### 🔶 8.2 C++ 真题

> **Q47: `shared_ptr` 是线程安全的吗？交叉引用问题？**
>
> - 引用计数的增减是**线程安全**的（原子操作）
> - 但 `shared_ptr` 指向的**对象**不是线程安全的
> - 交叉引用（循环引用）导致内存泄漏 → 用 `weak_ptr` 打破循环

> **Q48: 虚函数机制？构造函数能否是虚函数？**
>
> - 虚函数通过**虚函数表（vtable）**实现多态
> - 构造函数**不能**是虚函数（构造时 vtable 尚未建立）
> - 析构函数**应该**是虚函数（确保派生类正确析构）

---

## 九、软技能与职业素养

> **Q49: PCG TA（工具向 vs 内容向），你更喜欢哪个？**
>
> - **工具向 TA**：开发 Pipeline 工具、HDA 资产、自动化流程
> - **PCG 向 TA**：程序化内容生成、规则设计、场景搭建
> - 建议结合自己的实际项目经验回答，展示思考和热情

> **Q50: 介绍一个你做得最满意的 PCG 项目**
>
> - 用 **STAR 方法**：情境 → 任务 → 行动 → 结果
> - 重点讲：**技术方案选择 + 遇到的坑 + 如何解决 + 最终效果**
> - 量化结果（如：生成效率提升 10x，内存节省 40%）

> **Q51: TA 的职责定位：桥梁还是创作者？**
>
> - TA 是**美术与程序之间的翻译器**，但不止于桥梁
> - PCG TA 更是**内容创造者**：设计规则、定义流程、产出可规模化的内容
> - 理解美术需求 → 转化为技术方案 → 交付可用工具 → 持续迭代

---

## 十、备战清单（网易 PCG TA 专用）

### 📋 JD 映射优先级

| 优先级 | 内容 | 对应 JD | 状态 |
|--------|------|---------|:----:|
| ⭐⭐⭐⭐⭐ | PCG 管线搭建思路（从零到一） | 职责 1 | ☐ |
| ⭐⭐⭐⭐⭐ | 地形/植被/河流/岩壁 PCG 算法 | 职责 2 | ☐ |
| ⭐⭐⭐⭐⭐ | Houdini 程序化建模 + HDA 设计 | 职责 3 | ☐ |
| ⭐⭐⭐⭐⭐ | VEX 常用函数 + Wrangle 实操 | 要求 1 | ☐ |
| ⭐⭐⭐⭐⭐ | Python 脚本（批量 Cook/管线自动化） | 要求 1 | ☐ |
| ⭐⭐⭐⭐ | UE5 Houdini Engine 工作流 | 要求 2 | ☐ |
| ⭐⭐⭐⭐ | AI+PCG（WFC/ML/智能排布） | 职责 4 | ☐ |
| ⭐⭐⭐⭐ | 游戏美术开发全流程 | 要求 2 | ☐ |
| ⭐⭐⭐ | Blender/Maya 建模 + 美术修养 | 要求 3 | ☐ |
| ⭐⭐⭐ | 渲染管线 + PBR（通用基础） | 要求 2 | ☐ |
| ⭐⭐⭐ | 跨部门沟通 + 流程文档能力 | 要求 4 | ☐ |
| ⭐⭐ | HISM/ISM 性能优化 | 要求 2 | ☐ |

### 🎨 为这个 JD 量身准备的作品

> 核心思路：展示"搭管线"的能力，而非单个效果

| 作品 | 说明 | 打动面试官的点 |
|------|------|---------------|
| **Houdini → UE 全链路 Demo** | 一个 HDA 控制地形+植被+河流 | 证明你懂完整管线 |
| **HDA 工具包（2-3个）** | 建筑/栅栏/植被散布，含文档 | 证明你有工业化意识 |
| **AI+PCG 实验** | WFC 城市布局 / 智能室内排布 | 证明你有探索精神 |
| **Bledner/Maya 模型作品** | 展示你手工建模的质量 | 证明你有美术修养 |
| **Python 管线脚本** | 批量 Cook + 导出 + 报告 | 证明你有编程能力 |

### 🔥 面试时一定要主动提的关键词

- "管线标准化" → 说明你理解工业化的价值
- "美术可控性" → 说明你不只追求技术炫技
- "AI+PCG" → 说明你跟上了 JD 的前沿方向
- "性能与质量平衡" → 说明你有工程思维
- "跨部门协作" → 说明你有软技能意识

### ⚡ 面试可能挖的坑（提前准备）

1. "你这个 Demo 换个引擎（Unity）还能用吗？" → 回答管线设计的通用性
2. "如果美术不买账你的 HDA，怎么办？" → 回答工具易用性+培训
3. "AI 做出来的东西没法微调怎么办？" → 回答人工干预+参数暴露
4. "你做的东西和直接手摆有多大差距？" → 回答质量控制+手摆对比
5. "性能扛不住怎么办？" → 回答 LOD+分块+实例化

---

> [!TIP] 配合使用
> 通用 TA 面试基础知识（渲染/图形学/数学）请参考 [[面试经验]]

> [!success] 网易 JD 已全部覆盖
> 7 条 JD 要求 → 7 个定制模块 → 26 道 JD 直出题 + 51 道通用 PCG 题 = **共 77 题**
> 
> 完整 JD 见 → [[岗位JD#上海网易]]
