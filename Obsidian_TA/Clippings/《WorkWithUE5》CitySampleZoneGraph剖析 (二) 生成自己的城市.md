---
title: "《WorkWithUE5》CitySampleZoneGraph剖析 (二) 生成自己的城市"
source: "https://zhuanlan.zhihu.com/p/554727187"
author:
  - "[[小何才露尖尖角分享整理UE使用经验]]"
published:
created: 2026-06-05
description: "引言本章将从Houdini开始，利用UE5示例中的资源生成自己的城市。本篇文章属于纯流程向，本章过后将会在Houdini中生成自定义城市，且导出PBC文件。参考文档为官方文档，本文会对文档中的一些未说明的细节和坑进行记…"
tags:
  - "clippings"
---
从巴洛克到浪漫的你 等 46 人赞同了该文章

目录

收起

引言

相关概念

配置Houdini环境

绘制城市

1.绘制城市形状

2.创建城市主干路

3.绘制城区

4.绘制高速公路

5.组装城市

6.将高速公路起止点连接到城市

生成城市缓存并导出PBC

1.必要配置

2.生成城市缓存

导出geometry和城市点云数据(Point Cloud Alembics PBC)

结束语

## 引言

本章将从 [Houdini](https://zhida.zhihu.com/search?content_id=211405479&content_type=Article&match_order=1&q=Houdini&zhida_source=entity) 开始，利用UE5示例中的资源生成自己的城市。本篇文章属于纯流程向，本章过后将会在Houdini中生成自定义城市，且导出 [PBC](https://zhida.zhihu.com/search?content_id=211405479&content_type=Article&match_order=1&q=PBC&zhida_source=entity) 文件。参考文档为官方文档，本文会对文档中的一些未说明的细节和坑进行记录。

## 相关概念

1.什么是 [PointCloud](https://zhida.zhihu.com/search?content_id=211405479&content_type=Article&match_order=1&q=PointCloud&zhida_source=entity)

顾名思意，PointCloud就是点云，由于 [CitySample](https://zhida.zhihu.com/search?content_id=211405479&content_type=Article&match_order=1&q=CitySample&zhida_source=entity) 中的城市和街道是利用程序化生成的，而数据的形式就是利用点来存储的，每个点有自己的属性，即这个点是不是建筑点，是不是道路点，以及记录了该点与其他点之间的关系是什么，相同类型的点就形成了一个点云，不同的点云就形成了整个程序化生成的城市，即PointCloud就是存储了相同类型点的数据的集合。这些工作都是在Houdini中做的，而Houdini生成的PointCloud文件的格式就是.PBC(以后提及PBC就是PointCloud)，UE将PBC导入形成.uasset(下篇文章会讲)，再利用RulesProcessor即可在UE中生成城市。

2.右键的含义

为了简化，该篇文章提到的右键如果未特殊说明，都是在Houdini的节点窗口进行右键。

3.找不到某个节点：右键 - 直接搜索名字。OK废话不多说，Let's do it!

## 配置Houdini环境

1.在虚幻商城下载CitySample会有这个压缩包，将这个压缩包解压，路径不要有中文和空格，我的路径是这个D:\\UE5Sample\\CitySampleSource

![](https://pic4.zhimg.com/v2-539b4d3a22cae236bb49b522c2339dbf_1440w.png)

2.在C盘“文档”中找到houdini19.0/houdini.env，在最后一行添加HOUDINI\_PATH = D:/UE5Sample/CitySampleSource/Small\_City/houdini;&。路径就是将刚才解压好的路径下的Small\_City/houdini;设置到默认配置中，houdini19.0可能不在“文档”中，具体路径由本地决定

3.在D:/UE5Sample/CitySampleSource/创建MyCity文件夹，用来存放缓存和生成的数据文件，以免对源文件覆盖

![](https://pic1.zhimg.com/v2-d18d67860f4910aa6ed68c71fd6b6d4e_1440w.jpg)

注意：一定要将SmallCity/houdini复制到MyCity下，该文件中包含了相关建筑模型，如果不复制则不出效果

4.启动Houdini，成功加载后会在工具栏 - Assets - Asset Manager - OperatorType Libraries显示如下

![](https://picx.zhimg.com/v2-fd7af38777151b7a32b42060f64d0901_1440w.jpg)

## 绘制城市

### 1.绘制城市形状

1.1打开Houdini，右键 - Geometry - Geometry - 双击Geometry打开geo1 Graph - 右键 - Primitive - Curve

![](https://pic2.zhimg.com/v2-ae18b7a667bcc3a525dd47e2ac656a19_1440w.jpg)

1.2点击curve1并在视口左边工具栏选中Show Handle，并在顶视图绘制城市形状

![](https://pica.zhimg.com/v2-9e2a0fda2a05147433482401c83aab54_1440w.jpg)

注意：要保证城市区域够大，注意看顶视图的刻度

1.3右键 - Epic Games - City(Layout) - City Layout - 将曲线的输出引脚链接到Layout的第一个引脚，选中Layout1在CityName输入MyCity，Ctrl + s，保存为CitySampleSource/MyCity/MyCity.hip(刚才的MyCity路径)

![](https://pica.zhimg.com/v2-76e2f341ef3c66cb0662c9158fc120d6_1440w.jpg)

### 2.创建城市主干路

同样的方法创建Curve2和Curve3，利用merge节点连接到一起，每一条Curve都是一条主干路，并链接如下

![](https://pic1.zhimg.com/v2-6b33cc65ccdd6523fa78cafafaa4d63a_1440w.jpg)

### 3.绘制城区

3.1同样的方法创建Curve4、Curve5，并创建CityZone链接至layout

![](https://picx.zhimg.com/v2-d4aa260d7f692279f0aec9a7b787ce2f_1440w.jpg)

3.2分别点击Zone1和Zone2，在参数窗口设置城区的属性

![](https://pic2.zhimg.com/v2-c51eb435f3d6ea8fcc0f7fad640595c9_1440w.jpg)

注意：该操作前要选中layout1，在参数窗口中勾选preview\_zones(完事取消勾选)，然后在透视图中操作

### 4.绘制高速公路

4.1同样的方法创建Curve6，注意Curve6是高速公路，起点终点都要能和绘制的主干路重合，即与主干道形成闭环并右键创建 [Freeway Util Curve Attribute](https://zhida.zhihu.com/search?content_id=211405479&content_type=Article&match_order=1&q=Freeway+Util+Curve+Attribute&zhida_source=entity) 节点，链接如下

![](https://pic2.zhimg.com/v2-2f22fb813732e0f43e8297dcbdf4b82f_1440w.jpg)

4.2点击Freeway Util Curve Attribute设置其属性

![](https://pic2.zhimg.com/v2-a68a4333336d2d8ecf046f78553a5247_1440w.jpg)

### 5.组装城市

5.1右下角将自动烘培从默认的自动改成手动

![](https://picx.zhimg.com/v2-d1bc71ab97fcfd3eb2133ad0ef2571bb_1440w.png)

5.2添加CityProcessor，链接如下(注意要点击processor1的蓝色部分)，点击烘培

![](https://pic2.zhimg.com/v2-be8ef5d59981fd07ea9a4cbca1b2fe69_1440w.jpg)

感叹号忽略它

5.3睡一觉出效果

![](https://picx.zhimg.com/v2-ab08b5d51595d18537d0b73dd4b8acd7_1440w.jpg)

### 6.将高速公路起止点连接到城市

6.1右键processor1 - Allow Editing of Contents - 双击processor1 - 找到蓝色的Freeway部分 - 双击 - 找到connections\_blank并双击

![](https://pica.zhimg.com/v2-19e89cebc9807b62e1d6f839ac82382a_1440w.jpg)

6.2双击all\_connections - 显示ROAD\_REFERENCE - 按住Ctrl 选择ROAD\_REFERENCE和merge\_freeway选中他们两个的Display Template (pink)

![](https://pic3.zhimg.com/v2-b294ac8796a6c022a982f6036551bb90_1440w.jpg)

6.3将右下角烘焙改成AutoUpdate

6.4选中connection\_set\_1并开启Preview Mode

![](https://pica.zhimg.com/v2-f2b977f3bc2bf11befe900230a09972a_1440w.jpg)

6.5点击添加曲线，并点击Handle tool，左键点击两个点进行链接(Ctrl + 左键/Shift + 左键)

![](https://pica.zhimg.com/v2-f09b6c5ae68f166cee1daf117e92c5de_1440w.jpg)

注意：高速公路必须连接到主干路上

6.6确保Street和链接处有相同的车道数

![](https://pic3.zhimg.com/v2-189859136cbda97cd1fd610bb59d9b32_1440w.jpg)

6.7重复6.5-6.6，链接高速公路另一端

6.8选中connection\_set\_1关闭Preview Mode

6.9回到梦开始的地方，检查下是否链接成功

![](https://pic4.zhimg.com/v2-4a64f4119f07ce7f6638c70d217dfd85_1440w.jpg)

这里建议将烘焙改成手动，不然。。。。。。你懂的

6.10补充：双击City Processor - 选择黄色的LOTS部分 - 选择City\_Lot\_Processor，这些参数是用来定义建筑模型的，需要改的自己该

![](https://picx.zhimg.com/v2-bd5efe6c45240a0734a963dd95beed69_1440w.jpg)

## 生成城市缓存并导出PBC

### 1.必要配置

1.1freeway\_export是用Python2写的，Houdini19是Python3，需要将代码改成Python3格式，右键Processor1 - Type Properties - Scripts更改所有print括号(三处)如下

![](https://pica.zhimg.com/v2-5d972e129de918a87030ae93d4b0d1c8_1440w.jpg)

1.2将自己的目录下的2.7复制出来一份改成3.7

![](https://pic3.zhimg.com/v2-6bbf2888f6c12a65e91889acdff540b0_1440w.jpg)

1.3City Processor - 双击FREEWAY - 操作如下 - Accept保存

![](https://pic2.zhimg.com/v2-eab43177b8abc99827582f74f2d24811_1440w.jpg)

1.4右键FREEWAY - Type Properties如下，Channel的配置指向了CONTROL\_Export的export\_all参数

![](https://pic4.zhimg.com/v2-2104d285ad368ad23880088f3b90ef8b_1440w.jpg)

1.5这几个大坑搞了很久，别问为什么，干就完了

### 2.生成城市缓存

2.1设置手动烘培 - 选中City Processor

2.2勾选Use [PDG](https://zhida.zhihu.com/search?content_id=211405479&content_type=Article&match_order=1&q=PDG&zhida_source=entity) ：PDG处理发生在建筑生成阶段，在城市规模较大时尤其有用，因为它并行化了需要最大计算能力的建筑生成，开启PDG需要依此点击1、2、3来生成缓存

2.3不勾选Use PDG：只需要点击process city without PDG就能生成缓存，我用的是不勾选，会在CACHES生成文件

![](https://picx.zhimg.com/v2-d35cef6a4f5d46fd3a4cae4357260c7d_1440w.jpg)

## 导出geometry和城市点云数据(Point Cloud Alembics PBC)

1.1如果生成缓存时勾选了Use PDG，则直接点击EXPORT ALL PBC

2.2如果生成缓存时没勾选Use PDG，则要在Caches and Exports下确定是否勾选了要导出的内容，然后点击EXPORT ALL PBC，会在D:\\UE5Sample\\CitySampleSource\\MyCity\\PBC下生成PBC文件

![](https://pic2.zhimg.com/v2-32154a27b6135e71d6f2ace7ef85339b_1440w.jpg)

2.3检查一下MyCity\\PBC下是否生成PBC，注意一定要有Freeway\_开头的PBC，这些包含了道路以及导航数据，如果没有的话，则在UE5中生成会没有道路。

![](https://pic3.zhimg.com/v2-0e4db97514745128d5c116a03f4c8084_1440w.jpg)

## 结束语

。。。。。。emmm，没什么说的，加油，干就完了 ，下章首先分析一下Houdini中的道路点云数据的格式是什么样的，然后讲如何导入UE5，在UE5生成城市，下班下班。。。。。。

编辑于 2022-08-18 12:52[ArkClaw -7\*24小时在线的专属个人助手](https://www.volcengine.com/product/arkclaw?utm_source=7&utm_medium=zhihu&utm_term=webtw_arkclaw_cuxiao&utm_campaign=0&utm_content=zhihu_arkclaw&spu=biz%3D0%26ci%3D3682615%26si%3Df52f4ac6-4c72-4ca7-8afb-c2e8568f7815%26ts%3D1780646956%26zid%3D1629)

