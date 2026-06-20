---
tags:
  - UE5
  - 美术问题
  - 排查指南
  - TA
  - 工作规范
created: 2026-06-18
related:
  - "[[UE5游戏项目流程|UE5游戏项目流程]]"
  - "[[场景大世界管线详解|场景大世界管线详解]]"
  - "[[游戏3D场景模型制作规范|游戏3D场景模型制作规范]]"
  - "[[01_项目文档/盘丝洞性能优化|盘丝洞性能优化]]"
---

# UE 游戏开发常见美术问题及解决方案

> 系统梳理 UE 项目中美术日常遇到的高频问题：现象 → 原因 → 解决方案。可作为新项目 onboarding 手册和 TA 支持速查表。

---

## 一、模型与资产导入

### 1.1 FBX 导入后模型缩放/旋转不对

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 模型导入后巨大或极小 | DCC 单位与 UE 单位不一致（Max 默认英寸，Maya 默认厘米，UE 是厘米） | Max：导出 FBX 时设置单位为**厘米**，或导入 UE 时 Scale Factor = 1.0 |
| 模型导入后旋转 90° | Maya Y-up ↔ UE Z-up 轴差异 | FBX 导出时勾选"Z-up"或导入 UE 时勾选"Force Front XAxis" |
| 模型中心点偏移到远处 | 模型内有游离顶点/空物体 | DCC 中清理空物体、合并游离点，Reset XForm |

### 1.2 导入后材质球丢失或多出一倍

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| FBX 导入后材质球全是 Default | 材质命名与 UE 内不一致 | 确保 DCC 材质球命名与 UE 内材质路径一致，或用导入设置中的材质映射表 |
| 材质球数量翻倍，出现 `_Inst` 后缀 | Max 多维子材质被拆成独立材质 | 检查 Max 中的材质 ID 分配是否合理，避免不必要的多材质球 |
| `_Inst` 材质每次导入都新建 | 引擎无法匹配已有材质 | 手动指定 Import Material，或写 Python 脚本批量替换 |

### 1.3 碰撞不生效

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 角色直接穿过物件 | 未生成碰撞 | 导入时勾选"Generate Collision"，或手动添加 Box/Convex 碰撞 |
| 碰撞偏移/错位 | 碰撞体没跟模型一起 Reset XForm | DCC 中先 Reset XForm 再导出碰撞 |
| `UCX_` 前缀不识别 | 碰撞网格必须是**凸包**（Convex），凹面不会被识别 | 将凹面拆分为多个凸包网格，分别命名 `UCX_name_00`、`UCX_name_01` |

---

## 二、材质与贴图

### 2.1 场景贴图变糊（Texture Streaming Pool 溢出）

**这是 UE 使用中最常见的问题之一。**

> ⚠️ **警告**：很多教程让你直接调大 `r.Streaming.PoolSize`，这只是掩盖问题——低配机器的玩家依然会看到糊掉的贴图。**先审计，再扩容。**

#### 根因诊断流程

```
Tools → Audit → Statistics → Texture Stats
→ 按 Current Memory 排序 → 锁定占用最大的贴图
→ 控制台 stat Streaming → 查看当前池使用量和 Overbudget 状态
```

#### 逐项排查表

| 检查项 | 标准 | 不通过的后果 | 修复 |
|--------|------|-------------|------|
| **贴图是 2 的幂次方** | 每边必须是 1/2/4/8...4096/8192 | 无法生成 Mipmap → 全分辨率常驻 VRAM | 外部软件 Resize 后重新导入 |
| **Mip Gen Settings** | `FromTextureGroup` | 无 Mip → 始终加载全分辨率 | 纹理编辑器 → Level Of Detail → Mip Gen Settings |
| **Never Stream** | **false**（不勾选） | 绕过流送池，全分辨率常驻 VRAM | 纹理编辑器 → Level Of Detail → Advanced → 取消 Never Stream |
| **压缩格式** | BC1/BC3(颜色) / BC5(法线) / BC6H(HDR) | 未压缩贴图显存占用暴增 | 纹理编辑器 → Compression → 按类型选择压缩 |
| **Maximum Texture Size** | 按物件实际需求设置上限 | 4K 贴图用在远处小石头上 | 纹理编辑器 → Compression → Advanced → 设置合理上限 |

#### 关键控制台变量

