---
tags:
  - pcg
---

## 开源资料

### youtube

- GDC

### houdini官方

### 官方技术大会

- [UnrealCircle厦门]《UE5资产优化》| 肖月

- bring nanite to fortnite battle royale in chapter 4


### github

- https://github.com/AdrianPanGithub/HoudiniPCGTranslator

- https://github.com/hcl381/RitualBuildingPCG

- https://github.com/lostcrowgames/EssentialUE5PCG

- https://github.com/dzmjs/UE_PCG_Building

- https://github.com/Davecodingking/PCG-city-generator

- https://github.com/KylerLizi/Houdini-PCG-Environment-Generator

- https://github.com/KylerLizi/PCG-Minigame-Development-Record

### youtube

### 红高

## Houdini城市

### 黑客帝国

- 算法

- 寻路地块划分

- 地块细分

### OSM地图

- LabsBuilding

### PSD to block

- 原画绘制平面，将不同风格建筑分层

### 古建筑单体

- 自定义算法

## UE5城市

### 道路

- 手动设置样条线

### 街区

- 随机撒点

- PCGEX

### 单体建筑

- grammar语法

	- 基于样条线或者体块采样

	- 特定长度范围内单元模块的规则排列

## Houdini自然环境

### 自然环境

- simon末世场景

- 地形

	- 建模

- 植被

	- 地形遮罩

### jianshuashua

- ps绘制平面，将所有元素分层绘制，houdini生成对应的平面数据，包括路径及面域，生成的线面元素导入UE中

- 手绘控制平面图

### 环境元素

- 藤蔓

- 积雪

### model

- 桥梁 ，石头

## UE5自然环境

### 电子梦

### 地形

- brushfy笔刷

### 植被

- 程序化地形材质

- 采样地形，网格体数据

- houdini输出遮罩，采样纹理数据

- biome系统，笔刷绘制遮罩

### 道路

- 遮罩纹理

- assembly模型样条线

- 寻路算法

### 河流

- 样条线

### 悬崖

### PCGEX寻路

## 性能优化

### 肖月

### 通用的性能问题

- ISM

	- 实力化静态网格通过将大量相同静态网格实例批量处理

	- 由于实力化静态网格要求所有实例共享材质

	- 通过在单一材质内部使用随机色相调整和每实例自定义的数据

- 启用分区生成（Partitioned Generation）

	- 将PCG生成域拆分为网格格子，让每个格子独立管理生成的数据，有利于配合World Partition和Level Streaming，实现更高效的场景流式加载和剔除。

	- 操作：选中PCG组件，勾选“Is Partitioned”，调整PCGWorldActor中的“Partition Grid Size”以控制格子大小。

- 使用分层生成（Hierarchical Generation）

	- 在分区基础上，通过PCG Graph的“Use Hierarchical Generation”选项，细化多层级的生成网格，支持不同层级大小的生成逻辑，进一步控制细节和性能平衡。

- 利用实例化静态网格（Instanced Static Meshes）

	- PCG中的Static Mesh Spawner生成的是实例化静态网格组件，极大降低了Draw Call和内存开销，类似于植被绘制的优化方式。尽量避免生成独立Static Mesh Actors。

- 优化碰撞和重叠检测

	- 小型细节物体如草类或小植物尽量关闭碰撞和重叠事件，大幅减少CPU开销和物理模拟压力。

- 合理调整分区网格大小和生成距离

	- 根据玩家摄像机视角和移动速度，调整分区大小和内容生成/剔除距离，避免生成玩家不可见区域的内容，减轻运行时负载。

- 利用HLOD（Hierarchical LOD）和Runtime Cell Transformers

	- 通过调整World Partition的HLOD设置，将远距离区域内容合并为简化实例，减少渲染和管理开销。

	- Runtime Cell Transformers可在运行时将复杂多Actor内容转换为单个实例化Actor，降低流式切换成本。

## 优劣势对比

### UEfest腾讯总结

### CPU与GPU

