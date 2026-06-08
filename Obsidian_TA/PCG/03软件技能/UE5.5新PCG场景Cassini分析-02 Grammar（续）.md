---
title: "UE5.5新PCG场景Cassini分析-02 Grammar（续）"
source: "https://zhuanlan.zhihu.com/p/1928843897972463613"
author:
  - "[[TheTus请输入文本]]"
published:
created: 2026-06-09
description: "前言书接上文 UE5.5新PCG场景Cassini分析-01 Grammar在这个场景中还有一个通过Grammar创建体积建筑的实例。下面对它进行分析。 创建横截面PolyLine首先，我们需要将场景中的图元（Box）的横截面转换为Spline（Poly…"
tags:
  - "clippings"
---
8 人赞同了该文章

目录

收起

前言

创建横截面PolyLine

按Grammar复制横截面

分层应用Grammar

地板和天花板

放置模型

## 前言

书接上文

[![](https://pic1.zhimg.com/v2-23bbeffa44fe225bd5e039827392655e.png?source=7e7ef6e2&needBackground=1)](https://zhuanlan.zhihu.com/p/1928475578874468068)

![](https://pica.zhimg.com/v2-8ebdf055c4603ffb423ed488c5890514_1440w.jpg)

Cover-1

在这个场景中还有一个通过Grammar创建体积建筑的实例。下面对它进行分析。

## 创建横截面PolyLine

![](https://pic2.zhimg.com/v2-30ced0f90050edfc34ba22cafaa25201_1440w.jpg)

创建横截面PolyLine

首先，我们需要将场景中的图元（Box）的横截面转换为Spline（PolyLine），以方便后面应用Grammar。

![](https://pic4.zhimg.com/v2-bfe6eeb098ec6b95ea20ea6c33b0aac7_1440w.jpg)

GetPrimitivesAndBUildCrossSecetion

首先，通过 **Get Primitive Data** 获取场景中，在 [Volume](https://zhida.zhihu.com/search?content_id=260423075&content_type=Article&match_order=1&q=Volume&zhida_source=entity) 内的所有Tag为 `MeshBuildingTag` 的图元。

然后，使用 **Primitive Cross-Section** 创建这个图元的横截面PolyLine。

![](https://pic4.zhimg.com/v2-1feb96513e8daca35e991b9af49a4b71_1440w.jpg)

PrimitiveCrossSection

这个节点的流程大概是将输入图元布尔合并为几个DynMesh，然后简化共面三角形（这里好像并没有 `Minimum Coplanar Vertices` 参数的参与），然后通过 `Slice Direction` 计算切片方向投影，应用 `Tier Merging Threshold` 进行分层切割，通过 `Min Area Culling` 剔除小于这个面积的横截面。

节点会输出多组PolyLineData，并添加一个 `ExtrudeVector` 属性，它代表当前横截面到下一个横截面的向量（非归一化）。

## 按Grammar复制横截面

![](https://pic2.zhimg.com/v2-4f0122fdc0db4d84be41ee9d78caf2f7_1440w.jpg)

复制横截面

接下来，我们需要横截面按照Grammar规则垂直排列。

![](https://pic3.zhimg.com/v2-c5eedfc81c6707dcdcf730235fdd589c_1440w.jpg)

DuplicateCrossSection

首先，将Grammar的属性通过 **Add Attribute** 添加给PolyLineData。Grammar为 `MainFloor,Second,Third,Top*` 。

然后，使用 `Duplicate Cross-Sections` 应用Grammar对PolyLine进行复制。它会在输入PolyLine沿着 `ExtrudeVector` 复制，并应用Grammar对Modules Info进行附加。

![](https://pic4.zhimg.com/v2-03a50e09236c4bb75c5f0993353097dd_1440w.jpg)

DuplicateCrossSection-1

## 分层应用Grammar

这一步的目的是对上一步复制出来的不同层的Grammar横截面上，对应的应用不同的Grammar进行这一层进行分割。

![](https://picx.zhimg.com/v2-c18bc8d0729f2bfd28e22c5e4a0c6ae5_1440w.jpg)

分层应用Grammar-1

首先，通过 **Spline Direction** 将PolyLineData绕序改为逆时针。

然后，为了能对样条线的每一段（而非PolyLineData存储的节点）进行 **Subdivide Segement** 的划分，我们需要通过 **Spline to Segment** 将PolyLineData转换为控制点的PointData。它会把PolyLineData存储的节点转换为两个控制点，控制点在线段中心且沿样条线， `ScaledLocalSize.X` （ `BoundsMax.X-BoundsMin.x` ）为线段长度，并会增加例如 `SplineIndex` / `PreviousAngle` / `SegmentIndex` 等。

![](https://pic1.zhimg.com/v2-15a54f0623e6f7b075bea93f94fc8172_1440w.jpg)

SplineToSegment

![](https://picx.zhimg.com/v2-4477a7c28b2143255e90389acef954bf_1440w.jpg)

SplineSegment

有了这些Segment的PointData，就可对这些Segment进行语法的附加。 **Select Grammar** 支持根据PointData在某属性的建对匹配关系上，通过属性比较选择一个语法。例如在这个例子中，首先通过 `Symbol` 属性作为Key在Criteria序列中进行匹配。再通过 `ScaledLocalSize.X` （Segment长度）对匹配的Grammar进行选择。Criteria序列选择从上往下，直到匹配Grammar。

![](https://pic3.zhimg.com/v2-8dfb941da79aabbf9623b5b1f2084296_1440w.jpg)

SelectGrammar

这一段的意思就是如果这一条线段距离过短，就放一个Filler填充物。否则就填充更多东西。Grammar的排列是首尾进行的，即会先满足两端的Filler放置，然后是Column，再有空闲位置再放置Wall/Port等。

最后，通过 **Subdivide Segment** 通过Grammar进行分割，它的用法和上一章的 **Subdivide Spline** 类似，前者输入PointData，后者PolyLineData。

## 地板和天花板

![](https://pic4.zhimg.com/v2-05efde573074c5b5d3f36cdc2ba9d84b_1440w.jpg)

地板天花板

这一步是提取底层（和顶层）PolyLineData，进行Interor的采样分割成多个PointData。

![](https://pic3.zhimg.com/v2-b6c5cc9fab1c8e872e6ba516691acef2_1440w.jpg)

地板天花板-1

分析Cargo Floor Ceiling SG。

首先，获取底层和顶层（虽然顶层最终没用上）。

![](https://pica.zhimg.com/v2-6587e65f1c427a44e3f36346f99dcef4_1440w.jpg)

获取顶层和底层

**Data Count** 的作用是返回 [PCGDataCollection](https://zhida.zhihu.com/search?content_id=260423075&content_type=Article&match_order=1&q=PCGDataCollection&zhida_source=entity) 数组的数量， **Filter Data By Index** 用来返回指定索引的PCGTaggedData。

之后，按理来说就可以直接对Spline进行On Interor的采样进行PointData的格子分割了。但这有一个bug，当Interor面积放不下最后一个格子的时候会被舍弃，导致不能完美封边。

![](https://pic1.zhimg.com/v2-6de3bc01c7a6aacc20ae32ad5ff7099e_1440w.jpg)

封边bug

所以做法应该是算出到每个节点能放多少个格子（向上取整），然后以格子的数量×格子尺寸决定长度。

![](https://pic2.zhimg.com/v2-7d972aa5a3315abaf90a908065a38107_1440w.jpg)

按格子数量计算长度

先通过到Local原点距离能放的格子数量计算实际坐标，然后创建新的Spline进行 `On Interor` 的采样。这里复制了一个Index到IndexBCK进行Sort，实际上直接对Index排序也是可以的。

最后，把底层复制上去当作顶层（所以第一步提取顶层没用上）。

![](https://pic2.zhimg.com/v2-becbc8b1518147238b0aba9d440a38eb_1440w.jpg)

复制底层

## 放置模型

还是如法炮制的放置模型流程，在上一章已经总结过了。

![](https://picx.zhimg.com/v2-e1ae80819a99f6c40f84eee728890b39_1440w.jpg)

放置模型-1

另外，这里的Branch也是没有用的，并没有用到Material的Attribute。

编辑于 2025-07-16 16:00・广东[如何写代码？豆包一键实现，程序员必备！](https://www.doubao.com/chat/?channel=dbweb_zhihu_xxl_pc_cpc_ty_aibc_bchx_516&source=dbweb_zhihu_xxl_pc_cpc_ty_aibc_bchx_516&keywordid=3734831&ad_platform_id=zhihu_feed_lead&ug_callback_url=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D8149e914-9971-4621-a4d9-b5e98845c7f0%26os%3D3%26zid%3D1629%26zaid%3D3744384%26zcid%3D3734831%26cid%3D3734831%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3Dc385da58e76fb6ebb431862bd3a5480e%26adv%3D784531%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1Gdx87VSAsMi9Cb1cXISFcCiIEeh4yNyw9GGJBRCUlVFZ0DngJcmN3ehFkUwBkfwNZY1YkXSo-fX4DPhIMZXsBW3MIeQ16WP4GpNhnsOE%3D&cb=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D8149e914-9971-4621-a4d9-b5e98845c7f0%26os%3D3%26zid%3D1629%26zaid%3D3744384%26zcid%3D3734831%26cid%3D3734831%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3Dc385da58e76fb6ebb431862bd3a5480e%26adv%3D784531%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1Gdx87VSAsMi9Cb1cXISFcCiIEeh4yNyw9GGJBRCUlVFZ0DngJcmN3ehFkUwBkfwNZY1YkXSo-fX4DPhIMZXsBW3MIeQ16WP4GpNhnsOE%3D&ug_semver=v1.0.0&spu=biz%3D0%26ci%3D3734831%26si%3Dfe4e1d01-33c8-4816-8280-21bc97541afc%26ts%3D1780938324%26zid%3D1629)

[

编程大佬们都在用的豆包AI!爬虫、写代码、修复bug...

](https://www.doubao.com/chat/?channel=dbweb_zhihu_xxl_pc_cpc_ty_aibc_bchx_516&source=dbweb_zhihu_xxl_pc_cpc_ty_aibc_bchx_516&keywordid=3734831&ad_platform_id=zhihu_feed_lead&ug_callback_url=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D8149e914-9971-4621-a4d9-b5e98845c7f0%26os%3D3%26zid%3D1629%26zaid%3D3744384%26zcid%3D3734831%26cid%3D3734831%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3Dc385da58e76fb6ebb431862bd3a5480e%26adv%3D784531%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1Gdx87VSAsMi9Cb1cXISFcCiIEeh4yNyw9GGJBRCUlVFZ0DngJcmN3ehFkUwBkfwNZY1YkXSo-fX4DPhIMZXsBW3MIeQ16WP4GpNhnsOE%3D&cb=https%3A%2F%2Fsugar.zhihu.com%2Fplutus_adreaper_callback%3Fsi%3D8149e914-9971-4621-a4d9-b5e98845c7f0%26os%3D3%26zid%3D1629%26zaid%3D3744384%26zcid%3D3734831%26cid%3D3734831%26event%3D__EVENTTYPE__%26value%3D__EVENTVALUE__%26ts%3D__TIMESTAMP__%26cts%3D__TS__%26mh%3Dc385da58e76fb6ebb431862bd3a5480e%26adv%3D784531%26ocg%3D0%26cp%3D0%26ocs%3D0%26aic%3D0%26atp%3D0%26ct%3D0%26ed%3DGiBNJgVzfCMmUW9XFyEvRA8xBGxJICwkOhh0FlwxKw1Gdx87VSAsMi9Cb1cXISFcCiIEeh4yNyw9GGJBRCUlVFZ0DngJcmN3ehFkUwBkfwNZY1YkXSo-fX4DPhIMZXsBW3MIeQ16WP4GpNhnsOE%3D&ug_semver=v1.0.0&spu=biz%3D0%26ci%3D3734831%26si%3Dfe4e1d01-33c8-4816-8280-21bc97541afc%26ts%3D1780938324%26zid%3D1629)