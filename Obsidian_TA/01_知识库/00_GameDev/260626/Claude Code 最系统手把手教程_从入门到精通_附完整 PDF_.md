# Claude Code 最系统手把手教程，从入门到精通（附完整 PDF）

## 2-G CLAUDE.md：它的永久记忆载体

Context 是短期记忆，Plan Mode 是当下对齐，CLAUDE.md 是长期记忆。

CLAUDE.md 是一个 Markdown 文件，Claude Code 每次进入一个目录会自动读它，把它当作"这个项目的入职手册"。

CLAUDE.md 有四个位置，优先级从低到高就近覆盖：

1. 第一，用户级：`~/.claude/CLAUDE.md`，对你所有项目生效。
2. 第二，项目级：项目根目录下 `CLAUDE.md`，对这个项目生效。
3. 第三，模块级：子目录下的 `CLAUDE.md`，对这个子目录及下层生效。
4. 第四，内联级：在对话里直接 `@CLAUDE.md` 引用一段临时说明。

就近覆盖的意思是，模块级会覆盖项目级，项目级会覆盖用户级。同一个变量在四个位置都定义了，实际生效的是离当前任务最近的那个。

懒得手动写第一版？用 `/init`。在项目根目录跑 `/init`，Claude Code 会自动扫描代码、读取 README、推断技术栈，给你生成一份 CLAUDE.md 草稿。

一份合格的 CLAUDE.md 模板，大致这几块：

```
# 项目意图
这是一个 [一句话项目定位]。
核心读者 / 用户:[谁会用]。
当前阶段:[原型 / 内测 / 上线]。

# 技术栈选择
- 语言:[Python 3.11 / Node 20 / ...]
- 框架:[FastAPI / Next.js / ...]
- 数据库:[PostgreSQL / SQLite / ...]
- 部署:[Vercel / 自建 / ...]

# 禁止改动
- 不要修改 `core/` 下的任何文件，这是稳定层。
- 不要引入新的全量依赖，需要的话先讨论。
- 不要破坏现有 API 的入参签名。

# 验收标准
- 任何改动都要跑过 `pytest` 全套。
- 关键路径要有对应的 e2e 测试。
- 接口变动需要同步更新 OpenAPI schema。

# 工作流
- 默认在 Plan Mode 工作。
- 大改动先开 plan.md，审批后再动手。
- 验证不过不要往下走。
```

类比一下：CLAUDE.md 是员工 onboarding 文档 + 项目 wiki 的合体。

新员工进项目第一天该知道的所有事，都应该在这里。

CLAUDE.md 是 Claude Code 永久记忆的载体。

---

## 2-H 命令速查

我自己最常用的 7 个命令，做成一张表：

| 命令 | 作用 |
|------|------|
| `/status` | 看当前会话配置（模型、目录、Token） |
| `/context` | 看 Context 用量 |
| `/clear` | 清空当前会话 |
| `/compact` | 压缩当前会话 |
| `/init` | 在当前目录生成 CLAUDE.md |
| `/cost` | 看当前会话消耗 |
| `Shift+Tab` | 切换 Normal / Plan / Auto 三种模式 |

这张表你截图存手机就行，前两周高频用得上。

---

## 2-I 急救三步 + 五个常见坑

Claude Code 用到一定阶段一定会卡。卡在长循环里出不来、卡在错误代码里改不对、卡在反复跑没结果。

### 急救三步，抄就行：

第一步，Ctrl+C 中断。把它正在跑的循环掐掉。

第二步，`/clear` 清空会话。把这段尝试的全部历史包袱清掉。

第三步，重新描述任务。基于刚才学到的"它会卡在哪"，把 Prompt 写得更具体。

Ctrl+C → /clear → 重新描述。三步走完，90% 的卡死能解决。

### 五个最常见的坑，提前避：

1. **Token 烧爆**：会话拖太久，Context 满了它开始忘事。解决：`/compact` 或 `/clear`。
2. **没 Plan 直接 Auto**：任务复杂的时候不用 Plan Mode，直接放它跑，出错率指数级上升。解决：80% 的任务都在 Plan Mode 跑。
3. **没写 CLAUDE.md**：每次新会话都要从头解释项目，效率掉一半。解决：进项目第一件事 `/init` 生成 CLAUDE.md。
4. **`@` 错文件**：引用了一个跟任务无关的大文件，Token 哗哗烧。解决：用 `@` 之前先想清楚这个文件是不是它真的需要看。
5. **Prompt 太散**：一个对话里塞五件事，它会越做越偏。解决：一个 Prompt 一件事，做完再开下一件。

---

## Part 3 Skills 进阶：让 AI 替你记住你的工作方法

### 3-B Skills 三件套：SKILL.md / scripts / references

一个 Skill 的标准结构是这样：

