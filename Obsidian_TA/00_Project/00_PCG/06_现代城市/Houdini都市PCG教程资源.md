# Houdini 都市PCG 教程与资源合集

> 更新日期：2026-06-14
> 关联：[[PCG方向TA市场分析与UE项目调研]] | [[00_技术美术 简历]]

---

## 一、官方/免费入门（必看）

### 1. Epic City Sample — UE5 + Houdini 城市生成官方教程 ⭐⭐⭐⭐⭐

> **最佳起点**，Epic 官方免费，完整生产级城市生成器

| 项目 | 详情 |
|---|---|
| **地址** | [City Sample Quick Start (中文版)](https://dev.epicgames.com/documentation/unreal-engine/city-sample-quick-start-for-generating-a-city-and-freeway-using-houdini?application_version=5.5&lang=zh-CN) |
| **内容** | 样条线定义城市边界 → 主干道路 → 功能区划分 → 建筑体块 → 高速公路+匝道 → PDG导出 → UE5导入 |
| **核心HDA** | City Layout、City Zone、City Processor、City Lot Processor、Freeway Util Curve Attributes |
| **推荐Houdini版本** | 18.5.532+（原项目开发版本），新版也兼容 |

### 2. kiryha/Houdini — Procedural City Wiki ⭐⭐⭐⭐

> 开源 Wiki，深度讲解**两级 Shape Grammar 立面系统**

| 项目 | 详情 |
|---|---|
| **地址** | [github.com/kiryha/Houdini/wiki/Procedural-City](https://github.com/kiryha/Houdini/wiki/Procedural-City) |
| **内容** | Level Grammar（垂直分层） → Bucket Grammar（水平分块） → JSON驱动风格替换 → 模块化资产插槽 |
| **亮点** | `floor_repeat: "*"` 实现高度自适应，`facade_orientation` 控制朝向 |

---

## 二、付费进阶教程（强烈推荐）

### 3. ABOUTCG — Houdini PCG 程序化工厂游戏场景 ⭐⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [aboutcg.org/courseDetails/2742](https://www.aboutcg.org/courseDetails/2742/introduce) |
| **时长** | 30小时 |
| **内容** | 道路生成、建筑群落、基于Tag的资产框架、**无穿插撒点技巧**、工业化PCG工具搭建 |
| **适合** | 游戏TA，工厂/工业场景PCG（可迁移到都市场景） |

### 4. 翼狐网 — Houdini+UE5《长城》科幻城市场景 ⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [global.yiihuu.com/a_12806.html](https://global.yiihuu.com/a_12806.html) |
| **时长** | 7.5小时 |
| **内容** | 原画→白模→Houdini 20.5 + UE5.5 构建科幻城市建筑群，可复用工具链+灯光氛围 |
| **适合** | 影视级城市场景，科幻/奇幻风格 |

### 5. Gnomon Workshop — Large-Scale Aerial Shot ⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [cgchannel.com/2024/01/tutorial-creating-a-large-scale-aerial-shot](https://www.cgchannel.com/2024/01/tutorial-creating-a-large-scale-aerial-shot/) |
| **讲师** | Frederick Vallee（ILM TD） |
| **时长** | 7+小时 |
| **内容** | OSM数据导入 → Houdini程序化城市+农田 → Arnold渲染 → Nuke合成 |
| **价格** | $54/月订阅 |

---

## 三、数据驱动城市生成（GIS/OSM）

### 6. EasyV — SHP/OSM数据实战：程序化生成城市建筑群 ⭐⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [easyv.cloud/c/article/15547.html](https://easyv.cloud/c/article/15547.html) |
| **内容** | OSM/SHP数据导入 → 坐标投影转换 → VEX高度补全（3.3m/层） → PolyExtrude拉伸 → Labs Building Generator立面 → 夜景灯光（VEX随机窗灯） |
| **亮点** | 完整的"数据→规则→资产"管线，中文实战教程 |

### 7. EasyV — 基于Houdini与GIS数据的程序化三维城市场景 ⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [easyv.cloud/c/article/40317.html](https://easyv.cloud/c/article/40317.html) |
| **内容** | GIS数据→建模→渲染全链路，大规模城市场景工程化方法 |

### 8. EasyV — 利用Houdini实现高效三维城市场景构建 ⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [easyv.cloud/c/article/15708.html](https://easyv.cloud/c/article/15708.html) |
| **内容** | "数据—规则—资产—渲染"四大环节，PDG并行处理，USD复合层组织，Instancing显存优化 |
| **性能数据** | 600km²城市：230GB原始 → 8.1GB模型 → 1.4GB Packed Instancing（RTX 4090单机） |

---

## 四、开源框架与管线工具

### 9. Undini Framework — UE5 ↔ Houdini 自动化PCG管线 ⭐⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **地址** | [github.com/luk4m4repo/luk4m4_Undini_framework](https://github.com/luk4m4repo/luk4m4_Undini_framework) |
| **技术栈** | UE 5.3.2+ / Houdini 20.0.653+ / Python 3.7+ |
| **工作流** | UE样条线→JSON→Houdini headless(TOP)→CSV/FBX→UE DataTable→自动构建PCG Graph |
| **生成器** | 建筑(PCGHD)、人行道+道路(SWR) |

### 10. Adrian Pan — 自定义Houdini Engine for Unreal ⭐⭐⭐⭐

| 项目 | 详情 |
|---|---|
| **GitHub** | [HoudiniEngineForUnreal](https://github.com/AdrianPanGithub/HoudiniEngineForUnreal) / [HoudiniMassTranslator](https://github.com/AdrianPanGithub/HoudiniMassTranslator) |
| **视频** | [YouTube Demo](https://youtu.be/HAM8_OP_Fyc) |
| **亮点** | 比官方插件**快2-40倍**的数据IO，原生UE5 World Partition支持，实时交通zone graph |
| **讨论** | [SideFX Forum](https://www.sidefx.com/forum/topic/98723/) |

---

## 五、快速参考 — 推荐学习路径

```
阶段 1：入门（1-2周）
  ├─ Epic City Sample 官方教程          → 了解完整管线
  └─ kiryha Procedural City Wiki         → 理解Shape Grammar概念

阶段 2：实用技能（2-4周）
  ├─ EasyV SHP/OSM 数据实战             → 学会数据驱动城市生成
  ├─ ABOUTCG 程序化工厂场景              → 游戏级PCG工具搭建
  └─ Undini Framework                    → 自动化管线思维

阶段 3：高级/专项（选学）
  ├─ 翼狐网《长城》科幻城市              → 影视级表现
  ├─ Gnomon Workshop航拍城市             → 大规模场景合成
  └─ Adrian Pan 自定义引擎插件           → 引擎底层优化
```

---

## 六、其他资源渠道

| 平台 | 搜索关键词 |
|---|---|
| **Bilibili** | "Houdini PCG 城市"、"Houdini 程序化建筑"、"UE5 PCG都市" |
| **YouTube** | "Houdini Procedural City"、"Houdini Urban PCG"、"UE5 City PCG" |
| **SideFX 论坛** | [sidefx.com/forum](https://www.sidefx.com/forum/) — 搜索 City、Urban、PCG |
| **ArtStation** | Houdini 板块 — 看作品 + 找 Breakdown |
| **80.lv** | 技术访谈 + 城市PCG案例研究 |

---

## 七、核心工作流速查

```
1. 数据准备
   └─ GIS/SHP/OSM导入 → 坐标投影 → VEX/Python清洗

2. 地块与道路
   └─ Curve主干道 → City Layout / Boolean切割 → 街区地块

3. 建筑体块
   └─ 地块轮廓 → PolyExtrude(高度) → 随机种子破整齐

4. 立面细节
   └─ Labs Building Generator → 窗户/阳台 → 风格替换

5. 大规模优化
   └─ Packed Primitive → LOD → PDG并行 → Instancing

6. 引擎交付
   └─ Cache(PBC/FBX/CSV) → Houdini Engine → UE5材质+渲染
```
