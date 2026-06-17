# houdinikitchen

### Houdini全面入门及进阶系列教程 houdinikitchen-Tutorials

### [入门小案例，湖边小屋老师讲解，有工程文件](https://www.vfxforce.cn/archives/11591)

### [HOUDINI KITCHEN](https://www.houdinikitchen.net/)

### 帮助文档

### Tutorial 1. Networks and Nodes

#### 子主题 5

![](793bfdfb22a046c60d5ceba420fbcf49a2d1ff42877ceca97a8b60d31d1e8bfc.png)

#### 创建单个物体

#### 创建地形

#### 地形上散布点，引用单个物体

#### 不同scatter参数

### Tutorial 2. Transform Node

#### group

### Tutorial 3. Geometry Primitives

#### 涵盖的节点为：圆形，球形，管状，框形，圆环形，柏拉图式实体和网格。

#### 这是一本非常实用的教程，它将告诉您有关可以创建的不同几何类型（基本体，多边形，多边形网格，网格，nurbs，贝塞尔曲线和多边形汤）以及何时需要使用它们的所有知识。

#### 我们讨论使用Houdini帮助文档来查看节点的工作示例。

#### 我们将更详细地介绍网格图元，并展示其某些用途，例如作为物品的生成，作为要绘画的表面以及作为山地景观的基础。 我们在参数窗口中给出另一个表达式示例，并使用这些表达式使网格密度保持一致，而不管其比例如何。

#### mountain

### Tutorial 4. Introduction to VOPs

#### 本教程是VOP网络的简介，该主题太大，无法在单个教程中涵盖。我们看一下属性VOP并解释如何将其用于操纵和创建点属性。

#### 本教程介绍了使用数学节点进行位置和颜色处理，并探讨了噪点和图案的生成。然后，它展示了如何使用大陆和海洋的噪声创建低多边形的行星，并展示了如何添加一个称为“ pscale”的新属性，该属性可用于缩放放置在这些点上的对象。

#### shader

- 网格着色原理
#### uifiednoise，常用的噪波，帮助文档

![](9b65d223626985b9eac916d1d5699254df64e31b437023841a4fdb2968b542ad.png)

#### 根据噪波颜色散布

### Tutorial 5. Merge Node

#### 关于如何以及何时使用合并节点以及如何在合并后的组中使用组访问单个源的简短教程。

### Tutorial 6. Scatter Node

#### 本教程着眼于分散节点，该节点用于在表面上放置随机点。它涵盖了驱动点放置的一些不同方式，包括点数，纹理和密度属性。

#### 它还深入研究了属性VOP。在本教程结束时，我们已经展示了如何使用“散布”节点来创建具有真实植被分布的沙漠场景。

#### 图形散布

![](f3d3431b591251df6ad8a7a2fa7766b9977dd08b39b859f200abf8f6d08b68be.png)

#### 程序限定散布条件

![](30fedd18fe650c2eff4843807dcd8e82c53a3407901d62510346dd701bea304d.png)

### Tutorial 7. Group Nodes

#### 本教程研究如何在Houdini中创建和使用组。它涵盖了组节点，组范围节点，组传输节点和组合并节点。

#### 我们来看一下可用于向组中添加组件模式的组语法。 组语法的文档在这里： https://www.sidefx.com/docs/houdini/model/groups.html

#### 用来筛选特点的元素，精确选择

### Tutorial 8. All about Houdini Digital Assets

#### Houdini Digital Assets (HDAs)

#### Houdini数字资产（HDA）是节点的网络，可以打包以简化Houdini中的常用任务或创建可以在外部软件中使用的工具。 HDA可以在具有Houdini Engine插件的任何软件中使用。这些包括： 胡迪尼，Autodesk的Maya，Autodesk的3DS Max，史诗的虚幻引擎（UE4）

#### 该视频涵盖： 在Houdini中创建网络以加快常用任务的速度 为外部软件设置网络，以及如何与Houdini中未创建的对象集成。 如何在HDA中设置输入对象的实例化

### Tutorial 9. Attribute Transfer Node

#### 本教程研究了属性传递节点的实际应用，该属性传递节点根据对象在空间中的位置将信息从一个对象传递到另一个对象。 首先介绍Houdini属性，然后演示简单的属性传递并解释节点的所有参数。 本教程的大部分内容是创建一个网络，该网络创建遍及山坡的树根。它以多种不同的方式使用“属性传递”将场景的所有元素拉在一起，以便可以更改树的根部或下面的地面的形状，并且场景中的其余部分也可以根据需要进行调整。

### Tutorial 10. Introducing Volumes and VDBs

#### 第一部分解释了不同类型的体积，并描述了创建和操纵它们的最佳方法。使用节点网络对此进行了演示，可以在此处下载

### Tutorial 11. Lines and Curves

#### 本教程首先说明Houdini创建曲线的方式，以及Houdini和其他建模程序中的边之间的差异。然后查看一些可用于创建和编辑曲线的节点。这些是“线”，“曲线”，“ Curvedraw”，“添加”和“端点”节点

#### 该视频的其余部分用于演示一些不同的方法，这些方法可以使用曲线从头开始创建过程几何。我们制作了一个程序化的赛车轨迹生成器，该生成器采用输入曲线和景观，并创建轨迹和道路标记，在曲线的内部具有障碍物，在曲线的外部具有成堆的轮胎。然后，我们将树木放置在可更新的景观上，以避免放置在赛道上。

### Tutorial 12. Copy Stamping and the Foreach Loop

#### 本教程描述了如何使用点属性来影响上游输入节点： -首先使用传统的“复制邮票”节点（01:30分钟） -然后按照sidefx的建议再次使用Foreach Loop节点（15:35分钟）

#### 然后深入研究Foreach循环的其他用途： -根据属性循环点组（38:17分钟） -遍历连接的片段（45:30分钟） -循环播放指定次数（57:25分钟） -创建分形（64:50分钟）

#### copy stamp

- 设定随机种子
  ![](6ab9e93411a6c2abb2b2982ba6e0f5843b8368d7e74910041086848b3a56c518.png)
  - 案例一，随机颜色，尺寸
    ![](33d5261995d872f46dd726144d7506a784db86dc388b09b7643b0a8e9e4cec5f.png)
- 所有种子随机，运算量大，速度慢
  ![](55f2181311b2aea115842f626f488e65264b0d73496916ee26bf9151e64971a7.png)
#### for each

- single pass 单个点检查数据
- 五个特定种子的树
  ![](8fed518370c56cf27a1b30b128c60e6109d6d3cadf096444a34b74706708fe6b.png)
#### for each 遍历循环

#### 分形

### [for each loop 额外教程](https://www.bilibili.com/video/BV1y84y1f7g9/?p=1&vd_source=089349bc15fe4a0508fc235b6d5563a8)

### Tutorial 13. UV Tools

#### 本教程概述了可在Houdini中创建UV的不同节点，还介绍了在Houdini中设置，显示和预览UV和纹理的方法，并演示了显示PBR纹理的快速方法。

#### 子主题 2

![](f0d15217bc03604409dd1c58259fd2ba0e587af4be2456cdcb0a45ecbca947d6.png)

### Tutorial 14. L-Systems

#### 使用Aristid Lindenmayer的著作《植物的算法之美》中的示例，深入学习用Houdini编写L系统的原理的教程。

### 地形加植物散布