```
my-skill/
├── SKILL.md       # 触发条件 + 执行说明
├── scripts/       # 可被调用的脚本
│   └── do-something.py
└── references/    # 参考资料、模板、提示词
    └── template.md
```

SKILL.md 是入口。它的开头有一段 YAML frontmatter，告诉 Claude：这个 Skill 在什么场景下激活、它能做什么、调用方式是什么。

最简 SKILL.md 模板：

```
---
name: my-first-skill
description: 在用户要求做 XX 的时候激活，产出 YY。触发关键词:[关键词列表]。
---

# 调用说明
当用户提到 [触发条件] 时，执行以下步骤:
1. 读取 references/template.md 作为参考。
2. 调用 scripts/do-something.py 跑流程。
3. 把结果写到指定位置。
```

`scripts/` 放脚本，Python、Shell、Node 都行。Claude 会按需调用。

`references/` 放它要参考的资料：风格模板、写作范例、提示词参考。

Skills 比 Prompt 高一档的地方是：它会被 Claude 自动发现。你写了一个"公众号排版"Skill，下次你说"把这篇排版一下"，Claude 不需要你说"用那个 Skill"，它自己会扫描可用 Skills 列表、发现匹配的、激活它。

---

### 3-D Skills vs CLAUDE.md vs MCP

这三个概念是 Claude Code 最容易混的三个东西。讲清楚边界：

- **CLAUDE.md** 是菜谱。Claude 进入项目就读，所有任务都会看一眼。
- **Skills** 是预制流程。平时不动，触发条件一到自动跑。
- **MCP** 是外部工具接入。要起服务、要登录、要拿能力，跟外部系统打交道时用。

真实差异是：

1. CLAUDE.md 总是在场，每次任务都会看。
2. Skills 按触发条件激活，平时不打扰。
3. MCP 是外部能力接入，不在 Claude 内部，而是把外部世界接进来。

> CLAUDE.md 总是在场，Skills 按需激活，MCP 接外部世界。

我自己最建议你先造的 Skill，是"深度研究一个陌生领域"。

因为这件事太高频了。老板突然提到一个新赛道，客户突然讲一个新概念，朋友圈刷到一个新趋势，你第一反应不是立刻写文章，而是先搞懂它到底是什么、为什么重要、谁在做、争议在哪、普通人该怎么入门。

这个 Skill 里可以封进去一整套研究流程：

1. 先澄清研究目的：是为了工作汇报、投资判断、内容选题，还是个人学习。
2. 再固定调研维度：定义、发展脉络、核心概念、代表玩家、商业模式、关键争议、入门资料。
3. 再要求来源核验：重要判断必须给出处，数据、时间点、公司案例要能追溯。
4. 再规定落盘结构：原始资料放 `research/raw-notes.md`，来源放 `research/sources.md`，报告放 `report/field-guide.md`。
5. 最后输出一份小白能看懂的入门地图，而不是一堆搜索结果。

封完之后，下次你说"帮我深度研究一下具身智能 / 低空经济 / AI Agent 浏览器 / 某个新行业"，Claude Code 就会自动按这套流程跑：先问清楚用途，再搜资料，再核验来源，再把资料和报告落到工作区里。

这件事的意义比"省时间"大得多：它把你理解陌生领域的方法，变成了一份可以被复用、被团队继承、被不断升级的研究资产。

写一个 Skill，就是在做一次知识结晶化。

---

### 3-H Skills 的本质

至少在我能看到的范围里，Skills 这一层的真正价值，不是"功能扩展"，是：

> Skills 让个人经验变成可传承的资产。

你过去十年攒下来的某种工作直觉、某种偏好、某种判断标准，在你没遇到 Skills 之前是装在你脑子里的。

除了你自己，没人能复用。

Skills 改变的是，这些东西现在可以变成一份 Claude 能读懂的文件，然后被你自己、被你的团队、甚至被陌生人激活。

到这一步，你已经知道怎么让 Claude Code 听话、记得住、有手艺。

---

## 4-C 三概念边界：Skills、MCP、子代理

在阶段 3 我们讲过 Skills、CLAUDE.md、MCP 三组关系。到了多代理协作这一层，要再加一个概念：**子代理**。

子代理是什么？Claude 替你启动的另一个 Claude。

每个子代理有自己独立的 Context、独立的任务、独立的工作目录，可以并行多个一起跑。

你不用管它们怎么沟通，主 Claude 会做调度。

类比一下，Skills 是岗位说明书，MCP 是外部能力接口，子代理是你雇的临时帮手。

更准确的说法是：

1. **Skills 管流程**：这个任务该按什么 SOP 跑。
2. **MCP 管连接**：这个任务要联什么外部世界。
3. **子代理管分工**：这个任务该几个人一起干、谁干什么。