| CVar | 作用 | 建议 |
|------|------|------|
| `r.Streaming.PoolSize` | 流送池大小 (MB) | **最后手段**才调大，量力而行（参考 VRAM 总量） |
| `r.Streaming.MipBias` | 全局 Mip 偏移 | 设为 0，配合 `UsePerTextureBias` 逐贴图控制 |
| `r.Streaming.UsePerTextureBias 1` | 允许逐贴图 Mip 偏移 | 推荐开启，精细控制 |
| `r.Streaming.LimitPoolSizeToVRAM 1` | 自动限制池大小 ≤ 可用 VRAM | 推荐开启 |
| `r.Streaming.FullyLoadUsedTextures 0` | 不预加载全 Mip | 推荐关闭（打包后），节省内存 |

#### UE 5.5.x 已知 Bug：贴图随机变黑

UE 5.5.0-5.5.3 存在流送/渲染同步 bug，材质随机变黑。临时修复：
- 切换 `r.Streaming.FullyLoadUsedTextures 1` 再切回 `0`
- 打开变黑的贴图资产 → 编辑器自动刷新 → 暂时修复
- 切换到**虚拟纹理（Virtual Texture）**据报告可完全规避
- 更新 GPU 驱动（部分用户反馈有效）

#### Quixel / MegaScans 特别提醒

Quixel 资产常附带 8K 贴图。导入后务必：
- 手动设置 `Maximum Texture Size` = 2048 或 1024
- 或从 Bridge 下载时选择较低品质

### 2.2 Normal Map 方向反了（DirectX vs OpenGL）

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 模型表面光影反向——凹陷变凸起 | UE 使用 **DirectX 格式**（Normal Y 通道向下），Maya/Substance 默认导出 OpenGL（Y 通道向上） | ① Substance Painter 导出设置选择 **DirectX**<br>② 或 UE 材质中翻转 Normal 贴图的 **G 通道**（Green Channel Invert）<br>③ Maya 烘焙：导出到 UE 不需翻转 Y；导出到 Unity 需翻转 Y |
| 同一张贴图在不同引擎效果不同 | Unity 用 OpenGL/Y+，UE 用 DirectX/Y- | **在 SP 导出时针对引擎选择正确格式**，不要在引擎内手动翻转（容易遗漏） |

### 2.3 虚拟纹理（Virtual Texture）导致材质异常

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 地形材质出现黑色块/闪烁 | 官方地形/植被材质默认启用 VT，自定义材质未配置 VT 支持 | 自定义材质如需 VT 兼容，需添加 `VirtualTexture` 节点并配置 `Runtime Virtual Texture Output` |
| 普通材质与 VT 材质混合出现 bug | VT 材质和非 VT 材质在同一个物体上混用导致采样冲突 | 检查母材质是否有隐式 VT 依赖。地编自己做的小物件材质**不需要 VT**，避免额外开销 |

### 2.4 半透明材质渲染顺序错误

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 半透明物体后面的物体消失了 | 半透明不写入深度缓冲（Depth Buffer），渲染顺序由 Translucency Sort Priority 决定 | 调整材质中的 **Translucency Sort Priority**（数值越大越优先渲染） |
| 多层半透明叠加变黑/变白 | 多次 Alpha Blend 叠加超出范围 | 减少半透明层数，或用 **Translucent Additive** 替代 `Translucent Default` |
| 半透粒子与不透明物体穿插 | 粒子排序依赖距离和 Priority | Niagara 中设置 `Sort Order`、材质中调 Priority |

### 2.5 材质属性未连接却显示异常

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Base Color 没连但模型有颜色 | 材质实例继承了**默认值**（灰色 0.5），这个值在实例面板不可见 | 母材质中为所有可覆盖属性设置合理的默认值，不要留 UE 默认值 |
| 材质实例调了参数无效 | 母材质未将参数声明为 **Static Switch Parameter** 或参数名不匹配 | 检查母材质中参数命名是否与实例中一致，Static Switch 需要 `Switch Parameter` + `Static Bool Parameter` 配套 |

---

## 三、Nanite

> Nanite 是 UE5 标志性技术，但对植被/透明材质/特定材质节点的兼容性仍是高频踩坑区。

### 3.1 WPO（World Position Offset）风动 × Nanite 底层冲突

**WPO 与 Nanite 在架构层面是对立的：**

| 问题 | 说明 |
|------|------|
| **强制保守剔除** | WPO 迫使 Nanite 使用超大 Cluster 包围盒 → 大量误判为可见 → Overdraw 暴增 |
| **逐顶点计算** | WPO 在顶点着色器中逐顶点计算，绕开 Nanite 的固定函数光栅化快车道 |
| **材质不兼容** | 每个使用了不同 WPO 的材质 = 独立的 GPU Dispatch → 多材质时性能急剧下降 |

