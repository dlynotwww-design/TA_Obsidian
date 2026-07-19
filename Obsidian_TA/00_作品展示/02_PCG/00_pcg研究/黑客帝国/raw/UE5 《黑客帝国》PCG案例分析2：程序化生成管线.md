---
title: "UE5 《黑客帝国》PCG案例分析2：程序化生成管线"
source: "https://zhuanlan.zhihu.com/p/8777588500"
author:
  - "[[从巴洛克到浪漫的你]]"
published:
created: 2026-07-11
description: "继上一篇《资产与内容管线》 UE5 《黑客帝国》PCG案例分析1：资产与内容管线之后，我们紧接着看下“程序化生成管线”，先来一段官方介绍： 官方文档可参考： \"城市示例\"快速入门 一，City Layout用于城市…"
tags:
  - "clippings"
---
[收录于 · Unreal从0到1](https://www.zhihu.com/column/c_1408921150043267072)

北京TA吴强 等 46 人赞同了该文章

目录

继上一篇《资产与内容管线》

[![](https://picx.zhimg.com/v2-040a58ce4bd1f47cc5b03a485a54ad5c.png?source=7e7ef6e2&needBackground=1)](https://zhuanlan.zhihu.com/p/8715741204)

之后，我们紧接着看下“ [程序化生成管线](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E7%A8%8B%E5%BA%8F%E5%8C%96%E7%94%9F%E6%88%90%E7%AE%A1%E7%BA%BF&zhida_source=entity) ”，先来一段官方介绍：

官方文档可参考：

## 一，City Layout

用于城市的布局，给定两类输入： **Shape** （由Curve节点手动圈出）和 **Main Arteris** （也是由Curve节点提供），通过修改一些参数生成” [城市布局](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%9F%8E%E5%B8%82%E5%B8%83%E5%B1%80&zhida_source=entity) “:

![](https://picx.zhimg.com/v2-bb1fb3ee8448e72ff6c2e96c9ace639f_1440w.jpg)

这个HDA节点一共有4个输入，从左到右依次是：” **City Shape（城市形状）**, **Arteries（主干道）** ， **City Zones（城区）** ， **Removal Inputs（移除输出）** “，City Layout完整的图表如下：

![](https://pica.zhimg.com/v2-fffa7ac993676d0fdb46461e0dfd4a64_1440w.jpg)

按照执行的逻辑流，从上往下依次实现：

![](https://pic1.zhimg.com/v2-ababd048d6629439184b42ecaaa97cf2_1440w.jpg)

其中元数据包括：“路网，地段定义，人行道网络，连通性，交通密度，行人密度”等：

![](https://pic4.zhimg.com/v2-aeb19aad037a85172bc34c18150f0b55_1440w.jpg)

![](https://pic3.zhimg.com/v2-63af2e36b56838043173e69df288a54e_1440w.jpg)

City Layout 输出城市布局和 [元数据](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=2&q=%E5%85%83%E6%95%B0%E6%8D%AE&zhida_source=entity) 给到City Processor来构建城市。

![](https://pic4.zhimg.com/v2-6699c86c2a02ec15dd4c93af3d3dcd07_1440w.jpg)

## 二，City Processor

这张 [依赖图](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E4%BE%9D%E8%B5%96%E5%9B%BE&zhida_source=entity) 展示了城市工具的关键组成和从上到下的依赖关系， 它显示了在程序化生成背景下如果要在特定情况下改变规则， [城市结构](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%9F%8E%E5%B8%82%E7%BB%93%E6%9E%84&zhida_source=entity) 的再生会发生在哪一环节。

![](https://pic4.zhimg.com/v2-0cec2e9185ceb7a0a26b66e656e5a4f5_1440w.jpg)

由上一环节生成的Layout做为Basic，然后生成Roads（道路）， FreeWay（高速路），Lots（城区地块），Sidewalks（人行道），这些部分构成了城市的基础。然后Traffic（ [交通系统](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E4%BA%A4%E9%80%9A%E7%B3%BB%E7%BB%9F&zhida_source=entity) ）， Buildings（建筑）， Ground（地块）构成了城市的核心。StreetFurniture（街道组件），Decals（贴花系统），Audio（卷积混响）构成了城市的点缀。

City Processor HDA也有四个Input, 从左到右依次是：”City Layout（城市布局，承接上一个步骤），FreeWay（高速公路），Hero Buildings（主建筑） ，Height Override（天际线覆盖）“，对应的Houdini 图表为（粉线代表了依赖关系）：

![](https://pic4.zhimg.com/v2-46721865fecc78edddaa5514e1678c33_1440w.jpg)

我们把这张图表所实现的功能大概标记下，得到：

![](https://pic3.zhimg.com/v2-a1244438bb0d09a3fc5343cb2df72f02_1440w.jpg)

上图中黄色标记为功能块，蓝色标记为导出的 **PBC（Point-Based-Bache）** 【一种 [点云数据](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E7%82%B9%E4%BA%91%E6%95%B0%E6%8D%AE&zhida_source=entity) 格式，可以存储位置等属性信息】，PBC在程序化流程的后半段会被导入引擎，根据属性和Rule Processor完成整座城市的引擎内重建。下面逐一介绍。

### 2.1，Road Generation

创建城市的第一步是明确的定义道路和 [几何体](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%87%A0%E4%BD%95%E4%BD%93&zhida_source=entity) ，道路段由两点构成的样条组成，包含三种类型” **Arterial（主干道）** 【遵循 [最短路径](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84&zhida_source=entity) 原则】， **Collector（区域贯穿道路）** ， **Local（局部街道）** “。

![](https://pic4.zhimg.com/v2-0944b8ccf166f8b37663ee6e2f6e34f9_1440w.jpg)

道路元数据包括”道路宽度，道路ID，每个交叉路口的分支数量“。道路的生成有一个单独的HDA，叫“ **City Road Processor** ”。它有一个输入为“City Layout”，六个输出依次为“ROAD\_NETWORK\_INSTANCE（道路网格实例），POINT\_CLOUD（点云），CITY\_LANES（城市车道），TRAFFIC\_DATA（交通数据），ROAD\_MODULES\_PACKED（道路模块数据），ROAD\_FILLERS（道路填充）”。除此之外，还有一个名为“ **Road\_detailing** ”的SubNetwork用于为道路添加细节

![](https://pic4.zhimg.com/v2-46324f01879242fbb11c4170938a76bb_1440w.jpg)

Road Processor里会根据道路连接的角度，基于准确计算的数量，切割每个路段并为交叉路口留出足够的空间。然后在每个路口放置道路 [切片](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%88%87%E7%89%87&zhida_source=entity) 进行填充，至于每条路的宽度有三种模块可用，分别是20米，10米，5米。每个模块都会以程序化的方式刷上顶点色以供材质使用。还会根据每个道路切片的延申走向评估交通系统数据并对极限角度下的道路进行填充。

![](https://pica.zhimg.com/v2-fd528bd821fb05a1be8f54af04778a06_1440w.jpg)

道路模块数据会被送入Road\_detailing子网络经过细化处理导入 [虚幻引擎](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E8%99%9A%E5%B9%BB%E5%BC%95%E6%93%8E&zhida_source=entity)

![](https://pic1.zhimg.com/v2-ecd0639783b9643cf78b4f62701b675a_1440w.jpg)

### 2.2，Freeway Generation

下一步是生成高速公路，高速公路的交错布局受到制片的影响，因为在一些区域会有追逐场景的需要，因此希望场景中的标志性建筑能够被轻松地识别出来。过场动画部门的需求主要集中在大型匝道口上。City场景（不是Small\_City）的高速路由两个闭环，一个悬垂通道和55个 [入口匝道](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%85%A5%E5%8F%A3%E5%8C%9D%E9%81%93&zhida_source=entity) 组成。

![](https://pic1.zhimg.com/v2-3a306df404dc4741084940a9a6160e04_1440w.jpg)

一个单独的HDA被设计出来以便在虚幻引擎中通过曲线工具形成大型布局，这一前期设计过程由多个部门的设计师和程序化人员反复调整以获得一条完美的追逐路线并确保其在外形和功能上都是适合的，确定高速公路的形状后设计曲线会从UE导回Houdini参与City Layout和City Processor过程。高速路生成与道路生成非常大的一点不同是，高速路没办法完全基于模块的实例化完成。在这种情况下，Mesh是根据区域需要自定义的，整个Mesh会被切分为100m左右的小型网格块以适应流送的需要。

虽然City的文件没有开源出来，但我们还是能通过Small\_City的实现一探究竟。Freeway的核心生成逻辑在“ **Freeway Master** ”的HDA里，它有5个输入，依次是“Freeway Curves（高速路曲线）， Cache Street Curves（缓存的街道曲线），Cache Street Geometry（缓存的街道几何），Cache Street Traffic（缓存的街道交通信息），Building Volume（构建体积）”；四个输出：“FreewayDeckVisible（高速路 [可视化](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%8F%AF%E8%A7%86%E5%8C%96&zhida_source=entity) ）， FreewayDeckCollision（高速路碰撞），FreewayStreetConnection（高速路连接信息表），FreewayStreetPillars（高速路街道立柱）”。 除了Freeway Master还有一些SubNetwork用于对高速路引入后的城市数据进行修正。

![](https://pic1.zhimg.com/v2-a8e2b4c49a58a76ecb6980a33e620f6a_1440w.jpg)

现在将注意力聚焦到Freeway Master HDA本身，图表如下：除了高速路本身和交通连接处的处理，还有其他的装饰性元素比如“路障，柱子，标牌，杂物”等沿高速路分布的实例的逻辑。

![](https://pic3.zhimg.com/v2-4de2063aae0440f62057dec3796d40cc_1440w.jpg)

### 2.3，City Lots Processor

高速路生成完毕后，着手进行地段划分。地块划分由一个名为“ **City\_Lot\_Processor** ”的HDA实现，它有四个输入，依次是"City Layout（城市布局），Freeway（高速路），LandMark Buildings（地标建筑），Height Override（高度覆盖）"；四个输出，依次是“ **Building Volume** （建筑体积），Buiding Subdivided Lot（细化地块），Building RoofTop（建筑屋顶），Building Proxy Geom (用于可视化的 [代理模型](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E4%BB%A3%E7%90%86%E6%A8%A1%E5%9E%8B&zhida_source=entity)) ”。

![](https://pic4.zhimg.com/v2-bdd7cc2cd0f5f4be4761895894710191_1440w.jpg)

因为生成了高速路，所以我们要把这部分区域从原来的地块分布中抠掉，然后在对地块做清理和简化同时重新扩大人行道范围，并引入 [高度数据](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E9%AB%98%E5%BA%A6%E6%95%B0%E6%8D%AE&zhida_source=entity) （这个数据会决定建筑天际线海拔区域），会结合高度和地表覆盖两类评估因素对地块做量化管理， [量化](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=2&q=%E9%87%8F%E5%8C%96&zhida_source=entity) 的目的是提高有效利用率。而地块的高效利用为建筑撒布提供了良好基础。对于后者，我们将 [城市建筑群](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%9F%8E%E5%B8%82%E5%BB%BA%E7%AD%91%E7%BE%A4&zhida_source=entity) 分为高层建筑和底层建筑（PCG生成部分，地标类不包括在内）。高层建筑由 **Building DNA** 控制，低层建筑则直接划分为纽约.布鲁克林街区的风格。

![](https://pica.zhimg.com/v2-003908d799ac024986185fd78e3552b8_1440w.jpg)

这里提到了一个新的概念——Building DNA，通过三类方法控制每一栋建筑的风格样式：一是 **FootPrint** （建筑足迹），它描述了建筑 [横截面](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E6%A8%AA%E6%88%AA%E9%9D%A2&zhida_source=entity) ；二是高度范围，将高层建筑在垂直方向上大体分为三段：第一层，中间层，屋顶层，每一层的高度都可以调整，在建筑构成环节这一块会搭配“ **Shape Grammar** ”（形状语法）对建筑单体做更详细的控制【会放到本文第三部分再详细展开，目前只需要了解建筑大体形态是怎么控制的即可】；三是 **BDF** ，也就是 [建筑风格](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E5%BB%BA%E7%AD%91%E9%A3%8E%E6%A0%BC&zhida_source=entity) 控制【这里是指第一层（最下层）的建筑风格，比如可能是商铺，可能会有雨棚等，通过BDF信息往建筑模块上挂Props】。

![](https://picx.zhimg.com/v2-9553b8524c39ca1fc180d0823327457f_1440w.jpg)

其中FootPrint一共设计了17种，也就意味着地块上可以撒布17种横截面的高层建筑，再加上高度差异的随机化和BDF，以及Shape Grammar提供的模块化控制，理论上我们可以实现无数种建筑造型。FootPrints的定义同样可以在City\_Lot\_Processor中找到：

![](https://pica.zhimg.com/v2-482460c6c371d2a4325247546527e5fe_1440w.jpg)

上文提到，City\_Lot\_Processor会输出一个很重要的内容Building Volume（建筑体积），它是一种全局控制，允许用户引入随机控制城市的整体错落程度

![](https://pic4.zhimg.com/v2-af17123a9e28a505bf5e550d6eff8c37_1440w.jpg)

### 2.4，City Ground &amp; SideWalk

创建地面，也就是城市地表（非道路，建筑覆盖的地方），包括道路两侧的人行道。City Layout已经提供了“人行道样条网格和地块定义以及元数据”。 **City Sidewalk Processor** 这个HDA会使用这些数据将模块撒布到对应位置。

![](https://picx.zhimg.com/v2-e1a4a750b580b7f99cf2354a50ff4097_1440w.jpg)

![](https://pica.zhimg.com/v2-0caa2b3691169d7ff9750a6f702b337a_1440w.jpg)

![](https://pic1.zhimg.com/v2-b37ee3485ed308d3170957c911e3b460_1440w.jpg)

至于地面，我们要减去建筑覆盖的部分，然后再根据地面模块大小布置点云。

除此之外，在地面上还需要放置一些特征元素，按照地面类型（ **Zone types** ）划分这些需要被放置上去的内容可以分成三种：“Plaza（商场地面），Freeway（高速公路下方地面），Parking（停车场地面）”:

![](https://pic3.zhimg.com/v2-97145c065b92f230b37a339c5ffcc71c_1440w.jpg)

它们被认为是Street（街道）的附属元素组件（ **Street Furniture** ），本质上是预包装好的 [资产包](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E8%B5%84%E4%BA%A7%E5%8C%85&zhida_source=entity) ，而实现这些内容的流程被团队称为” **Biomes** “（ [生态群落](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E7%94%9F%E6%80%81%E7%BE%A4%E8%90%BD&zhida_source=entity) ）。为了程序化放置这些Biomes采用了” **基于区域UV空间的分散技术** “（主要基于Houdini的uvlayout功能），同时考虑更好的使用城市布局，开发了” **packing\_scatterer** “HDA（官方译作” **填料撒布器** “）。它的大致原理是会测量每个单独的区域，计算区域的最长边并以此做为主方向参考，然后尽可能以最佳方式把Biomes组合在一起，同时支持不同的模式选择。

![](https://picx.zhimg.com/v2-97b0c4cefe5fd1d3aaf87adef4c29d77_1440w.jpg)

比如官方这个案例：

![](https://pic1.zhimg.com/v2-ef2c548b5de2716731e2e1c2ad6e0298_1440w.jpg)

可以在图表的这一块找到不同Zone Types上的Biomes撒布规则，每一个都封装为一个独立的SubNetwork，子网络中的核心功能都是通过调用packing\_scatterer HDA来实现。

![](https://pic2.zhimg.com/v2-3055089f48734fb77da2f8b8550776dd_1440w.jpg)

### 2.5，City Street Furniture Processor

除了地面区域，Street也有自己的 **Furniture** ，功能实现被封装为一个HDA：“ **City Street Furniture Processor** ”。包括：”Bus Stop（巴士站台），Fire Hydrant（消防栓），Parking Signage（停车牌），Street Lamp（路灯），Trash and Letter Box（垃圾桶和信箱），Traffic Light（交通灯），Border Wall（边境墙）， **Plers Biomes（普勒斯生物群系）** “。

![](https://picx.zhimg.com/v2-216ca6ef7860f4377b54603e887fbbaf_1440w.jpg)

![](https://pic3.zhimg.com/v2-af425cb1e01c306c694601f0313b216c_1440w.jpg)

这样看来，所谓"Furniture"其实就是指街道上可能会出现的那些公共设施，官方有意区分了”Road Furniture“和”City Biomes“这里认为还是有道理的，两者不能混为一谈。概念与分类性的维度这里不做过多讨论，只需要知道”Biomes“和”Furniture“指代的是什么就行。

### 2.6，City Road Decals

三类ZoneTypes, Street都已添加完各自的Dependant Biomes，还剩下Road。Road的细节特征，即”道路贴花“，同样是一个HDA：" **City Decals** "。我们要获取道路创建好之后计算出来的交通道和停车道，输入点信息用于添加贴花。在每个计算点上，会生成一个简单的平面并应用贴花材质

![](https://pica.zhimg.com/v2-b6bce88e48dcee97ae69a676a1da9cf0_1440w.jpg)

![](https://picx.zhimg.com/v2-a4359ce68651827d1bda4f16fa5c16f7_1440w.jpg)

City\_Decals有五个输入，依次是：“Traffic\_Lanes（交通线），Road\_Geom（ [道路几何](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E9%81%93%E8%B7%AF%E5%87%A0%E4%BD%95&zhida_source=entity) ），Sidewalk\_Lanes（人行道线），Road\_Traffic\_Output（道路交通信息），Out\_Bus\_Spaces（巴士区域）”；三个输出，依次为：“Decals（成片的大贴花），Manholes（井盖），Decals\_Small（独立且分散的小贴花）”：

![](https://pic4.zhimg.com/v2-d858a03b2ec8ff3fb8818f6dc9922f7d_1440w.jpg)

HDA内部依次实现了：“ **交叉路口标记，双黄线，白虚线，右转车道分离线，停车标记线， 方向箭头，轮胎标记，井盖，喷漆，斑马线，出租车待客区，公交车待客区** ”，并且大片的贴花做了路面网格适配，可以看到贴花是《黑客帝国》城市道路路面特征的主要贡献者，当然还有一部分和材质有关的特征（比如水坑，补丁，做旧，裂纹，油渍等做到路面材质上的，这些是属于材质和渲染管线的内容，这里暂不讨论）。

![](https://pic1.zhimg.com/v2-b7abb8cf34c981ae98fdafcce935d52e_1440w.jpg)

### 2.7，Audio Generation

UE5提供了一套被称为” **[卷积混响](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=2&q=%E5%8D%B7%E7%A7%AF%E6%B7%B7%E5%93%8D&zhida_source=entity)** “的立体声功能, 对于音频每隔 **3米** 布置一个点，根据城市布局和交通信息区分了15种不同的声音指标：

![](https://pica.zhimg.com/v2-1cfeb5199d63cf5577f7c1094b756368_1440w.jpg)

由于音频采集比较简单，并没有封装单独的HDA或者SubNetwork：

![](https://pic4.zhimg.com/v2-cd104d195a28fdaedf098c0f926eb44f_1440w.jpg)

### 2.8，City Stats

City Processor还提供了一块Stats搜集的功能，这些数据能够量化的展现出当前所生成城市的一些信息，通过这些信息能够很好的指引用户设计出更符合期望的结果，修复漏洞，添加细节等， **整个城市在开发过程中一共重新生成了53次，平均每次全量生成耗费25~30分钟** 。对于整套PCG流程一般能在几个小时内完成，并创建处最终的版本。

![](https://pica.zhimg.com/v2-11f2afe13d1e8e823863084c4303afde_1440w.jpg)

## 三，Building Generation

Building Generation功能在Release项目中【生产流程】实际上是同第二部分所介绍的HDA和SubNetwork一起包进City Processor这一更大HDA内的。

![](https://pica.zhimg.com/v2-4a76888c83794095b7d1e17670b846b2_1440w.jpg)

像建筑原型开发这种创意型工作的展开，团队选择了通过HDA和Houdini Engine直接在UE5内完成。于是开发了 **Building Module Template Generator** 工具，我们在《资产和内容管线》一文中也提到了这个工具。Building Module Template Generator能根据 **Shape Grammar** （形状语法）快速生成建筑的原型样例【 **当然在这之前，TA已经对建筑构成进行了抽象，并抽离出对应的Module，通过这些Module搭配形状语法的驱动逻辑能够生成各式建筑原型（具体解构过程请参考《资产和内容管线》一文）** 】：

![](https://pic4.zhimg.com/v2-edce685f0740c4ee0885b3ea25c6ed93_1440w.jpg)

一旦原型设计完毕，建筑的层级信息和形状构成信息都会被保存进 **JSON** 文件（被称为”建筑定义文件“）。在生产流程中，从JSON创建 **BDF** （Building Definition files）【建筑定义文件】来封装建筑风格。从下面这张图能看出这些数据是如何在建筑生成器内部传播的：

![](https://picx.zhimg.com/v2-217da4e32adba27634b92bd47936040d_1440w.jpg)

输出的最终结果是点云和屋顶几何体，它们会进入城市生成流程，或者通过Houdini Engine送入虚幻引擎。允许从BDF的层级字典中计算出楼层间距，再依此对体积进行切割以划分具体的楼层

![](https://pica.zhimg.com/v2-dc468bb67b3ed01e8d0dc4343a4a3f24_1440w.jpg)

获取楼层切片后可以通过Primitive之间的 [点积](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E7%82%B9%E7%A7%AF&zhida_source=entity) 计算出Corner类型，并按楼层ID逐层处理

![](https://pic4.zhimg.com/v2-107efacb37ad476b811c20114f5c1239_1440w.jpg)

接着会为建筑模块和拐角生成点云，在这个过程中要考虑各种遮挡关系：

![](https://pic1.zhimg.com/v2-27c7ea12673b6802539e04192b820cc4_1440w.jpg)

建筑主体完成后，还有建筑的Props【由建筑ID和地块ID共同决定】以及可以选择在引擎内通过 **Volume Override** 功能添加额外的”防火逃生梯“等配件【但只适用于特定的建筑组合和风格】。至于屋顶的Biomes，则直接来自输入的Building Volume 。

最终的 **Building Generator** 可以在”4.BUILDINGS GENERATOR“的”BUILDINGS“子网络中找到：

![](https://picx.zhimg.com/v2-8039dde14cc1c621a9a495e3601cfc83_1440w.jpg)

![](https://pica.zhimg.com/v2-7c87bcec612f90a320d2eefee7c9c838_1440w.jpg)

Building Generator Graph内部实现过于复杂，考虑了很多种情况，包括Multi BDF，Volume Override，Windows ID等，后面有机会再展开。

## 四，Rebuild City in UE5

引擎内重建过程是使用Rule Processor和Houdini City Processor导出的携带 [点坐标](https://zhida.zhihu.com/search?content_id=250778318&content_type=Article&match_order=1&q=%E7%82%B9%E5%9D%90%E6%A0%87&zhida_source=entity) 和属性信息的PBC文件实现的：

![](https://pic2.zhimg.com/v2-f6efd09cc1176183d8220119057bb0bd_1440w.jpg)

发布于 2024-11-25 01:13・广东[豆包大模型，1000万tokens仅需19.9元，每日限量秒杀中](https://www.volcengine.com/activity/ark?utm_source=7&utm_medium=zhihu&utm_term=vg_zhihu_libao_webtw_dmx19k9&utm_campaign=0&utm_content=dbdmx_19k9&spu=biz%3D0%26ci%3D3635105%26si%3D772e899e-68f2-42cc-8c15-8281af6e7151%26ts%3D1783755632%26zid%3D1629)

[

豆包大模型，字节跳动自研大模型，具有更强的推理能力，多模态理解能力，GUI操作能力和前端页面编程能力，模型...

](https://www.volcengine.com/activity/ark?utm_source=7&utm_medium=zhihu&utm_term=vg_zhihu_libao_webtw_dmx19k9&utm_campaign=0&utm_content=dbdmx_19k9&spu=biz%3D0%26ci%3D3635105%26si%3D772e899e-68f2-42cc-8c15-8281af6e7151%26ts%3D1783755632%26zid%3D1629)

赞同 46