---
title: "《InsideUE5》GameFeatures架构（一）发展由来"
source: "https://zhuanlan.zhihu.com/p/467236675"
author:
  - "[[大钊]]"
published:
created: 2026-07-03
description: "许久不见，甚是怀念 引言新的一年，新的征程。许久没更新本专栏了，一是懒，二是没想到什么特别合适的主题。不过趁着过年期间整理一下以前的技术分享成文章。 GameFeatures的话题，我在UOD2021会上做过一期技术分…"
tags:
  - "clippings"
---
[收录于 · InsideUE5](https://www.zhihu.com/column/insideue4)

MarsZhou、北京TA吴强 等 531 人赞同了该文章

目录

收起

引言

目录摘要

一，发展由来

1\. 内建GamePlay框架

2\. GameAbilitySystem技能框架

3\. Subsystem系统

4\. GameFeatures是什么？

5\. 为什么需要GameFeatures？

总结

> 许久不见，甚是怀念

## 引言

新的一年，新的征程。许久没更新本专栏了，一是懒，二是没想到什么特别合适的主题。不过趁着过年期间整理一下以前的技术分享成文章。 GameFeatures的话题，我在UOD2021会上做过一期技术分享： [《虚怀若谷-模块化游戏功能框架》](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1j34y1B7Nf) ，感兴趣的可以自己参阅。本篇文章是基于自身学习GameFeatures时整理的技术资料，会比UOD2021会上的分享更加的详尽一些，毕竟现场时间有限，而且不能手把手太过详细的教授。

## 目录摘要

正题之前，也请容许我继续唠叨几句。在文章的最开头，理应让你知道后续的内容结构，以便让你决定是否有研读下去的必要，还是直接goto点赞。 我最早注意到GameFeatures是在UE5 EA公布的时候，其配合 [《古代山谷》](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E3%80%8A%E5%8F%A4%E4%BB%A3%E5%B1%B1%E8%B0%B7%E3%80%8B&zhida_source=entity) 项目一起亮相。一言以概之， **GameFeatures是UE5推出的一个支持动态装载游戏玩法的框架。** 官方在那之后也做过两期直播：

- [\[功能介绍\]UE5中的模块化游戏功能：即插即用，虚幻之道(官方字幕)](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1dL4y1h7YW/)
- [\[英文直播\]模块化游戏功能(官方字幕)](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1g34112799/)
- [\[UOD2021\]虚怀若谷-模块化游戏功能框架 | Epic Games 大钊(官方字幕)](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1j34y1B7Nf/) (顺便加上我自己的)

不过个人学习之后，觉得讲解得并不够深入。其更多是注重表层的使用，只能告诉你这个是什么，大概怎么用，并不能告诉你如何去用好它，而这正是我们最需要的东西！我自己在学习完那两个直播的最大感受也是，哦你给我科普了一下这个是什么，但是我自己回过头还是得自己去翻源码学习个透彻了才敢有一定的信心能用好它，否则面对着UE编辑器却依然无从下手一脸懵逼心浮气躁怀疑人生。有感于此，关于GameFeatures的讲授，将分为四个大部分：

1. **发展由来** ，简单介绍一下Epic开发这套框架的初衷，让大家知道背后的缘由，以及为什么需要它。
2. **基础用法** ，开始上手GameFeatures。会从零开始讲解开始创建一个GameFeature的各个步骤，你遵照着来就一般不会有什么问题，因为它确实用起来很方便简洁的，我有信心它绝对不会难倒你。
3. **[框架机制](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E6%A1%86%E6%9E%B6%E6%9C%BA%E5%88%B6&zhida_source=entity)** ，我会剖析GameFeatures框架背后的一些流程和原理，让大家更清楚背后的工作机制，做到用起来心里有数不慌，也懂得在合适的地方进行扩展。这部分内容是文章的重点，我也会花更多的篇幅在这里。想要透彻讲解一个框架的方方面面是一件常常顾此失彼的事，有 [内核机制](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E5%86%85%E6%A0%B8%E6%9C%BA%E5%88%B6&zhida_source=entity) 有表层使用，有大流程也有小扩展，但我会尽我之力把我脑子里的所有东西表述出来。希望好文章不怕长！
4. **[最佳实践](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5&zhida_source=entity)** ，如何用好GameFeatures，学习之后我们就必须得有能力尝试回答这个问题。因此这里我会同时站在框架设计者和使用者的两种视角，来回答一些大家在使用GameFeatures时候的可能疑问，还有我比较推荐的做法。
5. **祝你好运** ，最后当然还是得需要你自己的实践才能出真知。把学习到的知识转换成你自己的，也欢迎在遇见问题的时候同我交流。

## 一，发展由来

GameFeatures作为GamePlay的新发展出来的一套框架，究其发展，就不得不回顾历史盘点手上的现有工具们。

### 1\. 内建GamePlay框架

最早的最基础的当然要属于引擎的内建GamePlay框架，这部分相信大家也是都非常了解了。这套GamePlay框架其实也是随时代一直在进化的，从UE3时代比较简单的功能，进化到UE4的这些，然后再到UE5的WordPartition，LevelInstance等功能。可以说这些基本的Game Play类构成了引擎的核心玩法框架基石。它们提供的功能也很丰富，场景编辑、 [序列化](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E5%BA%8F%E5%88%97%E5%8C%96&zhida_source=entity) 、网络同步，生命周期等。一个初级开发者就可以直接利用这些基本的类开发出游戏雏形。这些类我都有写过文章详细讲述过，就不赘述了。

![](https://pica.zhimg.com/v2-a5a9d38c36e4c74e650862cdf1265dd6_1440w.jpg)

### 2\. GameAbilitySystem技能框架

再之后随着玩法的复杂化，游戏里常常会需要丰富多样的技能。这就要求游戏玩法框架也能实现一套复杂的技能系统，同时我们还希望它易于扩展、易于配置、易于协作且还能支持联机。《 [堡垒游戏](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E5%A0%A1%E5%9E%92%E6%B8%B8%E6%88%8F&zhida_source=entity) 》的技能多样化需求也一直催生着 [GAS框架](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=GAS%E6%A1%86%E6%9E%B6&zhida_source=entity) 的进化。GAS的文章和教程网上已经有一些了，我去年UOD也录过一期专门讲解GAS里各个组件的技术分享： [\[UnrealOpenDay2020\]深入GAS架构设计 | EpicGames 大钊](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1zD4y1X77M/) 。大家有兴趣可以回头再去学习一下。

![](https://pica.zhimg.com/v2-daab184f1054ef2f7f05e603e84dda46_1440w.jpg)

### 3\. Subsystem系统

再之后是Subsystem系统，我在知乎上也写过一篇长文来讲解这个系统([《InsideUE4》GamePlay架构（十一）Subsystems](https://zhuanlan.zhihu.com/p/158717151))。UE在4.22版本的时候，开始引入Subsystems，然后在4.24完善。简单来说，Subsystems允许你从已经预定义的5个类中继续下来，并自动实例化和托管生命周期，用起来非常省心。 当你在代码里发现要写一个Manager类的时候，就很可能是把它换成Subsystem的好时机。 现在引擎代码的趋势是把越来越多的模块用Subsystem来管理，包括接下来要介绍的GameFeatues框架也有个GameFeatureSubsystem。

![](https://pic2.zhimg.com/v2-217c0403d33d75a5ebd34c69747c5221_1440w.jpg)

### 4\. GameFeatures是什么？

终于说到GameFeatures，那它是一套什么东西呢？GameFeature其实就是一种比较特殊的插件，这些插件共同组成了游戏的整体玩法。普通的插件为游戏提供了一些基础功能的封装，例如数据库读取、EOS等这种功能。而游戏玩法上的插件，就可以说是GameFeature。我们利用这个 [插件框架](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E6%8F%92%E4%BB%B6%E6%A1%86%E6%9E%B6&zhida_source=entity) ，可以把一种玩法封装成一个插件，在运行时动态的开关这个插件，从而改变游戏的玩法。这么说起来和MOD意味还有点像，只不过MOD是一般通过直接修改游戏本体而实现的。 如果把一个游戏比喻成一台主机，那GameFeature就是像USB那样 [热插拔](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E7%83%AD%E6%8F%92%E6%8B%94&zhida_source=entity) 加上的功能，而Plugin的话就是类似插在 [主板](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E4%B8%BB%E6%9D%BF&zhida_source=entity) 上的内存 [显卡](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E6%98%BE%E5%8D%A1&zhida_source=entity) 等这种更基础的功能。

![](https://pic3.zhimg.com/v2-6770d97ec38d9ece7c24be2ece717e22_1440w.jpg)

这个比喻有点傻，不过却隐含了一些机制的道理：

- 谁更基础。插在主板上的硬件显然要比USB设备要更基础一些。因此Plugin也是用于实现相比GameFeature更加基础的功能的，比如网络通信SDK这些。而GameFeature是用于实现“玩法”的。
- 依赖顺序。如果把PC主机机箱比作我们的游戏项目CoreGame，则显然CoreGame是依赖于Plugin的，就像主板要依赖主板插槽上的设备。而USB设备显然要依赖于主机的功能，因此GameFeature是依赖于CoreGame的。
- 易变性。主板上的设备显然一般是插在上面就好了不会插来拔去，也一般不会在开机运行状态下热插拔，就像Plugin一般也是随着游戏打包编译到 [发行包](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E5%8F%91%E8%A1%8C%E5%8C%85&zhida_source=entity) 里去的，一般也不会在运行时动态的加载释放。而USB设备的热插拔就是常规操作了，就像GameFeature设计之初就是用来在运行时开关某个游戏功能的。
- 底层本质一致。如果我们深究一下，会发现内存显卡等设备和USB设备其本质其实也都是通过某种接口“插在”主板上的，其实是一种共通的机制。因此GameFeature其实也是一种Plugin，也是依托于Plugin的机制实现的。

这么想来，我这个比喻真是妙啊！不经意间触碰到了一丝天道！如果用更简洁一点的图来表示：

![](https://pic1.zhimg.com/v2-229df58f3604219de3809b9116265e2c_1440w.jpg)

一个Game由众多的Plugin组成，其中一些Plugin用来实现继承功能，另外一些Plugin即GameFeature用来实现额外的玩法。言尽于此，希望读者对此有个笼统的大概念。依然不明就里也不打紧，下文更细细道来。

### 5\. 为什么需要GameFeatures？

按理说基础的内建GamePlay框架、GAS、Subsystem这些功能已经挺强大，我们也用得挺顺手的，也开发出了众多的游戏，何必无事生非多出一个GameFeature呢？啊，时代在进步，命运在呼唤。一些问题只有在 [项目开发](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E9%A1%B9%E7%9B%AE%E5%BC%80%E5%8F%91&zhida_source=entity) 运营经历积累到一定时期了才展现出来，新的问题催生新的方案。以Epic的自家游戏 [《堡垒之夜》](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E3%80%8A%E5%A0%A1%E5%9E%92%E4%B9%8B%E5%A4%9C%E3%80%8B&zhida_source=entity) 为例，在其开发过程中，随着每次赛季更新和活动内容迭代，也会很快就发现在玩家的 [Pawn类](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=Pawn%E7%B1%BB&zhida_source=entity) 里开始充斥了几千行代码和上百个方法。逐渐就变得难以维护和难以查错。每次要做个活动加点新内容，就得在Pawn里添加特定的方法，开发过程逐渐就变成一种苦痛负担。玩家一时爽，开发苦断肠。

![](https://pica.zhimg.com/v2-3f7e406b6de0c603b35ed2522db7a356_1440w.jpg)

因此我们需要一种 **模块化** 的逻辑组织方式，这就是GameFeatures的由来。虽然Subsystem和GAS在框架的某些方面都提供了解耦的作用，但GameFeatures更进一步，允许在“游戏功能”这个 [颗粒度](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E9%A2%97%E7%B2%92%E5%BA%A6&zhida_source=entity) 上进行解耦。

这种方式还为我们提供了这些优点：

- 团队内新人更易上手，因为无需了解项目内其他内在 [工作机制](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=2&q=%E5%B7%A5%E4%BD%9C%E6%9C%BA%E5%88%B6&zhida_source=entity) ，就能开发这些独立功能。他可以创建一个GameFeature然后独立的开发和测试。
- 更少漏洞，更易读代码。因为GameFeature本身是独立自包含的，因此代码天然更易于进行单元测试，可以自然地避免在构建时意外或偶然地依赖其他代码。
- 更轻松的在多个团队或项目中共享功能，可以更容易的迁移插件模块。在以往我们虽然也幻想一个游戏功能模块可以从一个项目复用到另一个项目，但这些一般都是偏向玩法无关的功能模块。因为游戏玩法模块一般来说都合作得很“紧密”，耦合得很深，一般也很难干净拆出来复用。而GameFeatues则至少为我们提供了一个解决方向，把一些独立玩法封装成GameFeatue，则至少大大增大了复用的可能。
- 更容易在大型或 [分布式开发](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E5%88%86%E5%B8%83%E5%BC%8F%E5%BC%80%E5%8F%91&zhida_source=entity) 环境中协作，模块化总是能促进团队协作，更少的担心自己的修改会干涉到别人的功能。
- 更容易在“快迭代更新”游戏中迭代功能，也能快速安全的删除出现问题的功能。当前游戏业是越来越多的网游了，因此这些长运营的游戏一般也都得不停的迭代更新功能，在开发过程中，把这些要更新出去的功能以GameFeature的方式一小包一小包的模块化分发出去，显然更容易开发和管理。万一哪个玩法包出错了，也可以及时动态的关闭它，而不影响游戏本体的功能。我知道有些小伙伴到这可能已经想到可以把GameFeature利用到 [热更新](https://zhida.zhihu.com/search?content_id=191961070&content_type=Article&match_order=1&q=%E7%83%AD%E6%9B%B4%E6%96%B0&zhida_source=entity) 去了，但这就是另一个大话题了。提前来说，GameFeatues从机制上来说已经支持从网络上下载来加载，但目前来说实现还不够完善。当然把一个GameFeatue打包成pak，再下载加载也是可以的。

## 总结

希望看到这，能引起你的兴趣来继续学习GameFeatures这个框架。对于每个UE程序员来说，只要工作中有涉及到GamePlay部分，我觉得都有必要来学习一下。因为GameFeatures新的思想和代码资源组织方式，必然会对项目的整体架构产生深远的影响，从而影响到每个人的工作内容涉及部分。鉴于篇幅太长，GameFeatures系列将分为几篇讲述。下一篇很快就会开始讲解基础用法，再会。

下一篇： [大钊：《InsideUE5》GameFeatures架构（二）基础用法](https://zhuanlan.zhihu.com/p/470184973)

*UE 5.0.0*

——————————————————————————————————————

知乎专栏： [InsideUE4](https://zhuanlan.zhihu.com/insideue4)

UE深入学习QQ群： **456247757** (非新手入门群，请先学习完官方文档和视频教程)

**个人原创，未经授权，谢绝转载！**

编辑于 2026-03-04 17:35・上海[AI时代下，图形化编程、Python、C++怎么选？](https://zhuanlan.zhihu.com/p/27288158021)

[

在少儿编程学习中，目前 图形化编程、Python、C++这三种语言最为流行，那么在现今这个科技发达、人工智能发展的时代，选择哪门编程语言最有用？怎么选择更适合孩子？学完后对孩子有什...

](https://zhuanlan.zhihu.com/p/27288158021)

赞同 531