**兼容性矩阵（截至 UE 5.6）：**

| Mesh 类型 | Nanite | WPO | 光追阴影 | 状态 |
|-----------|--------|-----|:---:|------|
| Static Mesh | ✅ | ✅ | ✅ | 5.6+ 支持 |
| Instanced Static Mesh | ✅ | ❌ | ✅ | 正常 |
| Instanced Static Mesh | ✅ | ✅ | ❌ | **不支持** |
| Foliage Tool 笔刷 | ✅ | ✅ | ❌ | **Bug UE-314241** |

### 3.2 UE 5.6 已知 Bug：Nanite 树 + Foliage Tool + WPO = 无阴影

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Foliage Tool 笔刷放置的 Nanite 树（开启 WPO 风动）不投射任何阴影 | 引擎 Bug（UE-314241），Foliage Tool 生成的 ISM + WPO + 光追阴影三角组合不兼容 | ① **手动拖入关卡**（不用 Foliage Tool）→ 阴影正常<br>② 关闭 Nanite → 传统 LOD + CSM 阴影<br>③ 关闭 Directional Light 的光追阴影<br>④ 尝试 `r.RayTracing.Geometry.InstancedStaticMeshes.EvaluateWPO 1` |

### 3.3 UE 5.7+ 新方案：Nanite Foliage + Skeletal Mesh 风动

Epic 推荐的新方向——**不再用 Static Mesh + WPO 做风动**，改为：

```
Nanite Foliage 工具（5.7+ 实验性）
├── 骨骼层级（Bone Hierarchy）驱动风动 —— 替代 WPO
├── 保持在 Nanite 固定函数光栅化快车道
├── 100,000 骨骼同时更新仅 ~0.1ms GPU
├── 屏幕占比过小时自动停止动画
├── 兼容 Voxel 和 Virtual Shadow Maps
└── 与 Foliage Tool 正常协作
```

### 3.4 Nanite 植被拉远后消失

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 开启 Nanite 的植被拉远一定距离后整片消失 | Nanite 对远距离小三角形的剔除过于激进 | ① 增大资产的 **Bounds Scale**（Static Mesh Editor → Details → Bounds Scale）<br>② 设置 `r.RayTracing.Geometry.InstancedStaticMeshes.Culling 0`（光追阴影下） |

### 3.5 Nanite 表面出现错误的阴影/黑斑

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Nanite 模型表面出现三角形黑斑 | 光追阴影 + Nanite 的兼容问题 | ① `r.RayTracing.Nanite.Mode 1`（默认 0）<br>② `r.RayTracing.Shadows.EnableTwoSidedGeometry 0`（双面几何体导致阴影错误时） |
| Nanite 模型阴影锯齿严重 | 非 Nanite 几何体的虚拟阴影贴图法线偏移默认值过低 | `r.Shadow.Virtual.NormalBias 1`（默认 0.5） |

### 3.6 Nanite Landscape 问题（5.6）

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 5.6 中 Nanite Landscape 材质异常 | 5.6 引入的 Nanite Landscape 与某些材质节点不兼容 | 检查材质是否有不兼容节点；临时回退到非 Nanite Landscape |

### 3.7 如何确认 Nanite 是否真的生效

| 检查方法 | 操作 |
|---------|------|
| **材质兼容性** | 打开材质 → Details → `Usage → Used with Nanite` 是否 ✓ |
| **视口可视化** | 视口 → `Nanite Visualization` → `Triangles` / `Clusters` |
| **Mesh 设置** | Static Mesh Editor → Details → `Nanite` → `Enabled` = true |
| **回退提示** | 控制台可能有 `Nanite disabled for mesh X because material Y is incompatible` 日志 |

---

## 四、光照与阴影

