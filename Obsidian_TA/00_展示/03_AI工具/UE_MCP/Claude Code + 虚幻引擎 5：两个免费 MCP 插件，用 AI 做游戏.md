---
title: "Claude Code + 虚幻引擎 5：两个免费 MCP 插件，用 AI 做游戏"
source: "https://www.top3d.ai/zh/learn/claude-code-unreal-engine"
author:
  - "[[Stefan Vaskevich]]"
published: 2026-06-09
created: 2026-06-16
description: "用两个免费 MCP 插件（UnrealClaude 和 VibeUE）把 Claude Code 接入虚幻引擎 5，搭出一个可玩的无尽跑酷游戏。完整安装步骤与坦诚评测。"
tags:
  - "clippings"
---
[AI接管虚幻引擎5：Claude Code全流程游戏开发实战_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1CEEv6QEy2/?spm_id_from=333.1387.favlist.content.click&vd_source=089349bc15fe4a0508fc235b6d5563a8)

[Claude Code Took Over Unreal Engine 5 and Built a Game](https://www.youtube.com/watch?v=iRcrZjOt5H8)

**Claude Code 真的能驱动虚幻引擎 5** 吗 - 移动物体、编辑蓝图、运行游戏、再看看结果？能。在花了一个月测试各种连接器和插件之后（一堆垃圾，其中有些还很贵），真正管用的方案是 **两个免费、开源的插件配合使用** ：用 **UnrealClaude** 截取视口画面、移动 actor，用 **VibeUE** 编辑蓝图、跑 Python。唯一要花钱的，就是 Claude 本身。

这是一份完整的实操：每个插件做什么，怎么安装和连接，以及一次诚实的压力测试 - 我把自己用 AI 生成的 3D 资产丢进一个项目，让 Claude 从一个第三人称角色出发，搭出一个 **能玩的无尽跑酷游戏** ，然后看它能做到什么程度。简短结论： *只要* 你能把想要的逻辑讲清楚，它就是一个实打实的加速器；含糊的提示只会换来含糊的结果。

一句话讲清这套搭建

**虚幻引擎 5.7** + 在你 UE 项目文件夹里打开的 **Claude Code** ，外加两个免费插件： [UnrealClaude](https://github.com/Natfii/UnrealClaude) （通过 MCP 截图 + 操控 actor）和 [VibeUE](https://www.vibeue.com/) （通过 MCP 操作蓝图 + Python，需要一个免费 API key）。两者都会暴露一个 MCP 服务器，剩下的交给 Claude。

## 观看完整制作过程

整套搭建和压力测试，从头到尾，都在 YouTube 上。

![左侧的 Claude Code 正在检查两个 MCP 连接，右侧的虚幻引擎 5 编辑器里是项目场景](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fhero-claude-unreal-setup.jpg&w=3840&q=75)

整套搭建在一块屏幕上：Claude Code 通过两个 MCP 插件 - UnrealClaude 和 VibeUE - 与虚幻引擎 5 对话，两个连接都已确认。

## 1\. 把 Claude Code 连到虚幻引擎的两个免费插件

我试过的几乎每一个「给虚幻用的 AI」插件，要么根本不能用，要么最关键的那部分要收费。这两个是免费、开源的，而且各自覆盖了工作的不同一半 - 这正是你要把它们一起用的原因。

### UnrealClaude - 视口里的眼睛和手

[UnrealClaude](https://github.com/Natfii/UnrealClaude) 是一个广受好评的插件，它做的恰好是你最需要的两件事：它能 **捕获视口** （这样 Claude 就能 *看到* 自己刚刚搭出来的东西），也能 **在场景里移动物体** 。它附带一个带 20 多个编辑器工具的 MCP 服务器，面向 **虚幻引擎 5.7** ，采用 MIT 许可。那个「截一张图，然后自己审查」的循环，是整套搭建里最有用的一件事。

![UnrealClaude 的 GitHub 页面，显示虚幻引擎 5.7、一个带 20 多个工具的 MCP 服务器以及 MIT 许可](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Funrealclaude-plugin-github.jpg&w=3840&q=75)

UnrealClaude：UE 5.7，一个带 20 多个工具的编辑器内 MCP 服务器，免费且 MIT 许可。它的视口捕获工具正是让 Claude 能自我审查的关键。

### VibeUE - 蓝图和 Python

[VibeUE](https://www.vibeue.com/) 同样是开源的，但它配套有自己的控制台，所以需要一个 **免费 API key** 。除非你想用它自带的编辑器内 agent，否则不必付费 - 我们只想要它的 **MCP 工具** ，而这些工具非常齐全：编辑蓝图、在编辑器里跑 Python 脚本、处理资产和材质，等等。这一半才是真正改变你项目的部分。

![登录后的 VibeUE 控制台，显示可复制到编辑器里的免费 API key](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fvibeue-api-key.jpg&w=3840&q=75)

VibeUE 需要一个免费的账号 key（在 vibeue.com 浏览器登录）。跳过付费 agent - 你只需要 MCP 工具和 Python 访问。

## 2\. 安装并连接 MCP 插件

前置条件：安装并打开 **虚幻引擎 5.7** 和 [Claude Code](https://www.claude.com/claude-code) ， 并 *在你虚幻项目的文件夹里* 打开 Claude Code。从这里开始，安装基本上靠对话就能完成 - 你把两个插件链接粘进去，告诉 Claude 去搞定。

1

### 丢上链接，安装两个插件

把两个仓库链接给 Claude，说 *安装这两个插件* 。安装过程会拉一些依赖（Node.js、几个微软 C++ 库），所以如果缺什么，直接让 Claude 装上就行。你还会想在项目根目录放一个好用的 `CLAUDE.md` - 这是 Claude Code 每次运行都会读取的指令文件。我手写了一份，你可以在下面拿到；一份已知可用的配置文件能在这里帮你省下最多的 token 和试错。

2

### 拿到免费的 VibeUE API key

安装结束后，Claude 会提示它需要 VibeUE 的 key。在 **vibeue.com** 登录，从控制台复制 key，然后把它粘进虚幻编辑器里 VibeUE 设置（齿轮图标）并保存。

3

### 安装 MCP 并重启编辑器

Claude 第一遍可能不会注册上 MCP 服务器 - 直接让它 *安装所有 MCP* 就好。然后重启虚幻项目，让刚装好的插件加载，并（有时）重启 Claude Code，让 MCP 服务器生效。

4

### 检查两个连接

让 Claude 确认两个 MCP 服务器都在线。UnrealClaude 仅凭你的 Claude 鉴权就能独立工作；VibeUE 只有在 key 保存后才会响应。当两者都有回应时，你就准备好了。

```
# 快速确认两条桥都通了的办法：
curl http://localhost:3000/mcp/status   # UnrealClaude
curl http://127.0.0.1:8088/mcp          # VibeUE  (405/200 = alive)

# 在 Claude Code 里，最简单的检查就是：
#   "check both mcp connections"
```

下载我的 CLAUDE.md（帮你省 token 的配置）

把这个文件放到你的 Unreal 项目根目录并命名为 `CLAUDE.md` ，Claude Code 就会照着一套验证过的流程走 - `.mcp.json` 连接配置、VibeUE 技能库，以及我亲自踩过的约 20 个 UE 5.7 的坑（Play 时蓝图被锁无法编辑、FBX 导入崩溃的修复、按钮 OnClicked 静默失效等），让你少走弯路。

[下载 CLAUDE.md](https://www.top3d.ai/learn/claude-code-unreal-engine/CLAUDE.md)

让你的 CLAUDE.md 自己成长

每当 Claude Code 碰上一个真正的问题、花时间把它弄明白、并最终落地一个修复，就让它把 **那个解决方案写进 CLAUDE.md** 。几次会话下来，这个文件就会变成一份久经实战的流程手册，你可以把它丢进任何一个新的虚幻项目 - 我那份文件里的那些坑，正是这样攒出来的。

开始任何 vibe coding 之前：先起 Git

一个虚幻项目是一大堆代码 *外加* 资产，而 AI agent 跟版本控制配合得极好。先初始化 Git（没有的话让 Claude 装上），并 **在每个里程碑都提交一次** ，这样当某次实验跑偏时你能干净地回滚。在下面，你会看到我在每个可用步骤之后都要求提交一次。

## 3\. 压力测试：用提示词搭出一个无尽跑酷

我不从空白场景开始 - 我用一个第三人称模板，把默认的人形模特换成一个 **AI 生成的模块化角色** （一只狐狸，在更早的视频里做的；如果你想做自己的，这里有一份完整的 [AI 3D 角色流水线](https://www.top3d.ai/zh/learn/ai-3d-character-pipeline-2026) ）。然后我就一次一个功能地把游戏描述出来，每做完一个就提交一次。

1

### 先清理，再生成无限路径

第一个提示：把配件全去掉，只留角色（Claude 会问一些靠谱的问题，比如「保留光照和天空吗？」- 要）。接着：清空关卡，造出无限的地块，随着移动在前方生成、在身后销毁。它搭了一个 `BP_RunnerTile` ，变量命名清晰可读，用 UnrealClaude 捕获视口确认角色正站在平面上，一次就跑通了。

![AI 生成的狐狸角色站在虚幻引擎里一条纯白灰模跑酷路径上](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Ffirst-runner-greybox.jpg&w=3840&q=75)

第一个里程碑：在灰模地块上无限滚动的路径。Claude 自己截视口的图，来确认角色摆放正确。

2

### 自动奔跑、俯视镜头、三条赛道

无尽跑酷靠自己跑，所以接下来的提示让角色自动向前移动，把镜头往下俯一点，再加上用 A 和 D 切换的 **三条赛道** 。Claude 通过 VibeUE 执行 Python 脚本来编辑现有蓝图，然后运行 Play-In-Editor 自己测试。 *逻辑* 是好的；蓝图 *布局* 则不然。

![Claude 生成的一张虚幻引擎蓝图事件图，连线缠成一团、被标注为意大利面](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fblueprint-spaghetti.jpg&w=3840&q=75)

诚实的部分：它接出了能跑的逻辑，但节点布局是一团乱麻。你可以让它整理一下 - 它多半不会照做。盯着它。

3

### 障碍物、金币，以及逐渐加快的速度

加上会撞到的障碍物，再把金币作为随机分布的收集品加进来。这一轮大约花了 **15 分钟和约 1.4 万个 Opus 4.8 token** - 不算免费，但对一个能跑的玩法机制来说很便宜。我还让它 **让奔跑速度随时间逐渐加快** ，这样你撑得越久，游戏就越难。一个诚实的小提醒：我从没要求金币避开障碍物，所以有些金币就直接生成在障碍物上面了 - 这只是一个很容易跟进的提示，也是个很好的提醒：agent 会精确地做你要它做的事，不多也不少。整个过程里，同一个循环不断重复：用 Python 编辑、运行游戏、截视口的图、读结果、修。

![Claude Code 正在运行 VibeUE 的 python 工具，并读取一张带金币和障碍物的视口截图，计数器显示 14.1k token](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fagentic-loop-tokens.jpg&w=3840&q=75)

agentic 循环实战：VibeUE 执行 Python，UnrealClaude 捕获视口，Claude 读自己截的图并诊断哪里出了问题 - 金币功能约耗 1.4 万 token。

4

### 计分、金币、游戏结束 + 重试界面

一次快速的处理加上了分数、已收集金币计数，以及一个带「重试」按钮的「游戏结束」界面。样式很粗糙 - 没关系，那只是个占位，之后能重新设计。

![无尽跑酷的游戏结束界面，显示最终得分 13、金币，以及一个绿色的重试按钮](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fgame-over-ui.jpg&w=3840&q=75)

一个能用的「游戏结束 / 重试」HUD，一次提示就搞定。先功能，后好看。

## 4\. 把灰模换成 AI 生成的 3D 资产

机制在灰模上跑通了；现在让它看起来像个游戏。我在 **ChatGPT** 里生成一张概念图，然后从中提取我需要的部件 - 障碍物、金币、桥 - 再单独制作 3D 环境。（制作可直接用于游戏的 3D 模型和环境本身就是一门手艺；我在频道上讲了免费的路子，你也可以在 [排行榜](https://www.top3d.ai/zh/leaderboard) 里看到每个生成器的排名。）

![一张 ChatGPT 生成的亚洲庙宇风无尽跑酷概念图，里面有狐狸、金币、一个带刺的滚筒障碍物和一座石桥](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fchatgpt-concept.jpg&w=3840&q=75)

一张 ChatGPT 概念图就成了美术圣经 - 障碍物、金币、桥都从中提取出来，再重建为 3D 资产。

自己准备资产，让 Claude 来接线

Claude 不是 3D 生成器 - 那张图来自 ChatGPT，不是 Claude。我找到的最佳分工是： **你来想清楚并准备好资产** ，然后把 Claude 当成那个 **负责整理和接线的 agent** 。把资产导出成一个装着 FBX 的压缩包，丢进项目，再加一张截图让它理解这一套。它会自己搞清楚正确的命名，并处理摆放逻辑。

资产进来后，要求就很直白了： *把障碍物换成障碍物网格，把金币换成金币网格* ，然后搭桥。项目里有一个从 Git 拿来的免费 **卡通着色器** 跟新网格打架，所以我让 Claude 把它关掉 - 编辑材质只是 VibeUE 的又一个用例。它不是没有 bug：左转或右转会误触发「游戏结束」，桥段之间有缝隙，障碍物穿进了桥的栏杆里。大多数问题我都靠着 **给 Claude 看一张截图** 再让它去处理就修好了。其中最有意思的一次修复是栏杆穿模：Claude 发射了一批 **line traces** 来摸清桥的真实几何，再根据这些射线打到的位置把障碍物从栏杆上挪开 - 靠的是测量，而不是猜。

![灰模跑酷路径现在摆上了 3D 带刺滚筒障碍物和爪印金币](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Fassets-greybox.jpg&w=3840&q=75)

灰模被换成了真正的 3D 障碍物和金币。接下来是环境天空盒和 PBR 材质。

最后的润色：把背景投射为一个球体／天空盒（源图留下了一道淡淡的接缝 - 可以修），并给桥加上正确的 PBR 贴图 - 这些贴图我第一次生成时弄错了。一旦贴图对了，效果就好看多了。

## 5\. 成果，以及一个诚实的结论

最后做出来的是一个真正能玩的无尽跑酷：狐狸在一个漂浮山峦的世界里自动奔跑、跑过一座石桥，在三条赛道间躲避带刺的滚筒，抓到金币时分数不断攀升。对于一个几乎完全由提示词驱动、由 Claude 完成蓝图和 Python 工作的搭建来说，这是个实打实的成果。

![做好的无尽跑酷：狐狸在漂浮山峦的地景中跑过一座石桥，得分 416](https://www.top3d.ai/_next/image?url=%2Flearn%2Fclaude-code-unreal-engine%2Ffinal-runner.jpg&w=3840&q=75)

做好的压力测试 - 同一个项目，现在配上了 AI 生成的 3D 资产、一个天空盒和 PBR。由提示词驱动，蓝图和 Python 由 Claude 完成。

它什么时候出彩，什么时候不行

- **给它详细的逻辑和架构** - 描述一个功能该如何运作、又该如何扩展 - 你就能得到惊艳的结果。
- **给它含糊、肤浅的提示** ，它就会走最快的路，而不是可扩展的那条。之后很难在上面继续搭。
- 它不会产出一张 *漂亮* 的蓝图。逻辑能跑；节点图是一团乱麻，让它清理多半会失败。盯着它。
- 把 Claude 用在 **整理和逻辑** 上，而不是生成资产或精细摆放。那些自己准备好。

这能完全替代学习虚幻引擎吗？还不至于 - 但对那些清楚自己在要什么的人来说，它是个巨大的加速器。如果你是新手，别躲着它；用得 *更聪明* 些。问它 *为什么* 这里有个节点，某个模式做了什么，对你的游戏来说正确的架构是什么。作为一个既能干活、又能陪你学习的伙伴，AI 非常出色。

留意上下文窗口（约 20 万 token）

长时间的虚幻会话会很快塞满 Claude Code 的上下文。当它快满时，如果你还在做同一个任务，就运行 `/compact` ；如果你已经转到一个新任务，就 **开一个新对话** 。新对话比压缩更干净；压缩往往会把旧的杂音一起拖过来。

## 你实际得到的东西

一座能用的免费 MCP 桥

用 UnrealClaude + VibeUE 把 Claude Code 接进 UE 5.7 - 截图、actor、蓝图，还有 Python。

一个会自我审查的 agent

它运行游戏、截视口的图、读结果，再修好自己的错误。

一个能玩的无尽跑酷

自动奔跑、三条赛道、障碍物、金币、计分 HUD，还有「游戏结束」- 全由提示词搭出来。

一份清醒的成本账

每个功能约 15 分钟、约 1.4 万个 Opus 4.8 token - 还有一份对该在哪里盯着它的真切体会。

这就是整条流水线：用两个免费插件把 Claude Code 连到虚幻引擎，准备好你的 AI 资产，然后让这个 agent 在你掌舵的同时把游戏拼起来。能喂养这类工作流的新 AI-3D 工具层出不穷 - 一旦出现，它们就会直接进入 [Arena](https://www.top3d.ai/zh/arena) ，让你在下手之前先比一比。想看更多引擎工作流，可以看看 [一天搭出一个 UE5 关卡](https://www.top3d.ai/zh/learn/build-ue5-game-level-one-day-ai) 以及 [无代码的 Aura 工作流](https://www.top3d.ai/zh/learn/aura-unreal-engine-no-code-workflow) 。