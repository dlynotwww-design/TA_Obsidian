---
title: "[技术美术] 技美篇（十一）：【PCG TA】WFC 波函数坍塌 （一）"
source: "https://zhuanlan.zhihu.com/p/694911664"
author:
  - "[[dreamerflyerAT]]"
published:
created: 2026-06-09
description: "WFC 可以用来动态生成 模型，地图，图片，已经好几年的东西了，现在准备做一些程序化建筑，参考了ue5的wfc部分，深入了解一下这个东东。网上都没找到比较容易理解细致分析过程的资料，不是跳过了算法分析，就是没…"
tags:
  - "clippings"
---
15 人赞同了该文章

WFC 可以用来动态生成 模型，地图，图片，已经好几年的东西了，现在准备做一些程序化建筑，参考了ue5的wfc部分，深入了解一下这个东东。网上都没找到比较容易理解细致分析过程的资料，不是跳过了算法分析，就是没有可视化步骤，搞得还是一知半解。经过两天摸索，消化理解以后，发现其实并不难，比a\*寻路还简单的多。

***个人理解的结论：***

***wfc 原理其实非常简单，主要是大部分人不知道怎么简单明了的去说明白***

WFC 是借用 [量子力学](https://zhida.zhihu.com/search?content_id=242555151&content_type=Article&match_order=1&q=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6&zhida_source=entity) 的量子纠缠时候的（0，1 ）组合的混沌态，把可能性一步步确定成唯一结果的过程，对应游戏程序建模这边，就是生成目标元素时候按一定规则选择哪个元素作为唯一可能性的过程。在这个过程中，可能性一步步减少，直到合理数量时候随机确定一个可能性作为唯一结果，也就是坍塌的过程。两者之间共同点就是几率的不断确定，所以，和量子力学还是有一定关系的。量子力学的几率坍塌是通过人眼观察（原因至今无解，这个就是主观改变客观的世界，也就是玄学！----著名的双缝干涉实验的波粒二象性～），wfc的几率坍塌，最简单就是随机选一种没有规则，高级点的会用一定规则去确定几率高的（这个根据项目需求不同而不同），有点像 重要性采样的思路。

按3d WFC 说明

关键：

1: 规则约束

dir: 元素在另外一个元素的哪个方向.(上，下，左，右，前，后）

rules:就是枚举所有元素按dir约定方向两两组合时候的是否可以组合。这个是核心数据

即，元素A和元素B在dir方向上组合结果(rules\[A\]\[B\]\[dir\]=1 ，可以组合；rules\[A\]\[B\]\[dir\]=0，不可以 ）

2: 每次生成元素时候，选一个在没有被占用的其元素最小可能性的地方，假定为目标位置（tile\_target,tile=\[posibility=min\])，然后按约定方向(dir)，依次遍历这个位置相连的附近位置，如果附近位置有被占用的元素（tile\_neighbor,tile=\[posibility=fixed\]），就在rules里面查找目标位置所有可能的元素和被占用元素在dir方向上去掉 不能组合的可能性，得到更小范围的可能性，即（tile\_target,tile=\[posibility=min-dir\])

3\. 得到更小范围的可能性后，随机选一个元素，把可能性变成1（tile\_target,tile=rand\[posibility=min-dir\])；也就是所谓的坍塌，然后按dir方向遍历附近位置，把对应的元素可能性按坍塌后的唯一元素和相邻元素在dir方向上去掉不能组合的可能性，进一步把附近位置的元素的可能性变少。

4.重复2和3,就可以填满所有位置。（如果可能性变成0，就是不能满足rules约束，也即放弃，停止）

UE5的1d 方向的例子说明（dir 只有左，右）：

![](https://pic1.zhimg.com/v2-35105350db136ffe557ac76f82b40bea_1440w.jpg)

ue5 wfc生成屋顶物体

![](https://pic2.zhimg.com/v2-82805ce34dd1745e7c68cca38b295fb9_1440w.jpg)

约束设置

rules 约束设置，图中可以看出 ，tail可右接body, tail可右接head,tail 可以左接empty,head 不可以左接empty，empty不能左接tail。rules\[tail\]\[tail\]\[right\]=0,rules\[tail\]\[body\]\[right\]=1,rules\[tail\]\[head\]\[right\]=1,rules\[tail\]\[empt\]\[right\]=0;etc...

![](https://picx.zhimg.com/v2-55150109f58ffbf1461c894fe6db6159_1440w.jpg)

每个位置都有4个可能

![](https://pica.zhimg.com/v2-c37ec9780e2f30a9cfc71bce229faef4_1440w.jpg)

随机选了头尾这两个目标位置，最左边左接没有东西，也就左接empty,所以去掉不可以左接empt的头和身体；最右边则去掉不可以右接empty的尾部和身体，可能性都从4减到2

![](https://pic1.zhimg.com/v2-eb87027164ef7ba7cf56246e1deec286_1440w.jpg)

未塌陷的最小可能性是2的位置随机选一个位置进行坍塌，2个可能性减少为1

![](https://picx.zhimg.com/v2-e679c6640d708582098e9a8570952d1b_1440w.jpg)

坍塌后，遍历塌陷相邻的位置，也就是查找坍塌后的tail右接元素的可能性，把相邻位置的元素可能性去掉不能组合的tail和empt，可能性减少成2

![](https://pica.zhimg.com/v2-fcc15f80891aca8843c0eba61c0c4462_1440w.jpg)

在没坍塌过的位置中，选可能性最小为2的随机一个，坍塌一次变成1

![](https://pic1.zhimg.com/v2-cd24d3a5f7e5742fbe76399dc697175a_1440w.jpg)

坍塌后，遍历相邻的位置，也就是查找坍塌后的head右接元素的可能性，把相邻位置的元素可能性去掉不能组合的head和body，可能性减少成2

![](https://pic4.zhimg.com/v2-7ffcb486bff0f3b5a70230633109ed7b_1440w.jpg)

在没坍塌过的位置中，选可能性最小为2的随机一个，坍塌一次变成1,把相邻位置的可能性变成2

![](https://picx.zhimg.com/v2-2742c80692bd50643e5904960fbd8755_1440w.jpg)

在没坍塌过的位置中，选可能性最小为2的随机一个，坍塌一次变成1

![](https://pic2.zhimg.com/v2-80cfeb6864ac7250eac6bd7a0ae2feb1_1440w.jpg)

坍塌后，遍历相邻的位置，也就是查找坍塌后的head左接元素的可能性，把相邻位置的元素可能性去掉不能组合的head和empty，可能性减少成2

![](https://pic1.zhimg.com/v2-0eaeb438a05232fb8080d77998713f7a_1440w.jpg)

在没坍塌过的位置中，选可能性最小为2的随机一个body，坍塌一次变成1,把左接相邻位置的元素可能性去掉不能组合的empty,可能性变成1

![](https://pic4.zhimg.com/v2-c9806f3a842b013352146cfe3120d401_1440w.jpg)

在没坍塌过的位置中，选可能性最小为1的，直接选，这也是最后一个没坍塌的位置，结束！

编辑于 2024-04-28 12:35・上海[坍塌](https://www.zhihu.com/topic/21261097)