### 4.1 Lightmap 烘焙问题

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 烘焙后模型出现黑斑/光斑 | ① UV2 有重叠<br>② UV2 间距不足<br>③ Lightmap Resolution 过低 | ① 检查 UV2：**不能有任何重叠**<br>② UV2 间距保持 2-4 像素（512 精度）<br>③ 增大 Lightmap Resolution（但会增加烘焙时间和内存） |
| Lightmap 接缝处有黑线 | UV2 切断位置在视觉直视面 | UV2 断开必须在朝下或内侧部分，**禁止在视觉焦点处断开** |
| Commandlet 批量烘焙结果与编辑器内不一致（5.5.4） | Swarm Cache 被 Commandlet "污染" | 清空 `%APPDATA%\Local\UnrealEngine\5.5\Saved\Swarm`，先在编辑器内烘焙一次以正确种子缓存 |
| **Baked Light + Lumen 同时开启** | Lumen 在运行时会丢弃已烘焙的 Lightmap——**烘焙白做了** | 如果用 Lumen → 不要烘焙；如果需要烘焙 → 关闭 Lumen 改用传统 GI |
| ISM 的 Lightmap 质量极低（5.4/5.5） | ISM 只采样最低分辨率 Lightmap Mip | 5.6+ 部分修复（Vulkan）；PC 端建议不用 Lightmap + ISM 组合 |

### 4.2 Lumen 特定问题

#### 4.2.1 Hardware Lumen — Nanite 表面黑斑（5.6+ Bug UE-316311）

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Hardware Lumen 下 Nanite 几何体表面出现黑色/斑块伪影 | Nanite 光追代理几何体与世界位置重建的 Surface Cache 不匹配，阴影/辐射度射线击中了 Mesh 自身表面 | ① 关闭该资产的 Nanite（消除问题）<br>② Nanite LOD 偏差：`Max Edge Length Factor = 3`（减轻）<br>③ 调整射线偏差：`r.LumenScene.DirectLighting.HardwareRayTracing.ShadowRayBias 9`<br>④ `r.LumenScene.Radiosity.HardwareRayTracing.SlopeSurfaceBias 5` |

#### 4.2.2 UE 5.6 Diffuse Color Boost 回归

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 即使 Diffuse Color Boost 值低至 1.2，方向光过度增亮，反射破坏，低光场景出现过饱和溢色 | 5.6 的"修复"错误地将间接光照强度 & Diffuse Color Boost 应用到**反射 Hit-Lighting**（不应影响反射），同时缓存光照预曝光范围被移动（-4→24 EV） | 恢复 5.5 行为：<br>① `r.Lumen.CachedLightingPreExposure 0`<br>② `r.SkyLight.RealTimeReflectionCapture.PreExposure 0`<br>Epic 已确认需要正确修复 |

#### 4.2.3 Lumen 反射中的物体变暗/消失

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 镜面/反射面在特定角度显示暗色或不正确的材质 | 物体对 SSR 可见但不在 Lumen Scene / 光追场景中（物体离开屏幕时消失） | ① 切换视图模式 → **Lumen Overview** → 粉色/黄色表示 Lumen Card 不足<br>② PP Volume 中启 用 **Include Translucent Objects**<br>③ 确保 Mesh 生成合适的 Lumen Card |
| Lumen 反射中出现黑色块 | 屏幕空间追踪（Screen Trace）被遮挡后无回退 | `r.Lumen.Reflections.HierarchicalScreenTraces=1` 启用分层追踪；室内场景考虑混合使用 **Reflection Capture** |

#### 4.2.4 Lumen + 风格化美术的固有冲突

| 问题 | 说明 |
|------|------|
| Lumen 动态阴影本质上有噪点 | **必须依赖 TAA/TSR 降噪** → 边缘模糊 → 与干净风格化/绘画风美学冲突 |
| 锐化后处理会重新引入伪影 | 无解——要么接受噪点，要么接受模糊 |
| **唯一完整的替代方案** | 放弃 Lumen → 全烘焙光照 + CSM/距离场阴影 → 干净、锐利、无噪点的阴影 |

#### 4.2.5 Lumen 闪烁/大像素阴影快速诊断

依次尝试以下 CVar（注意：这些会降低质量，仅用于排查）：
- `r.Lumen.Reflections.HierarchicalScreenTraces 0`
- `r.Lumen.Reflections.HighQuality 0`
- `r.Lumen.ScreenProbeGather.ScreenTraces 0`
- `r.Lumen.Reflections.ScreenTraces 0`
- `r.Shadow.Virtual.OnePassProjection.MaxLightsPerPixel 64`
- 同时检查：关闭 Nanite、验证 Mesh 法线方向、禁用 Hardware Ray Tracing 对比

