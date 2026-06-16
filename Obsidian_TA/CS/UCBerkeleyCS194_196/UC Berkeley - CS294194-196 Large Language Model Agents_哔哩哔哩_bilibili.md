---
title: "UC Berkeley - CS294/194-196 Large Language Model Agents_哔哩哔哩_bilibili"
source: "https://www.bilibili.com/video/BV1STZuBQEs7/?spm_id_from=333.1387.favlist.content.click&vd_source=089349bc15fe4a0508fc235b6d5563a8"
author:
  - "[[常青藤名校课]]"
published: 2026-02-16
created: 2026-06-16
description: "UC Berkeley - CS294/194-196 Large Language Model Agents共计12条视频，包括：LLM Reasoning by Denny Zhou、LLM Agents: History & Overview by Shunyu Yao、Agentic AI Frameworks/AutoGen & Multimodal等，UP主更多精彩视频，请关注UP账号。"
tags:
  - "clippings"
---
##  History & Overview by Shunyu Yao

[LLM Agents MOOC | UC Berkeley CS294-196 Fall 2024 | LLM Agents: History & Overview by Shunyu Yao](https://www.youtube.com/watch?v=RM6ZArd2nVc&list=PLGK6tAsp1smbj8Ga4JHcgzGNbXArity-c&index=2)

这段视频由 **Shunyu Yao** 主讲，深入探讨了大语言模型（LLM）智能体的历史、现状与未来方向。以下是该视频内容的详细概述：

### 1. LLM 智能体的定义与分类

讲座首先定义了什么是**智能体（Agent）**：它是一个能与环境（物理环境如机器人，或数字环境如软件、人类）交互的智能系统。视频提出了三个层次的概念：

- **文本智能体（Text Agent）**：通过语言进行观察和行动的智能体。
- **LLM 智能体**：使用大语言模型来执行行动的文本智能体。
- **推理智能体（Reasoning Agent）**：这是目前最先进的阶段，即智能体利用 LLM 进行推理并据此采取行动。

### 2. 历史演变与技术范式的收敛

视频回顾了智能体的发展历程，指出从早期的规则驱动（如 1960 年代的聊天机器人 Elisa）到强化学习（RL）驱动的文本游戏，都存在领域局限性且训练成本高。

- **推理与行动的合流**：研究者发现，单纯的“推理”（如思维链 Chain of Thought）缺乏外部知识，而单纯的“行动”（如检索增强生成 RAG 或工具调用）缺乏逻辑思考。
- **ReAct 范式**：这是视频重点介绍的创新点。**ReAct (Reasoning + Acting)** 结合了两者，通过让模型生成“思维-行动-观察”的轨迹来解决问题。这种方式模仿人类，让推理引导行动，行动反馈又进一步修正推理。

### 3. 核心技术：推理作为内部行动与长期记忆

- **推理的本质**：与以往固定动作空间的智能体不同，推理智能体的行动空间是无限的语言空间。推理是一种“内部行动”，它不改变外部世界，但会改变智能体自身的上下文和记忆。
- **长期记忆（Long-term Memory）**：当前的 LLM 受限于上下文窗口（短期记忆），容易像“金鱼”一样遗忘。通过**自我反思（Reflection）**，智能体可以从失败中学习，并将经验存入长期记忆，从而在下次任务中表现更好。

### 4. 实际应用与数字自动化

LLM 智能体推动了**数字自动化**的发展，使其超越了简单的问答。视频举了几个前沿例子：

- **WebShop**：智能体像人类一样浏览网页、搜索并购买商品。
- **软件工程**：智能体可以根据 GitHub 上的 Issue 自动修复代码漏洞。
- **科学发现**：利用推理智能体分析化学数据并提出新的化学合成方案。

### 5. 未来研究方向

主讲人提出了五个值得关注的未来课题：

- **训练（Training）**：不仅是预测下一个 Token，更需要针对智能体的思维和评估过程进行专门训练。
- **接口（Interface）**：为智能体设计更优的环境（如为模型优化的文件搜索命令），而非仅仅沿用人类的界面。
- **鲁棒性（Robustness）**：在现实任务（如客服）中，追求 100% 的成功率比偶尔一次的高分更重要。
- **人类参与（Human-in-the-loop）**：智能体需要与人类进行多轮交互以明确需求。
- **基准测试（Benchmark）**：建立更具挑战性、更贴近现实世界的评估体系。

最后，视频总结道，优秀的科研工作往往是**简单且通用**的（如 ReAct），这需要研究者具备抽象思考的能力，并从历史和其他学科中汲取灵感。
