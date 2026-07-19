# Houdini 散布系统文档（Scatter + Copy to Points）

> **项目文件**: `D:/TA/Houdini/mcp/MCP.hip`
> **网络路径**: `/obj/scatter_system`
> **创建日期**: 2026-07-18
> **Houdini 版本**: 21.0.440

---

## 一、概述

基于 **Scatter** 在噪声地形表面随机散布点，利用 **Copy to Points** 将 Torus（圆环）复制到每个散点上。每个圆环具有随机大小和颜色，Y 轴对齐地形法线，孔洞与地形表面平行。

---

## 二、节点管线

```
ground ──→ terrain ──→ pt_normals ──→ scatter_pts ──→ rand_pscale ──→ rand_color
  (网格)     (置换)      (法线烘焙)       (散点)         (随机缩放)       (随机颜色)
                                                                          │
                                                                          ├──→ copy_tori ←── rotate_torus ←── source_torus
                                                                          │     (显示节点)     (旋转-90°X)      (圆环源)
                                                                          │
                                                                          └── (merge1 备用)
```

### 节点详情
    end

    T1 --> X --> T2 --> C --> R
```

### 2.4 节点详情

| # | 节点名称 | 类型 | 说明 | 关键参数 |
|---|---------|------|------|---------|
| 1 | `ground` | Grid | 10×10 地面网格 | Rows/Cols: 80, Size: 10×10 |
| 2 | `terrain` | Mountain::2.0 | Simplex 分形噪声置换 | Height: 0.98, Element Size: 2.5, Octaves: 4, Roughness: 0.6 |
| 3 | `pt_normals` | Normal | 计算显式点法线 (N) | Add Normals to: Points |
| 4 | `scatter_pts` | Scatter::2.0 | 在置换地形表面散布 500 个点 | Force Total Count: 500, Seed: 42, Relax: 5 iterations, Output `pscale` + `id` |
| 5 | `rand_pscale` | Attribute Randomize | 随机缩放属性 | Attribute: `pscale`, Uniform [0.15, 0.8], Seed: 123 |
| 6 | `rand_color` | Attribute Randomize | 随机颜色属性 | Attribute: `Cd`, Uniform blue spectrum, Seed: 456 |
| 7 | `source_torus` | Torus | 源圆环几何体 | Radius: (0.3, 0.1), Rows/Cols: 24/16 |
| 8 | `rotate_torus` | Transform (xform) | 将圆环的 Y 轴旋转到 Z 方向 | Rotate: [-90°, 0, 0] |
| 9 | `copy_tori` | Copy to Points::2.0 | 复制 500 个圆环到散点 | Pack & Instance, `transform: true` |

---

## 三、关键技术点

### 3.1 法线对齐（Normal Alignment）

**问题**：Mountain 产生的法线 `N` 是顶点属性，Scatter 生成散点时顶点法线被丢弃，Copy to Points 找不到法线进行旋转对齐。

**解决**：在 `terrain` 和 `scatter_pts` 之间插入 **Normal SOP**（`pt_normals`），设置 `Add Normals to: Points`，将顶点法线烘焙为点法线。散点继承后每个点都携带 `N` 属性，Copy to Points 即可根据法线进行旋转。

### 3.2 Y 轴对齐机制

Copy to Points 的 `transform: true` 模式默认将源几何体的 **Z 轴**对齐法线。Torus 默认平铺在 XY 平面，孔洞沿 Z 轴，因此需要在复制前通过 **Transform SOP** 将 Torus 绕 X 轴旋转 -90°，使 Y 轴交换到 Z 方向，实现 Y 轴对齐法线。

| 源 Torus 轴 | 旋转后方向 | Copy to Points 映射 |
|-------------|-----------|-------------------|
| Y 轴 | → Z | → 法线 N ✓ |
| Z 轴（孔洞） | → -Y | → 垂直于法线 |

### 3.3 散点属性传递

散点属性流向：

```
scatter_pts 生成:
  ├─ P (位置)      ──→ Copy to Points: 复制位置
  ├─ N (法线)      ──→ Copy to Points: 旋转对齐
  ├─ pscale (缩放) ──→ rand_pscale 随机化后 → 每个圆环大小
  └─ id (ID)      ──→ 每个点唯一标识

rand_color 生成:
  └─ Cd (颜色)     ──→ 每个圆环颜色
```

### 3.4 性能优化

`copy_tori` 开启 **Pack and Instance**：500 个 Torus 以 Packed Geometry 实例化，视口性能友好，内存开销低。

---

## 四、可调参数

### 地形
| 参数 | 节点 | 默认值 | 说明 |
|------|------|--------|------|
| Height | terrain | 0.98 | 地形起伏幅度 |
| Element Size | terrain | 2.5 | 噪声特征尺寸 |
| Octaves | terrain | 4 | 分形细节层数 |

### 散布
| 参数 | 节点 | 默认值 | 说明 |
|------|------|--------|------|
| Force Total Count | scatter_pts | 500 | 散点总数 |
| Seed | scatter_pts | 42 | 散布随机种子 |
| Relax Iterations | scatter_pts | 5 | 点松弛迭代（均匀度） |

### 变化
| 参数 | 节点 | 默认值 | 说明 |
|------|------|--------|------|
| Min/Max | rand_pscale | [0.15, 0.8] | 大小范围 |
| Min/Max | rand_color | 蓝色系 | 颜色范围 |

### 源几何体
| 参数 | 节点 | 默认值 | 说明 |
|------|------|--------|------|
| Radius | source_torus | (0.3, 0.1) | 圆环半径 |
| Rows/Cols | source_torus | 24/16 | 圆环分辨率 |
| Rotate X | rotate_torus | -90° | 方向对齐 |

---

## 五、几何体统计

| 指标 | 数值 |
|------|------|
| 散点数量 | 500 点 |
| Torus 副本数 | 500（Packed） |
| 包围盒 | ~10.78 × 0.84 × 10.70 单位 |
| 散点属性 | P, N, pscale, id, Cd |
| 网络节点数 | 9（含 1 个备用 merge） |
| 所有节点状态 | 零错误 |

---

## 六、扩展建议

- **替换源几何体**：将 `source_torus` 替换为任意 SOP 链，自动散布到所有散点
- **密度控制**：在 Scatter 上使用 `Density Attribute` 按区域控制分布密度
- **多源变体**：利用 Copytopoints 的 `Piece Attribute`（`name` 属性），在源输入中并入多种几何体，按散点 `name` 值匹配
- **增加变化维度**：继续追加 Attribute Randomize 节点，为 `orient`（方向扰动）、`alpha` 等属性添加随机变化
- **缓存**：在 `terrain` 和 `scatter_pts` 之间插入 File Cache，避免重烹饪；在 `copy_tori` 后添加 File Cache 固化最终结果