> Skills 管流程，MCP 管连接，子代理管分工。三个东西不是替代，是协作。

---

## 4-D /brainstorming：澄清需求

第一步，在 Plan Mode 下激活 Superpowers 的 brainstorming：

```
/brainstorming
我要做一份 2026 年 Agent 工具横评的报告。
对象:Claude Code / Cursor / Codex / Devin / ChatGPT Atlas。
最终交付物:一份带封面、横评矩阵、推荐路径的 PDF。
帮我先把这个任务的细节澄清清楚。
```

```
/dispatching-parallel-agents
基于当前目录的 plan.md，启动三个子代理并行跑:
子代理 1(researcher): 负责对 plan.md 里的 5 个工具，每个工具按 5 个维度收集公开资料，
把原始信息和来源链接写到 research/<tool-name>.md。
子代理 2(fact-checker): 等 researcher 写完一个工具，你就复核它的事实和来源，
有问题写到 issues.md，没问题加 ✓ 标记。
子代理 3(report-writer): 等 fact-checker 复核完所有工具，你把 research/ 下的所有素材，
按 plan.md 的报告结构整合到 report.md。
```

提交之后，主 Claude 会调度三个子代理依次或并行启动。你能在终端里看到它们各自的工作日志。

这一段是整篇文章的最高潮：因为这是 Claude Code 跟普通对话工具拉开数量级差距的地方。

- 普通对话工具：你一个人坐在一个对话框里，所有问题都问同一个 AI，它一件一件给你回答。
- Claude Code 多代理：三个子代理同时在你电脑上跑，researcher 那个终端在哗啦啦输出资料和链接、fact-checker 那个在挨条打勾、report-writer 那个在等前两个出活，你坐在中间像在看交易室。一屏多窗，各自在跑，你只看进度。

你坐在调度位上。

主 Claude 替你协调三个 Claude 干活：一个查资料、一个核事实、一个写报告。

你不是程序员，你是问题的导演。

---

## 4-G sources.md：留来源

researcher 每查到一条资料，强制要求把出处链接写进 sources.md。

这一步在 plan.md 里已经写死了："所有事实陈述都有可点击的来源链接"。所以 researcher 在收集资料的时候，就会一边写一边更新 sources.md。

为什么这一步关键？因为可追溯性是这种调研类报告的底线。哪天你的横评结论被人问"这个分数怎么来的"，你打开 sources.md，链接全在那里。

我做 AI 这些年看下来，所有真正能立得住的产出，都有一份完整的 sources。不留 sources 的报告，自己回头都不敢看。

---

## 4-H /minimax-pdf：生成 PDF

report.md 整合完之后，最后一步：产出 PDF。

```
/minimax-pdf
把当前目录下的 report.md 转成一份 PDF。
风格:专业横评报告，封面深色 + 大字标题。
内页:浅色背景 + 衬线正文。
所有矩阵图用网格化布局。
```

minimax-pdf 会调用 MiniMax 的设计能力，出一份带封面、有版式、可印刷的 PDF。

如果你没装 MiniMax Skills，也可以用社区里的其他 PDF 生成 Skill。

核心不是"必须用某个 Skill"，是"PDF 这一步要有交付"。

---

## 4-I 工作区文件树复盘

整个项目跑完之后，看看 IDE 左侧的工作区：

```
agent-comparison-2026/
├── CLAUDE.md
├── plan.md
├── sources.md
├── issues.md
├── research/
│   ├── claude-code.md
│   ├── cursor.md
│   ├── codex.md
│   ├── devin.md
│   └── chatgpt-atlas.md
├── report.md
└── report.pdf
```

这棵树就是这个项目的全部历史。

下次你要做"Agent 工具横评 2027"，这棵树整个复用。改 plan.md 里的对象、跑一遍同样的流水线，新报告产出。

好的工作流不只产出交付物，还产出一个能被复用的工作区。

---

## Part 5 工具不是门槛。一份给你的工作流方法论

### 5-A 五步工作流方法论

回头看 Part 4 我们刚才跑完的整个流程，它能被抽象成五步：

**澄清 → 计划 → 分工 → 落盘 → 交付。**

1. **澄清**：用 brainstorming，把模糊需求问清楚。
2. **计划**：用 writing-plans，把需求落成一份 plan.md。
3. **分工**：用 dispatching-parallel-agents，把活分给多个子代理。
4. **落盘**：每一步的输出都进文件、进 sources.md，可追溯、可复用。
5. **交付**：用合适的 Skill（minimax-pdf 或别的）产出最终交付物。

我管这个叫：**五步工作流**。

先澄清，再计划，再分工，再落盘，再交付。五步，不止用在 Claude Code 上。

你做任何复杂的协作项目（做一份调研、做一支视频、做一次发布、带一个团队跑一个 OKR）都能套这五步。
