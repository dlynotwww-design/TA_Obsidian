# TRAE Editor for Unity：字节跳动把AI塞进了Unity编辑器，写代码这件事彻底变了

作者: 创艺记
发布时间: 2026年5月23日 21:12
发布地点: 河南

UNITY插件 · AI编程 · 字节跳动

TRAE Editor for Unity：把AI塞进Unity编辑器

GitHub: Pico-Developer/TRAE-Editor-Unity · 2026-05-23

⚠️ 先说结论：字节跳动PICO团队做了一件事——让AI和Unity编辑器在同一个工作流里直接对话。装好插件，双击脚本，TRAE IDE连带AI助手一起就位，你说什么它写什么，不用来回复制粘贴。

## 📖 它到底是什么

TRAE Editor for Unity是字节跳动PICO团队开发的一个开源插件，作用是把TRAE IDE的能力直接嵌入Unity编辑器。

原理不复杂。它本质上做了两件事：

第一件事是让你在Unity里写的C#脚本，能够用TRAE IDE打开。Unity默认的脚本编辑器是MonoDevelop或者Visual Studio，现在你可以把它换成TRAE。

第二件事更关键——TRAE是个带AI能力的IDE，打开脚本的同时，AI助手也跟着一起就位了。你可以让它帮你写新功能、解释一段老代码、或者自动生成你重复写过无数遍的工具类。

GitHub: github.com/Pico-Developer/TRAE-Editor-Unity

## 💎 核心优势，说白了就三点

**第一，无缝继承，该有的都有。**

TRAE Editor for Unity完整承载了TRAE IDE的全部功能，代码高亮、智能提示、调试功能全部保留。

**第二，外部包支持。**

Unity项目经常用到从本地磁盘导入的外部包，这类包跟主工程是分离的。TRAE Editor for Unity会根据你当前打开的脚本路径，把对应的外部包目录作为独立工作区加载，保证代码补全、定义跳转、依赖分析这些功能在完整项目上下文里正常运行。

**第三，内置Unity开发规则。**

插件自带了一套为Unity项目定制的规则文件。每次你通过插件打开项目，这些规则会自动启用，帮助AI更准确地理解Unity的API逻辑。

## 🛠️ 怎么装？5步搞定

1. 在Unity项目里安装插件：Windows → Package Manager → Add package from git URL → https://github.com/Pico-Developer/TRAE-Editor-Unity.git
2. 把TRAE CN设置为外部脚本编辑器：Edit → Settings → External Tools → External Script Editor → Trae CN
3. 在TRAE IDE里装两个扩展：C# Dev Kit + Unity
4. 打开一个脚本试试
5. 开始用AI写代码

## 🧪 SOLO模式实测：我让AI写了一个背包系统

我找了一个真实的Unity小需求测试：写一个简单的背包系统，8个格子，可以放入道具、显示图标、超出上限提示。几秒钟后，背包系统的框架出来了——格子数组、道具数据结构、添加和移除方法。

## 🎯 适合谁用

- Unity初学者，刚学C#，对很多API不熟
- 独立开发者，正在做个人项目
- 之前用ChatGPT辅助写过Unity代码，但一直受困于「需要来回复制粘贴」

## ⚠️ 一个现实的问题：插件还年轻

- 文档目前比较简略
- 插件跟不同版本的Unity兼容性待验证
- 功能迭代速度取决于PICO团队的后续维护

AI写代码这件事，在Web和CLI领域已经相当成熟了。Unity这边的进展一直比较慢。TRAE Editor for Unity正在尝试解决这个问题。它还很年轻，但方向是对的。