### 4.3 动态阴影问题

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 植物阴影出现黑色实心方块 | 光追阴影 + 植物透贴面的法线偏移不足 | `r.RayTracing.NormalBias` 提高（如 0.1 → 0.5），解决光追植物黑斑 |
| 远景阴影丢失 | 阴影距离不够 | `r.Shadow.DistanceScale=2`（默认 1，加倍阴影绘制距离） |
| 小物件阴影消失 | 阴影面积阈值剔除（小于某面积自动关阴影） | `r.Shadow.RadiusThreshold` 降低（默认 0.03，设为 0 关闭剔除） |
| 非 Nanite 物体远距离阴影不正常 | 远阴影剔除策略与 Nanite 不同 | `r.Shadow.Virtual.UseFarShadowCulling 0` |

### 4.3 多灯光叠加问题

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 场景某区域出现红色 X 标记 | **Stationary Light 重叠超过 4 盏**——第 5 盏被强制转为动态光，消耗暴增 | ① 用 Light Complexity View（Alt+7）检查重叠<br>② 减少 Stationary Light 数量，或缩小其影响范围（Attenuation Radius）<br>③ 不重要的补光改为 Static（烘焙） |
| 动态光太多导致帧率暴跌 | 动态光性能消耗排序：静态 < 固定 < 动态。每盏动态光都增加 Shadow Pass | ① 用 Light Complexity View 定位问题区域<br>② 优先降级为 Stationary/Static<br>③ 统一使用 Light Function 而非多盏灯 |

---

## 五、性能问题

### 5.1 DrawCall 过高

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| `Stat SceneRendering` 显示 DrawCall 远超预算 | 大量独立材质/独立 Mesh 未经合批 | ① **ISM/HISM**：重复物件统一用 Instance 渲染（5000 棵树 = 1 DrawCall）<br>② **Merge Actors**：相邻的静态 Mesh 手动合并<br>③ **打包型关卡 Actor**（UE5 新功能）：优化 DrawCall 合批 |
| 植被 DrawCall 爆炸 | 每种树/草/灌木各自独立渲染 | 同一物种合并为 HISM、设置合理的 Cull Distance 减少远处绘制 |
| PCG 生成后 DrawCall 超预算 | HISM 合并阈值设置不合理 | Phase F 闭环：生成 → `stat SceneRendering` → 调高 HISM 合并阈值 → 重生成 |

### 5.2 半透明材质导致的 Overdraw

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Shader Complexity 视图（Alt+8）显示大片粉白色 | 半透明材质不参与深度写入，每层都叠加渲染 | ① 减少半透明面积：草/树叶模型用更紧凑的 Mesh 包裹透贴<br>② 大面积贴花用 Plane 而非粒子<br>③ 植被 LOD 近处用更多面减少透贴空白，远处直接换 Impostor |
| 粒子特效导致 GPU 炸 | 大量半透明粒子叠加 | 控制粒子总数、使用 GPU Scene 粒子模式、减小粒子屏幕占比 |

### 5.3 Shader 复杂度过高

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Shader Complexity 视图中某材质发白 | 像素着色器指令数（Pixel Shader Instruction Count）过高 | ① 环境物件材质目标：**150-200 指令**<br>② 优先用 **Static Switch Parameter** 而非 `If` 节点（If 会并行执行两条路径）<br>③ 用贴图查表替代复杂数学运算<br>④ 合并 R/G/B/A 通道：4 张灰度图 → 1 张 RGBA 贴图 |
| 材质中有大量 Texture Sample | 每次采样都有开销 | 合并通道、减少不必要的采样、共用贴图 |

### 5.4 Texture Memory / VRAM 过高

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 场景 VRAM 占用超 2.5GB | 过多 4K 贴图、未压缩、未 Mipmap | ① 审计：小物件不需要 4K，降为 1K/512<br>② 非关键贴图用 **BC 压缩**（DXT5/BC7）<br>③ 启用 **Virtual Texture**（RVT）流式加载地形贴图<br>④ 关闭不必要的贴图 Mip（默认都保留） |

---

## 六、PCG / Houdini 管线

### 6.1 PCG Graph 生成无结果 / 输出为空

