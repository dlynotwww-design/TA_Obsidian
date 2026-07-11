---
title: last30days-skill 中文操作手册
source: https://github.com/mvanhorn/last30days-skill
created: 2026-06-20
tags:
  - AI
  - research
  - tool
---
# /last30days 中文操作手册

> **一个由 AI Agent 驱动的搜索引擎，按点赞、投票和真金白银排名——而非编辑决定。**

## 一、项目简介

`/last30days` 是一个 AI Agent 技能（Skill），能够在 **Reddit、X（Twitter）、YouTube、Hacker News、Polymarket、GitHub、TikTok、Instagram、Threads、Bluesky、Pinterest** 等十多个平台上**并行搜索过去 30 天内**任何话题的热门讨论，并由 AI 合成一份有据可查的摘要简报。

### 核心理念

Google 聚合的是编辑内容。`/last30days` 搜索的是**真实的人**。

- Reddit 的点赞、X 的转发、Polymarket 的真金白银赔率——数百万人每天都在用注意力和钱包投票。
- `/last30days` 同时搜索所有这些平台，按**真实参与度**排名，然后由 AI 裁判合成一份简报。
- 没有单个 AI 能原生访问所有这些平台——Google 搜不到 Reddit 评论，ChatGPT 搜不了 X，Gemini 有 YouTube 但没有 Reddit。而你可以带上自己的 API 密钥和浏览器会话，让一个 Agent 同时搜索它们。

### 典型使用场景

| 场景 | 示例命令 |
|------|----------|
| 会议前调研 | `/last30days Peter Steinberger` |
| 招聘信号分析 | `/last30days Listen Labs --hiring-signals` |
| 热点事件追踪 | `/last30days Kanye West` |
| 工具对比 | `/last30days OpenClaw vs Hermes vs Paperclip` |
| 出行前调研 | `/last30days Universal Epic Universe` |
| 快速学习 | `/last30days Nano Banana Pro prompting` |

---

## 二、安装指南

### 2.1 Claude Code（推荐）

```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

更新：

```bash
claude plugin update last30days@last30days-skill
```

> Claude Code 市场会自动处理更新。这是推荐方式。

### 2.2 Codex / Cursor / Copilot / Gemini CLI 等（50+ 平台）

```bash
npx skills add mvanhorn/last30days-skill -g
```

- `-g`：全局安装，跨所有项目可用
- 不加 `-g`：仅安装在当前项目的 `./.skills/` 目录

指定特定平台：

```bash
npx skills add mvanhorn/last30days-skill -g -a codex
npx skills add mvanhorn/last30days-skill -g -a cursor
npx skills add mvanhorn/last30days-skill -g -a gemini-cli
```

更新：

```bash
npx skills update last30days -g
```

### 2.3 claude.ai（网页版）

1. 从 [Releases](https://github.com/mvanhorn/last30days-skill/releases/latest) 下载 `last30days.skill`
2. 打开 claude.ai → Customize → Skills
3. 点击 `+` → Create skill → Upload a skill，上传文件
4. **注意**：需先在 Capabilities 中启用"Code execution and file creation"

### 2.4 Claude Desktop

1. 从 [Releases](https://github.com/mvanhorn/last30days-skill/releases/latest) 下载对应平台的 `.mcpb` 包：
   - macOS Apple Silicon：`last30days-pp-mcp-darwin-arm64.mcpb`
   - macOS Intel：`last30days-pp-mcp-darwin-amd64.mcpb`
   - Linux x86_64：`last30days-pp-mcp-linux-amd64.mcpb`
2. 打开 Claude Desktop → Settings → Extensions，拖入文件
3. 按提示填入 API 密钥（全部可选——不填则降级为仅网页搜索）
4. 重启 Claude Desktop

> **要求**：系统需安装 Python 3.12+

### 2.5 OpenClaw

```bash
clawhub install last30days-official
```

### 2.6 手动安装（开发者）

```bash
git clone https://github.com/mvanhorn/last30days-skill.git
ln -s "$(pwd)/last30days-skill/skills/last30days" ~/.claude/skills/last30days
```

---

## 三、零配置即可使用

**Reddit（含评论）、Hacker News、Polymarket、GitHub** 开箱即用，无需任何 API 密钥。

运行一次 `/last30days`，首次启动的设置向导会在 30 秒内引导你解锁更多数据源。

---

## 四、API 密钥配置

### 4.1 各数据源所需密钥

| 数据源 | 所需凭证 | 费用 |
|--------|----------|------|
| Reddit + HN + Polymarket + GitHub | 无需密钥 | 免费 |
| X / Twitter | 在浏览器登录 x.com，或设置 `XQUIK_API_KEY` / `XAI_API_KEY` | 浏览器 Cookie 免费 |
| YouTube | `brew install yt-dlp` | 免费 |
| Bluesky | bsky.app 的 App Password | 免费 |
| TikTok + Instagram + Threads + Pinterest + YouTube 评论 | ScrapeCreators 密钥 | 100 次免费，之后按量付费 |
| Perplexity Sonar | OpenRouter 密钥 | 按量付费 |
| Web 搜索 | Brave Search 密钥 | 每月 2000 次免费 |

### 4.2 macOS 钥匙串（可选）

在 macOS 上可将密钥存入系统钥匙串，而非 `.env` 文件：

```bash
# 交互式设置——逐一提示输入各密钥，跳过可留空
skills/last30days/scripts/setup-keychain.sh

