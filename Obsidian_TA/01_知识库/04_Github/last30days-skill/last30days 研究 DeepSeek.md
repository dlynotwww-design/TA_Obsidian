---
title: "last30days 研究 DeepSeek"
source: "last30days"
created: 2026-06-20
tags:
  - AI
  - DeepSeek
  - research
  - last30days
---
# DeepSeek：过去30天发生了什么

🌐 last30days v3.6.0 · synced 2026-06-20

## 我的发现

**本月最大新闻：¥500亿融资 + 84% 创始人控制权** — DeepSeek 在 6 月完成了成立以来的首轮外部融资，总额超过 ¥5000 亿（约 $74 亿），投后估值约 $520-590 亿。梁文锋个人出资 ¥200 亿（约 $28 亿），腾讯 ¥100 亿、宁德时代约 ¥50 亿跟投。交易结构前所未有：外部资金注入梁文锋控制的有限合伙企业，投资者仅享有财务收益权，无投票权、无董事会席位、锁定五年，据 [SCMP](https://scmp.com) 报道。CNBC 披露条款中包含"不挖角 DeepSeek 员工"的承诺。这笔钱不是补资金缺口——目的是给员工期权做市场化定价以留住人才，同时绑定国家大基金获取国产算力优先供给。在 [r/DeepSeek](https://www.reddit.com/r/DeepSeek/comments/1toz1zn/can_we_talk_about_how_deepseeks_impact_on_ai/)，社区认为这是那场迫使小米数天后砍价 MiMo 的价格革命的延续："DeepSeek 公开了架构、基础设施的每一个细节……现在其他人都能从这项研究受益。"

**V4 技术很强，但市场的游戏已经换了** — DeepSeek V4 在沉默 15 个月后于 4 月 24 日发布：1.6 万亿参数，100 万 token 上下文窗口，MIT 开源协议。在 Vibe Code Benchmark 上以压倒性优势拿下开源权重模型第一名，击败了 Gemini 3.1 Pro。Replit CEO Amjad Masad 称赞其注意力压缩机制是"真正的架构创新"。但主导叙事，据 [36Kr](https://36kr.com) 和 [SemiAnalysis](https://semianalysis.com)，是"叫好不叫座"：2026 年的竞争已经从模型基准测试转向了 AgentOS。开发者现在说"我用 Claude Code"或"我用 Codex"，而非"我用某个模型"。DeepSeek V4 没有一个自研的 Agent 框架，等于在打上一场战争。

**V4 Flash 是 Agent 工作负载的性价比之王——每天几分钱** — 每百万 token $0.14/$0.28 的价格，[V4 Flash 的输出成本约为 Claude Opus 4.8 的 1/100](https://www.cloudzero.com/blog/deepseek-pricing/)。Agent 工作的实际日成本：约 $0.20/天 vs 约 $10/天。r/openclaw 社区的实用路由策略，据 [Dev.to](https://dev.to)，是：Flash 负责仓库扫描和工具循环，Qwen 3.7 Max 负责复杂推理，GLM 5.1 负责结构化合成。社区的座右铭："选择你能承受的失败模式。"有开发者用 V4 Flash 生成了 80 万字的网文内容，消耗 7500 万 token（85% 缓存命中），总花费仅 $3.78。在 [r/DeepSeek](https://www.reddit.com/r/DeepSeek/comments/1u2jkwg/do_foreigners_use_deepseek/)，一位中国用户发问："我是中国人，在这边用过 ChatGPT、Gemini 和 Claude，但有点贵。好奇你们外国人用过 DeepSeek 吗？我觉得 V4 性能相当令人印象深刻。"

**工具调用可靠性是阿喀琉斯之踵** — 已经被文档记录的"呼叫风暴"模式：[V4 重复调用相同工具 30+ 次陷入死循环](https://baixiaoustc.github.io/2026/06/08/claude-code-repetition-loop-deepseek-bug/)，Reasonix 框架团队确认为已知失败模式。工程师 Vladimir 在消耗 1434 万 token 后报告 V4"频繁忽略 Agent 文件"。一个 [OpenClaw GitHub issue](https://github.com/openclaw/openclaw/issues/73185) 记录了空提示词静默计费漏洞：发送空提示词给 V4 Flash 会产生约 3.5KB 响应并静默扣费，用户看不到任何输出。有 X 用户报告相同任务 V4 Pro 耗时 2 小时 vs Codex 5.5 Medium 仅需 20 分钟。这些不是基准测试的失分——而是让团队在生产环境中继续使用 Claude/GPT 的可靠性差距。

**本地自部署正在快速吸收 V4，但还很粗糙** — llama.cpp 已[提供 V4 新 KV 缓存架构的 WIP 支持](https://github.com/ggml-org/llama.cpp/pull/24162)："通过长上下文/工具调用测试，但速度很慢。"V4 Flash 在 Q4 量化下可装入单张 RTX 4090（24GB 显存）。antirez/ds4 项目在 Apple Silicon 上实现了 +62% 的预填充加速。另一边，vLLM 在 8× H20-3e 上部署 V4-Pro 正遇到兼容性报错。

**国产芯片故事是真正的战略差异化壁垒** — V4 发布的同时[Nvidia GPU 和华为昇腾 950 被放在同一验证框架内](https://govt.chinadaily.com.cn/s/202604/27/WS69eeeea7498e23165e06f109/deepseek-unveils-ai-model-for-domestic-chips-in-symbolic-break-from-nvidia-reliance.html)——这是对 CUDA 依赖的一次标志性脱钩。这使 DeepSeek 成为首个能在全栈国产硬件上部署的万亿参数模型。Jensen Huang 此前曾表示，如果 DeepSeek 的新模型在国产芯片上表现最佳，可能推动中国技术成为全球标准。

## 研究揭示的关键模式

1. AI 市场从"哪个模型最强"转向了"哪个 Agent 框架 + 模型最强"——DeepSeek 只有一半筹码，据 [36Kr](https://36kr.com) 和 [SemiAnalysis](https://semianalysis.com)
2. 极致的成本优势（比 Opus 便宜 28-100 倍）创造了过去经济上不可能的新用例——24/7 Agent 循环在美系模型上每天数百美元，现在只需零钱
3. 梁文锋的"要钱不要权"融资结构是对 VC 驱动 AI 发展模式的刻意拒绝——五年锁定期和"不挖角"条款释放出长期主义的信号，据 [SCMP](https://scmp.com) 和 [CNBC](https://cnbc.com)
4. 工具调用可靠性和幻觉问题仍是生产环境部署的真正障碍，即使价格差距巨大，团队仍将关键任务留在 Claude/GPT 上
5. 开源生态在快速吸收 V4（llama.cpp、vLLM、ds4），但生产部署还很毛糙——代码能跑，运维还没跟上

---

✅ 所有 Agent 已回报！
├─ 🟠 Reddit: 3 条帖子
├─ 🐙 GitHub: 6 条结果 │ 294 reactions │ 223 条评论
├─ 🗣️ 核心发声者: r/DeepSeek
├─ 🌐 Web: 36Kr, Morphllm, SemiAnalysis, CloudZero, BlockBeats, SCMP, CNBC, Dev.to, Baixiaoustc, ThePaper, FutureAGI
└─ 📎 原始结果已保存至 ~/Documents/Last30Days/deepseek-raw-v3.md

## 数据覆盖范围

| 来源 | 状态 | 数据量 |
|------|------|--------|
| Reddit | ✅ | 3 条帖子 |
| GitHub | ✅ | 6 条结果 (294 reactions, 223 评论) |
| Hacker News | ❌ | 无数据 |
| Polymarket | ❌ | 无数据 |
| X / Twitter | ❌ | 未配置 |
| YouTube | ❌ | 未配置 |
| Web (补充搜索) | ✅ | 13 个来源 |