> ⚠️ 2025 年 Epic 论坛高频问题。

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 节点 Debug 显示有 Point 但 Spawner 无实例 | GPU 执行标志冲突：`StaticMeshComponentPropertyOverride` 在 **ExecuteOnGPU = true** 时静默失败 | 关闭相关节点的 `Execute on GPU`，或将 GPU 不兼容节点移到 CPU 分支 |
| Graph 在 PCG Volume 中正常，嵌在 Blueprint 中无输出 | Blueprint PCG Component 缺少正确的 World 引用/Generation Trigger | ① 检查 PCG Component 的 Generation Trigger 设置<br>② 确保 `Generate on Load` 或手动触发<br>③ 关闭 World Partition 的异步加载测试对比 |
| UE 5.6 升级后 `GetActorData` + `Difference` 节点不再移除 Point | 5.6 的 `GetActorData` 默认 Mode 变了 | 显式设置 `GetActorData` → `Mode = GetSinglePoint`（或你需要的模式） |
| 散布物体全部不在预期位置 | Surface Sampler 的 Target Landscape 未设置或设置错误 | PCG Graph 中确保 `Get Landscape Data` 或 `Surface Sampler` → Landscape 输出正确连接 |
| 散布密度忽高忽低 | Seed 不同或 Density Filter 参数漂移 | ① 使用固定 Seed 确保可复现<br>② PCG Data Asset 中锁定关键参数，防止误操作 |
| ISM 不生效（每个物体仍是独立 Actor） | 未设置 ISM/HISM 或合并条件不满足 | 确认 `Static Mesh Spawner` 的 Instance Settings 中合并阈值正确，同类 Mesh 距离在合并范围内 |

### 6.2 PCG Graph Debug 快速诊断

| 操作 | 作用 |
|------|------|
| 在节点上按 **D** | 显示该节点的 Debug 可视化——检查 Point 是否真的生成了 |
| 在节点上按 **A** | 显示 Point 属性面板——检查 `Mesh`/`StaticMesh` 属性是否正确赋值 |
| 控制台 `pcg.FlushCache` | 清除 PCG 缓存后重新生成 |
| 临时关闭 World Partition | 隔离 WP 流式加载导致的问题 |

### 6.3 Runtime PCG 再生成失效（World Partition）

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 运行时删除 PCG 生成的 ISM（砍树）→ 喂入 Difference 节点 → 不触发再生成 | WP Grid Actor 卸载/重载后 ISM 重新出现，输入变更未触发重新执行 | ① **不要断开 PCG Blueprint 节点的 Source 输入**——保持直通即使不处理<br>② 关闭 PCG Component 的 `Force Generation`<br>③ `pcg.FlushCache` 刷新 |

### 6.4 Spline Mesh → 后续采样失败

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| `Spawn Spline Mesh` 后用 `Copy Points` 采样生成的 Spline Mesh 表面无输出/偏移错误 | `Spawn Spline Mesh` 输出的是 **PolyLine Data** 而非 Point Data，无法直接获取 Mesh 表面点 | ① 换用 **Spline Sampler → Projection** 对原始 Spline 做地表投影<br>② 用 **Surface Sampler** 对代理表面采样<br>③ 复杂几何体场景考虑 Blueprint / C++ Raycast |

### 6.5 NavMesh 不更新

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| PCG 生成的 ISM 不被 NavMesh 识别 | PCG 生成后不会自动触发 NavMesh 重建 | ① 生成完成后手动触发 **NavMesh Rebuild**<br>② Blueprint 中复制 ISM Component 触发 NavMesh 注册 |

### 6.6 HDA Cook 失败

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| HDA 在 UE 内 Cook 后无输出 | ① 输入曲线/地形无效<br>② HDA 内部参数设置冲突<br>③ Houdini Engine 版本不匹配 | ① 检查 HDA 输入是否正确（Spline 是否闭合、Landscape 是否已加载）<br>② 在 Houdini 中单独 Cook HDA 验证逻辑<br>③ 确保 UE Houdini Engine 插件版本与 HDA 创建时的 Houdini 版本一致 |
| 反复 Cook 导致 UE 卡死 | HDA 输出量过大或无限循环 | 为 HDA 添加**复杂度上限**（最大建筑数、最大点云数），避免误操作导致爆炸式生成 |

### 6.7 Houdini → UE 属性丢失

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 颜色/缩放/变体信息没传递过来 | Houdini Point 属性（`unreal_instance`、`scale`、`color` 等）命名不规范或未导出 | ① 检查 HDA 导出属性命名是否符合 UE 规范<br>② Python 导出脚本确认属性写入 JSON 或直接写入 FBX 元数据<br>③ 检查 PCG Data Table 映射是否完整 |

### 6.8 PCG ISM 消隐异常（Cull Distance Bug）

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| UE 5.5+ 中 PCG 散布的植被/物件在很近距离就消失 | Static Mesh 上的 Cull Distance 设置在 PCG/Foliage 中行为异常 | 检查 Static Mesh 的 Cull Distance 设置，临时将 Cull Distance 设为 0 测试是否恢复 |

---