# 手动存储单个密钥
security add-generic-password -a "$USER" -s last30days-XAI_API_KEY -w "xai-..."

# 查看已存密钥
skills/last30days/scripts/setup-keychain.sh --list

# 删除某个密钥
skills/last30days/scripts/setup-keychain.sh --delete XAI_API_KEY
```

> 优先级：`.env` 文件 > 环境变量 > 钥匙串

---

## 五、基础用法

### 5.1 基本搜索

```bash
/last30days <话题>
```

**示例：**

```bash
# 搜索人物
/last30days Peter Steinberger

# 搜索公司
/last30days OpenAI

# 搜索产品
/last30days OpenClaw

# 搜索技术
/last30days Nano Banana Pro prompting

# 搜索事件
/last30days Iran vs USA
```

### 5.2 对比模式

```bash
/last30days OpenClaw vs Hermes vs Paperclip
```

引擎会自动运行并行搜索，生成对比表格（架构、内存、安全性、最佳用途等维度）。

### 5.3 竞品自动发现

```bash
/last30days OpenAI --competitors
```

AI 会自动发现前 2 大竞品（如 Anthropic、xAI），然后并行运行三条搜索管线，合并输出三方对比。

### 5.4 GitHub 人物模式

```bash
/last30days Peter Steinberger --github-user=steipete
```

从关键词搜索切换为**按作者限定**的查询——直接展示该人物的 PR 数量、合并率、Star 数最高的仓库、本月 Release Notes。

### 5.5 招聘信号

```bash
/last30days Listen Labs --hiring-signals
```

分析目标公司的招聘岗位，解读其战略重心变化（企业安全？客户成功？基础设施？产品扩张？）。

### 5.6 输出 HTML 简报

```bash
/last30days OpenClaw --emit=html
```

或直接用自然语言：

```bash
/last30days OpenClaw, give me a shareable HTML brief
/last30days Cursor IDE for slack
/last30days Anthropic earnings export as html
```

生成的 HTML 文件保存在 `~/Documents/Last30Days/`，自带暗色模式、打印友好、无 JavaScript、可离线使用。

### 5.7 ELI5 模式

运行搜索后，说：

```
eli5 on    # 用通俗语言重写摘要
eli5 off   # 恢复标准模式
```

---

## 六、配置选项

### 6.1 存储目录

默认存储目录：`~/Documents/Last30Days/`（Windows 为 `C:\Users\<用户名>\Documents\Last30Days\`）

自定义方式：

```bash
# 环境变量（全局生效）
export LAST30DAYS_MEMORY_DIR=/你/想要/的/路径

# 命令行参数（单次生效）
/last30days <话题> --save-dir /你/想要/的/路径
```

### 6.2 指定输出文件

```bash
/last30days <话题> --output /精确/路径/文件名.md
```

### 6.3 保存后缀

```bash
/last30days <话题> --save-suffix=客户A
```

生成文件：`<话题>-raw-客户A.md`

### 6.4 趋势监控（持久化存储）

```bash
/last30days <话题> --store
```

添加 `--store` 将搜索结果持久化到 SQLite 数据库，配合以下脚本使用：

- `scripts/watchlist.py`：定时运行，发现新内容时可推送 Slack / Webhook
- `scripts/briefing.py`：生成每日 / 每周摘要

### 6.5 排除数据源

```bash
EXCLUDE_SOURCES=tiktok,instagram,threads
```

任意逗号分隔的子集均可。

### 6.6 启用额外数据源

```bash
INCLUDE_SOURCES=youtube_comments,tiktok_comments,perplexity
```

---

## 七、数据源详解

| 数据源 | 获取内容 | 信号类型 |
|--------|----------|----------|
| **Reddit** | 帖子 + 热门评论（含点赞数），通过公开 JSON 免费获取 | 社区共识、真实观点 |
| **X / Twitter** | 帖子、专家串文、突发反应 | 第一时间的热评和争论 |
| **YouTube** | 完整字幕搜索，定位最有价值的 5 句引用 | 深度解析 |
| **TikTok** | 创作者内容，可有 360 万播放量的观点 | 文化信号 |
| **Instagram Reels** | 博主口语字幕 | 视觉文化信号 |
| **Hacker News** | 825 分、899 条评论的开发者共识 | 技术圈共识 |
| **Polymarket** | 不是观点，是真金白银的概率 | 市场预测 |
| **GitHub** | PR 活跃度、Star 数、Release Notes | 开发者动态 |
| **Digg** | AI 领域 Top 1000 X 账号的精选聚类（无需 X 授权） | AI 圈信号 |
| **Threads** | 后 Twitter 时代的文字层 | 创作者和品牌对话 |
| **Pinterest** | 图钉、收藏、产品评论 | 视觉发现 |
| **Bluesky** | AT Protocol 帖子 | 去中心化社交层 |
| **Perplexity** | Sonar Pro 引文搜索 | 附来源的网页搜索 |
| **Web** | 编辑报道、博客对比 | 多信号之一 |

---

## 八、v3 版本新特性

### 8.1 智能搜索（核心升级）

v3 引擎在搜索之前会**先理解话题**，自动解析出正确的 X 账号、GitHub 仓库、Subreddit、TikTok 标签、YouTube 频道。

**示例：**
- 输入 "OpenClaw" → 自动解析 `@steipete`（创始人）、`r/openclaw`、`r/ClaudeCode`、正确的 YouTube 频道
- 输入 "Paperclip" → 解析 `@dotta`
- 输入 "Dave Morin" → 解析 `@davemorin` + `@OpenClaw` + TWiST 播客

### 8.2 可分享的 HTML 简报

生成自包含、暗色模式、打印友好的 HTML，可直接丢进 Slack、邮件或 Notion。无 Markdown 泄漏，无 JavaScript，可离线使用。

### 8.3 Best Takes（最佳语录）

v3 有第二个裁判专门按**幽默、机智、病毒传播度**评分。每条简报末尾附带一个"Best Takes"板块——最精辟的一句、最火的引用、让人想分享的反应。

### 8.4 跨源聚类合并

同一事件出现在 Reddit、X、YouTube 时，v3 合并为一个聚类，而非三条独立条目。基于实体的重叠检测即使标题用词不同也能匹配。

### 8.5 单次对比

"CLI vs MCP" 过去需要 3 次串行搜索（12+ 分钟）。v3 一次运行，同时覆盖双方，同等深度仅需 3 分钟。

### 8.6 GitHub 人物模式

搜索人物时自动从关键词搜索切换为作者限定查询，展示真实的交付情况——而非"谁在 Issue 里提到了这个名字"。

### 8.7 ELI5 模式

"eli5 on"——用通俗语言重写，无术语。同样的数据，同样的来源，同样的引用，就是更清晰。

### 8.8 其他 v3 改进

- **免费 Reddit 评论**：通过公开 JSON 获取帖子 + 热门评论（含点赞数），无需 API 密钥
- **YouTube 字幕增强**：候选池扩大 3 倍，覆盖更多谈话/评测类内容
- **Polymarket 降噪**：常见词消歧义（"Apple" 不再匹配 "Will Apple release a car?"）
- **弹性 Reddit**：超时预算和运行时回退，单条慢线程不拖垮整次运行
- **Polymarket 显示概率而非金额**：概率百分比比美元金额更有意义
- **单作者上限**：每位作者最多 3 条，防止单一声音主导简报
- **实体消歧义**：引擎解析出的账号被合成阶段信任使用
- **1,012 项测试通过**

---

## 九、工作流程

1. **你输入一个话题**——人物、公司、产品、技术、"X vs Y"，任意话题
2. **Agent 解析关键实体**——找到 X 账号（含创始人）、GitHub 仓库、Subreddit、TikTok 标签、YouTube 频道。如 "Kanye West" 解析出 `r/hiphopheads`、`@kanyewest`、YouTube 的 "bully review"
3. **所有数据源并行搜索**——多查询扩展，按参与度、相关性、新鲜度评分
4. **无人能及的深度**——YouTube 反应视频的完整字幕、Reddit 热门评论含点赞数、TikTok 字幕、Polymarket 概率……不只是标题和链接
5. **同一事件合并**——Wireless Festival 在 Reddit 上宣布、在 X 上讨论、TikTok 上的票价 = 一个聚类，而非三条独立条目
6. **合成一份简报**——扎根于具体数据，逐源引用，按真实参与度排名。不是"我找到了什么"，而是"什么值得关注"
7. **你的 AI 变身专家**——运行一次后，你的 Claude 会话就知道社区知道的一切。问后续问题、让它写提示词、起草邮件、规划旅行、设计架构——全部基于此刻的真实信息

---

## 十、常见问题

### Q：哪些数据源免费？
A：Reddit（含评论）、Hacker News、Polymarket、GitHub 完全免费，零配置。YouTube 安装 `yt-dlp` 后免费。Bluesky 免费（需 App Password）。

### Q：如何获取 X/Twitter 的访问权限？
A：在任意浏览器登录 x.com 即可（Cookie 方式，免费），或使用 `XQUIK_API_KEY` / `XAI_API_KEY`。

### Q：数据保存在哪里？
A：默认 `~/Documents/Last30Days/`（Windows：`C:\Users\<用户名>\Documents\Last30Days\`）。可通过 `LAST30DAYS_MEMORY_DIR` 环境变量或 `--save-dir` 参数自定义。

### Q：如何定时运行？
A：使用 `--store` 参数持久化到 SQLite，配合 `scripts/watchlist.py` 定时运行，可选 Slack/Webhook 推送。

### Q：Claude Code 中同时安装了 marketplace 插件和 npx skills 版本怎么办？
A：`/last30days` 会显示两条。选择一种安装方式，移除另一种。推荐 marketplace 插件（自动更新）。

### Q：需要什么系统环境？
A：Python 3.12+、yt-dlp（用于 YouTube）、Node.js（内置的 Bird client 用于 X 搜索）。

### Q：支持 Windows 吗？
A：Claude Code、npx skills 安装方式完全支持。Claude Desktop 的 `.mcpb` 方式暂不支持 Windows。

---

## 十一、许可证与社区

- **许可证**：MIT
- **隐私**：无追踪、无分析，研究数据留在你的机器上
- **测试**：1,012 项测试
- **技术栈**：Python 3.12+、yt-dlp、Node.js、ScrapeCreators API
- **GitHub**：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)
- **完整配置文档**：[CONFIGURATION.md](https://github.com/mvanhorn/last30days-skill/blob/main/CONFIGURATION.md)
- **贡献者列表**：[CONTRIBUTORS.md](https://github.com/mvanhorn/last30days-skill/blob/main/CONTRIBUTORS.md)
- **更新日志**：[CHANGELOG.md](https://github.com/mvanhorn/last30days-skill/blob/main/CHANGELOG.md)

---

> **@slashlast30days** · *不是更好的搜索引擎。是十几个断裂的平台，由一个 Agent 桥接起来的全新能力。*