## 七、场景 / 关卡

### 7.1 场景迁移后关卡不显示

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 迁移过来的关卡空白 | 目标项目**未启用所需插件** | 检查源项目使用的插件（如 PCG、Houdini Engine、Landmass 等），在目标项目启用 |
| 迁移后材质丢失 | 材质路径不同 | 使用 UE 迁移工具（右键 → Asset Actions → Migrate）而非手动复制，它能自动处理依赖 |

### 7.2 持久关卡/主关卡无法编辑

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 持久关卡（Persistent Level）锁定 | World Partition 项目中持久关卡是只读的 | 在**子关卡**（Data Layer / OFPA 文件）中编辑，持久关卡只做总览和组织 |

### 7.3 场景崩溃

| 常见崩溃原因 | 解决方向 |
|-------------|---------|
| VRAM 爆显存 | 降低贴图分辨率，减少同时加载的资产量 |
| 无限循环（蓝图/Houdini Cook） | 写保护条件或超时机制 |
| 插件冲突 | 逐一禁用排查；更新到与引擎版本匹配的插件版本 |
| Nanite 某些资产崩溃 | 暂时禁用该资产 Nanite，排查是否因 WPO/特殊材质节点触发 |

---

## 八、植被

### 8.1 Foliage Tool 阴影不跟随风动

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| Foliage Tool 笔刷的植被开启 WPO 风动后，树枝/叶片在动但**阴影不动** | 阴影 Pass 没有正确读取 WPO 后的顶点位置 | ① 确保 Directional Light 的 **Ray Traced Shadows** 开启<br>② 检查 `r.RayTracing.Geometry.InstancedStaticMeshes.EvaluateWPO 1`<br>③ 如果使用 CSM（Cascaded Shadow Maps）：已知 Bug，`r.Shadow.LODDistanceFactor` 未正确考虑 WPO |
| Nanite 树 + Foliage Tool + WPO = 完全不投射阴影 | Bug UE-314241（详见 [[#3.2 UE 5.6 已知 Bug：Nanite 树 + Foliage Tool + WPO = 无阴影|§3.2]]） | 手动拖入关卡、关闭 Nanite、关闭光追阴影 |

### 8.2 树/草 LOD 切换明显

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 远处树突然变成十字片 | LOD 切换距离太近或 Screen Size 设置不合理 | 调大 Screen Size 值使切换更晚发生；调整 LOD 的 Screen Size 曲线 |
| 十字片（Billboard）颜色/亮度与本体不一致 | Impostor 烘焙时光照条件不同 | ① 在统一的中性光照下烘焙 Billboard<br>② 或使用 `LOD Transition` 中的 Dither 淡入淡出过渡 |
| 草地在某个距离突然消失 | Cull Distance 设置过小 | 增大草地的 Cull Distance，或将小地面草改为更大的聚类 Cluster |

### 8.3 植被风动异常

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 风动过于剧烈或完全不动 | Wind Material 参数未与 Wind Directional Source 正确联动 | 场景中放置 **Wind Directional Source** Actor，材质中使用 `Wind` 相关节点（`SimpleGrassWind` / `SpeedTree` 专用节点） |
| Nanite 植被无风动 | WPO × Nanite 架构冲突（详见 [[#三、Nanite|第三章]]） | 禁用 Nanite；或 5.7+ 尝试 Skeletal Mesh 风动新方案 |

---

## 九、后处理与视觉效果

### 9.1 TAA 鬼影 / 重影

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 移动物体拖尾/重影 | TAA 时间混合权重过高 | `r.TemporalAACurrentFrameWeight=0.1`（降低时间混合权重，值越低重影越少但可能闪烁增多） |
| 静止画面也有闪烁 | TAA 处理高频细节时采样不足 | `r.TemporalAASamples=32`（提高采样数，增加 GPU 负载） |

### 9.2 Lumen 反射异常

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 镜面反射中出现黑色块 | Lumen 的屏幕空间追踪（Screen Trace）被遮挡后无回退 | `r.Lumen.Reflections.HierarchicalScreenTraces=1` 启用分层追踪；如果是室内场景，考虑混合使用 Reflection Capture |
| Lumen 反射更新慢 | 间接光照缓存更新频率低 | 提高 Lumen Scene 更新速度（`r.LumenScene.Radiosity.UpdateFactor`） |

### 9.3 体积雾 / 高度雾性能问题

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 开启体积雾后帧率暴跌 | 体积雾是逐 Ray March 计算，开销很大 | ① 降低 **Volumetric Fog Grid Pixel Size**（增大像素间距）<br>② 减少 **Volumetric Fog Grid Size Z**<br>③ 非关键区域关闭体积雾，用 Exponential Height Fog 替代 |

---

## 十、工作流 / 管线问题

### 10.1 资产命名混乱

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 找不到对应资产 | 命名无规则、大小写混用、空格/中文 | 建立统一的命名规范（参见 [[00_工作规范/UE5游戏项目流程/Modeling/游戏3D场景模型制作规范#五、命名规范|游戏3D场景模型制作规范 §5]]）：全小写、下划线分隔、分类前缀 |
| 同一物件有多个版本不知道用哪个 | 版本号管理缺失 | 使用 `_v01`、`_v02` 版本后缀，或依赖 Perforce/Git 版本管理 |

### 10.2 引擎截图与 DCC 效果不一致

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| SP 里调好的效果进引擎变暗/变亮 | ① 引擎 ToneMapper 影响<br>② 色彩空间差异 | ① SP 中设置 **ACES 色彩空间**预览（与 UE 默认 ToneMapper 一致）<br>② 引擎中检查 **Auto Exposure** 是否影响整体亮度 |
| 烘焙后比 Substance 中暗 | 引擎中默认启用了 Auto Exposure 或 PP Volume LUT | 关闭 Auto Exposure 或用中性 PP Volume 重新对比 |

### 10.3 P4/版本管理常见问题

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| .uasset 合并冲突无法解决 | 二进制文件只能整体覆盖 | 使用 UE 自带的 **Asset Diff** 工具对比，采用 OFPA（One File Per Actor）减少多人冲突 |
| 误覆盖别人的工作 | 未 Check Out 直接编辑 | P4 强制的 Check Out 工作流；Git 使用 LFS + Lock 文件 |

---

## 十一、性能快速诊断工具速查

| 问题类型 | 诊断命令 / 视图 | 怎么看 |
|---------|----------------|--------|
| **整体帧率瓶颈** | `stat unit` | Game = CPU 逻辑瓶颈，Draw = CPU 渲染瓶颈，GPU = GPU 瓶颈 |
| **DrawCall 数量** | `stat SceneRendering` | 通常在 `Mesh draw calls` 行 |
| **Shader 复杂度** | 视口 → **Shader Complexity** (Alt+8) | 绿色=低，粉色/白色=严重超预算 |
| **灯光重叠** | 视口 → **Light Complexity** (Alt+7) | 冷色=少灯，暖色/红色=灯太多 |
| **Overdraw** | 视口 → **Shader Complexity** (Alt+8) | 半透材质叠加区域会特别亮 |
| **贴图内存** | `stat Streaming` | 查看 Streaming Pool 使用量和 Overbudget 警告 |
| **GPU 分析** | `ProfileGPU` | 显示 GPU 各 Pass 耗时，定位具体瓶颈 Pass |
| **CPU 分析** | **Unreal Insights** | 更精确的 CPU 帧分析 |

---

## 十二、TA 日常工作：问题排查 SOP

```
美术反馈问题
      ↓
① 收集信息：哪个场景？什么操作后出现？截图/录屏？
      ↓
② 快速筛查：
   ├── 材质类 → Alt+8 Shader Complexity
   ├── 灯光类 → Alt+7 Light Complexity
   ├── 帧率类 → stat unit → 定位 GPU/CPU/Draw
   ├── 贴图类 → stat Streaming → Pool Overbudget?
   ├── 阴影类 → 相关 r. 控制台命令逐项排查
   ├── 导入类 → 检查 FBX 设置 / 单位 / 材质命名
   └── PCG 类 → 检查 HDA 输入 / Cook Log / PCG Graph Debug
      ↓
③ 定位根因 → 修复验证 → 记录到本文档
      ↓
④ 如果问题反复出现 → 写检查脚本自动化拦截
```

---

> [!TIP] 相关笔记
> - 项目流程总览 → [[UE5游戏项目流程|UE5游戏项目流程]]
> - 大世界管线详细分工 → [[场景大世界管线详解|场景大世界管线详解]]
> - 3D 模型制作规范 → [[游戏3D场景模型制作规范|游戏3D场景模型制作规范]]
> - 性能优化复盘案例 → [[01_项目文档/盘丝洞性能优化|盘丝洞性能优化]]
> - 控制台命令速查 → [[01_项目文档/工作文档临时/UE控制台命令|UE控制台命令]]
