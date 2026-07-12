---
title: "ComposioHQ/awesome-claude-skills: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows"
source: "https://github.com/ComposioHQ/awesome-claude-skills"
author:
published:
created: 2026-06-26
description: "A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows - ComposioHQ/awesome-claude-skills"
tags:
  - "clippings"
---
## Awesome Claude Skills

[![Composio banner](https://private-user-images.githubusercontent.com/67639393/534448770-e91255af-e4ba-4d71-b1a8-bd081e8a234a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI0MDM5NDQsIm5iZiI6MTc4MjQwMzY0NCwicGF0aCI6Ii82NzYzOTM5My81MzQ0NDg3NzAtZTkxMjU1YWYtZTRiYS00ZDcxLWIxYTgtYmQwODFlOGEyMzRhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI1VDE2MDcyNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTk3MGRmOWY1ZGE1ZTAwZDBiZTU5Njc2NGM0YzljNmIyM2IxZWMxMjc1OTA1NTc3YTRlNzZhZmJiMmI0YWIzZGYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.VX_40rzGWgJQhfX9WPyq5KCeJap18ZJMuDcvTDqy6_c)](https://dashboard.composio.dev/login?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills)

A comprehensive and curated list of 1000+ production ready and practical Claude Skills and Plugins for enhancing productivity across usecases on not just Claude.ai, Claude Code, but also across coding agents like Codex, Cursor, Gemini CLI, Antigravity and more.

> **Want skills that do more than generate text?** Claude can send emails, create issues, post to Slack, and take actions across 1000+ apps. [See how →](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/connect)

---

## Quickstart: Connect Claude to 500+ Apps

The **connect-apps** plugin lets Claude perform real actions - send emails, create issues, post to Slack. It handles auth and connects to 500+ apps using Composio under the hood.

### 1\. Install the Plugin

```
claude --plugin-dir ./connect-apps-plugin
```

### 2\. Run Setup

```
/connect-apps:setup
```

Paste your API key when asked. (Get a free key at [dashboard.composio.dev](https://dashboard.composio.dev/login?utm_source=Github&utm_content=AwesomeSkills))

### 3\. Restart & Try It

```
exit
claude
```

> **Want skills that do more than generate text?** Claude can send emails, create issues, post to Slack, and take actions across 1000+ apps. [See how →](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/connect)

If you receive the email, Claude is now connected to 500+ apps.

**[See all supported apps →](https://composio.dev/toolkits)**

---

## Contents

## What Are Claude Skills?

Claude Skills are reusable instruction packages that teach an AI agent how to handle a specific class of tasks. Each skill is a folder containing a `SKILL.md` file with YAML frontmatter (name, description) and Markdown instructions, optionally bundled with scripts, references, and assets. Anthropic introduced the format in October 2025 and released it as an [open standard](https://github.com/anthropics/skills) in December 2025; it's now supported by Claude Code, Claude.ai, the Claude API, OpenAI Codex, Cursor, Gemini CLI, Antigravity, and Windsurf.

Skills load progressively. At session start, the agent sees only each skill's name and description — roughly 100 tokens per skill. The full SKILL.md body (typically under 5,000 tokens) loads only when the agent decides the skill is relevant to the current task. Auxiliary files in `scripts/` and `references/` load on demand. This is what lets a single agent host hundreds of skills without bloating its context window.

Skills are not MCP servers and not tools. MCP defines how an agent connects to external systems — auth, transport, tool discovery. Tools are the individual functions an agent invokes. Skills define the workflow — what to do, in what order, with what guardrails — once the agent has the connections and tools it needs. In production, all three layers run together: MCP for access, tools for actions, skills for behavior.

## Skills

### Document Processing

- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.
- [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) - Extract text, tables, metadata, merge & annotate PDFs.
- [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) - Read, generate, and adjust slides, layouts, templates.
- [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) - Spreadsheet manipulation: formulas, charts, data transformations.
- [Markdown to EPUB Converter](https://github.com/smerchek/claude-epub-skill) - Converts markdown documents and chat summaries into professional EPUB ebook files. *By [@smerchek](https://github.com/smerchek)*
- [Master Claude for Legal](https://github.com/sboghossian/master-claude-for-legal) - Skill pack for legal teams. NDA triage, multi-party version diff, citation verifier, meeting brief, and the Friday-newsletter status synthesis pattern. Includes 10 reference docs (privilege, verification, long documents, practice areas) and 3 firm templates. Built from the public Anthropic Claude for Legal Teams webinar dataset. *By [@sboghossian](https://github.com/sboghossian)*

### Development & Code Tools

- [artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) - Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
- [aws-skills](https://github.com/zxkane/aws-skills) - AWS development with CDK best practices, cost optimization MCP servers, and serverless/event-driven architecture patterns.
- [building-blog](https://github.com/BuildShipGrowRepeat/nextjs-sanity-blog-skill) - Adds an SEO-first, i18n-ready blog to a Next.js + Sanity site via a 40-question intake, a one-page plan, and a 20-section spec. Includes a generator for AI hero images via Gemini 3 Pro Image (Nano Banana Pro). *By [@BuildShipGrowRepeat](https://github.com/BuildShipGrowRepeat)*
- [Changelog Generator](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/changelog-generator) - Automatically creates user-facing changelogs from git commits by analyzing history and transforming technical commits into customer-friendly release notes.
- [Chrome Relay](https://chrome-relay.kushalsm.com/) - Drives the user's already-open Chrome session — cookies, SSO, extensions, localhost — through a local CLI bridge. Real-Chrome counterpart to Playwright Browser Automation; install via `npx skills add chrome-relay` + a [Chrome Web Store extension](https://chromewebstore.google.com/detail/chrome-relay/cpdiapbifblhlcpnmlmfpgfjlacebokb). No remote relay, no Playwright fixtures, no MCP server needed.
- [Claude Code Terminal Title](https://github.com/bluzername/claude-code-terminal-title) - Gives each Claud-Code terminal window a dynamic title that describes the work being done so you don't lose track of what window is doing what.
- [Connect](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/connect) - Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services.
- [D3.js Visualization](https://github.com/chrisvoncsefalvay/claude-d3js-skill) - Teaches Claude to produce D3 charts and interactive data visualizations. *By [@chrisvoncsefalvay](https://github.com/chrisvoncsefalvay)*
- [FFUF Web Fuzzing](https://github.com/jthack/ffuf_claude_skill) - Integrates the ffuf web fuzzer so Claude can run fuzzing tasks and analyze results for vulnerabilities. *By [@jthack](https://github.com/jthack)*
- [finishing-a-development-branch](https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch) - Guides completion of development work by presenting clear options and handling chosen workflow.
- [Full-Page Screenshot](https://github.com/LewisLiu007/full-page-screenshot) - Captures full-page screenshots of web pages via Chrome DevTools Protocol with zero dependencies. *By [@LewisLiu007](https://github.com/LewisLiu007)*
- [great\_cto](https://github.com/avelikiy/great_cto) - Claude Code plugin: 7 specialised subagents (tech-lead, senior-dev, qa-engineer, security-officer, devops, l3-support, project-auditor) orchestrating a full SDLC pipeline — architecture, TDD, 12-angle code review, QA, security audit, deploy. 11 project archetypes auto-detected, 13 compliance frameworks (GDPR/PCI-DSS/HIPAA/SOC2/ISO 27001), self-improving knowledge layer that learns from every incident. *By [@avelikiy](https://github.com/avelikiy)*
- [iOS Simulator](https://github.com/conorluddy/ios-simulator-skill) - Enables Claude to interact with iOS Simulator for testing and debugging iOS applications. *By [@conorluddy](https://github.com/conorluddy)*
- [jules](https://github.com/sanjay3290/ai-skills/tree/main/skills/jules) - Delegate coding tasks to Google Jules AI agent for async bug fixes, documentation, tests, and feature implementation on GitHub repos. *By [@sanjay3290](https://github.com/sanjay3290)*
- [LangSmith Fetch](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/langsmith-fetch) - Debug LangChain and LangGraph agents by automatically fetching and analyzing execution traces from LangSmith Studio. First AI observability skill for Claude Code. *By [@OthmanAdi](https://github.com/OthmanAdi)*
- [lean-ctx](https://github.com/yvgude/lean-ctx) - MCP server and context runtime for AI coding agents: session caching, AST-aware compression, and 90+ shell patterns to reduce token usage. Supports Claude Code, Cursor, Copilot, and other integrations. Install the Claude Code skill with `lean-ctx init --agent claude-code`; docs at [leanctx.com](https://leanctx.com/). *By [@yvgude](https://github.com/yvgude)*
- [MCP Builder](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/mcp-builder) - Guides creation of high-quality MCP (Model Context Protocol) servers for integrating external APIs and services with LLMs using Python or TypeScript.
- [move-code-quality-skill](https://github.com/1NickPappas/move-code-quality-skill) - Analyzes Move language packages against the official Move Book Code Quality Checklist for Move 2024 Edition compliance and best practices.
- [OpenWeb](https://github.com/openweb-org/openweb) - Agent-native way to access any website. Calls the same APIs the website calls (JSON in, JSON out) with auth (cookies, JWT, CSRF, signing) auto-resolved per request. 90+ sites built in. *By [@openweb-org](https://github.com/openweb-org)*
- [overkill](https://github.com/santiago-vargas-de-kruijf/claude-overkill) - Surfaces advanced, maximalist alternatives to whatever solution is being discussed — advanced data structures, distributed-systems algorithms, niche frameworks, design patterns, and frontier tooling — each ranked on a calibrated complexity scale with learning links and the scenario in which the path pays off. *By [@santiago-vargas-de-kruijf](https://github.com/santiago-vargas-de-kruijf)*
- [Playwright Browser Automation](https://github.com/lackeyjb/playwright-skill) - Model-invoked Playwright automation for testing and validating web applications. *By [@lackeyjb](https://github.com/lackeyjb)*
- [prompt-engineering](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering) - Teaches well-known prompt engineering techniques and patterns, including Anthropic best practices and agent persuasion principles.
- [pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) - Design comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing) for requirements or code, generating optimized test suites with pairwise coverage.
- [reddit-fetch](https://github.com/ykdojo/claude-code-tips/tree/main/skills/reddit-fetch) - Fetches Reddit content via Gemini CLI when WebFetch is blocked or returns 403 errors.
- [Septim Agents Pack](https://septimlabs.com/tools/agents?utm_source=awesome-claude-skills&utm_medium=awesome-list&utm_campaign=oss-backlink) - 10 named Claude Code sub-agents (Atlas, Luca, Canon, Ember, Tally, Nova, Ward, Mira, Juno, Pip) covering planning, architecture, brand, marketing, finance, design, legal, customer, research, and coordination. Drop into `.claude/agents/`. *By [@septimlabs-code](https://github.com/septimlabs-code)*
- [Skill Creator](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/skill-creator) - Provides guidance for creating effective Claude Skills that extend capabilities with specialized knowledge, workflows, and tool integrations.
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) - Automatically converts any documentation website into a Claude AI skill in minutes. *By [@yusufkaraaslan](https://github.com/yusufkaraaslan)*
- [software-architecture](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture) - Implements design patterns including Clean Architecture, SOLID principles, and comprehensive software design best practices.
- [subagent-driven-development](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development) - Dispatches independent subagents for individual tasks with code review checkpoints between iterations for rapid, controlled development.
- [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - Use when implementing any feature or bugfix, before writing implementation code.
- [using-git-worktrees](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/) - Creates isolated git worktrees with smart directory selection and safety verification.
- [Webapp Testing](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/webapp-testing) - Tests local web applications using Playwright for verifying frontend functionality, debugging UI behavior, and capturing screenshots.

### Data & Analysis

- [CSV Data Summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) - Automatically analyzes CSV files and generates comprehensive insights with visualizations without requiring user prompts. *By [@coffeefuelbump](https://github.com/coffeefuelbump)*
- [deep-research](https://github.com/sanjay3290/ai-skills/tree/main/skills/deep-research) - Execute autonomous multi-step research using Gemini Deep Research Agent for market analysis, competitive landscaping, and literature reviews. *By [@sanjay3290](https://github.com/sanjay3290)*
- [postgres](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres) - Execute safe read-only SQL queries against PostgreSQL databases with multi-connection support and defense-in-depth security. *By [@sanjay3290](https://github.com/sanjay3290)*
- [recursive-research](https://github.com/Anjos2/recursive-research) - Recursive research up to PhD level across any domain (science, tech, business, arts, humanities) with source tiering, WDM + Munger inversion for autonomous decisions, and disk checkpointing to survive context compaction. *By [@Anjos2](https://github.com/Anjos2)*
- [root-cause-tracing](https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing) - Use when errors occur deep in execution and you need to trace back to find the original trigger.

### Business & Marketing

- [Brand Build Skills](https://github.com/rampstackco/claude-skills) - 59-skill library covering the full website lifecycle: brand, design, content, SEO, dev, ops, growth, and research. Stack-agnostic with an Ahrefs MCP-powered SEO audit suite. Includes a meta-skill for writing your own. *By [@rampstackco](https://github.com/rampstackco)*
- [Brand Guidelines](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/brand-guidelines) - Applies Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards.
- [Competitive Ads Extractor](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/competitive-ads-extractor) - Extracts and analyzes competitors' ads from ad libraries to understand messaging and creative approaches that resonate.
- [Domain Name Brainstormer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/domain-name-brainstormer) - Generates creative domain name ideas and checks availability across multiple TLDs including.com,.io,.dev, and.ai extensions.
- [Internal Comms](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/internal-comms) - Helps write internal communications including 3P updates, company newsletters, FAQs, status reports, and project updates using company-specific formats.
- [Lead Research Assistant](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/lead-research-assistant) - Identifies and qualifies high-quality leads by analyzing your product, searching for target companies, and providing actionable outreach strategies.

### Communication & Writing

- [article-extractor](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/article-extractor) - Extract full article text and metadata from web pages.
- [brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming) - Transform rough ideas into fully-formed designs through structured questioning and alternative exploration.
- [Content Research Writer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer) - Assists in writing high-quality content by conducting research, adding citations, improving hooks, and providing section-by-section feedback.
- [family-history-research](https://github.com/emaynard/claude-family-history-research-skill) - Provides assistance with planning family history and genealogy research projects.
- [Meeting Insights Analyzer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/meeting-insights-analyzer) - Analyzes meeting transcripts to uncover behavioral patterns including conflict avoidance, speaking ratios, filler words, and leadership style.
- [NotebookLM Integration](https://github.com/PleasePrompto/notebooklm-skill) - Lets Claude Code chat directly with NotebookLM for source-grounded answers based exclusively on uploaded documents. *By [@PleasePrompto](https://github.com/PleasePrompto)*
- [Twitter Algorithm Optimizer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/twitter-algorithm-optimizer) - Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit tweets to improve engagement and visibility.

### Creative & Media

- [anydesign](https://github.com/uxKero/anydesign) - Analyzes any image, URL, or Figma file and generates a structured `design.md` with the full design system, component inventory, and reconstruction notes — portable to v0, Lovable, Cursor or any AI builder. *By [@uxKero](https://github.com/uxKero)*
- [Canvas Design](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/canvas-design) - Creates beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, designs, and static pieces.
- [imagen](https://github.com/sanjay3290/ai-skills/tree/main/skills/imagen) - Generate images using Google Gemini's image generation API for UI mockups, icons, illustrations, and visual assets. *By [@sanjay3290](https://github.com/sanjay3290)*
- [Image Enhancer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/image-enhancer) - Improves image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation.
- [Slack GIF Creator](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/slack-gif-creator) - Creates animated GIFs optimized for Slack with validators for size constraints and composable animation primitives.
- [Theme Factory](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/theme-factory) - Applies professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages with 10 pre-set themes.
- [Video Downloader](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/video-downloader) - Downloads videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality options.
- [youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript) - Fetch transcripts from YouTube videos and prepare summaries.
- [swiftui-design-skill](https://github.com/wholiver/swiftui-design-skill) - SwiftUI 前端设计 skill — 反 AI Slop 六条铁律、设计方向顾问、品牌资产协议、五维评审。支持 Claude Code / Cursor / Codex / OpenCode 等全部 AI agent 平台。 *By [@wholiver](https://github.com/wholiver)*
- [Pixelbin-Media-Generation](https://github.com/anandpareek-hub/pixelbin-claude-skill) - Generate and edit images & videos with 85+ API portfolio and build visually appealing website pages

### Productivity & Organization

- [File Organizer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/file-organizer) - Intelligently organizes files and folders by understanding context, finding duplicates, and suggesting better organizational structures.
- [Invoice Organizer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/invoice-organizer) - Automatically organizes invoices and receipts for tax preparation by reading files, extracting information, and renaming consistently.
- [kaizen](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/kaizen/skills/kaizen) - Applies continuous improvement methodology with multiple analytical approaches, based on Japanese Kaizen philosophy and Lean methodology.
- [n8n-skills](https://github.com/haunchen/n8n-skills) - Enables AI assistants to directly understand and operate n8n workflows.
- [Raffle Winner Picker](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/raffle-winner-picker) - Randomly selects winners from lists, spreadsheets, or Google Sheets for giveaways and contests with cryptographically secure randomness.
- [solo-skills](https://github.com/rockscy/solo-skills) - 7 bilingual (EN+中文) skills for solo founders and indie devs: launch tweets, customer emails, decision frameworks, postmortems. Each skill includes an explicit "When NOT to use" section.
- [Tailored Resume Generator](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/tailored-resume-generator) - Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances.
- [ship-learn-next](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/ship-learn-next) - Skill to help iterate on what to build or learn next, based on feedback loops.
- [tapestry](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/tapestry) - Interlink and summarize related documents into knowledge networks.

### Collaboration & Project Management

- [git-pushing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing) - Automate git operations and repository interactions.
- [google-workspace-skills](https://github.com/sanjay3290/ai-skills/tree/main/skills) - Suite of Google Workspace integrations: Gmail, Calendar, Chat, Docs, Sheets, Slides, and Drive with cross-platform OAuth. *By [@sanjay3290](https://github.com/sanjay3290)*
- [mercury-mcp](https://www.teamoffsite.ai/proton/docs/skill) - Cheatsheet for the Mercury (Proton) MCP tools. Message agent teammates, manage threads, create tasks, and schedule automations across coordinated agent teams. *By [Mercury](https://mercury.build/)*
- [outline](https://github.com/sanjay3290/ai-skills/tree/main/skills/outline) - Search, read, create, and manage documents in Outline wiki instances (cloud or self-hosted). *By [@sanjay3290](https://github.com/sanjay3290)*
- [review-implementing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing) - Evaluate code implementation plans and align with specs.
- [test-fixing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing) - Detect failing tests and propose patches or fixes.

### Security & Systems

- [computer-forensics](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics) - Digital forensics analysis and investigation techniques.
- [file-deletion](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion) - Secure file deletion and data sanitization methods.
- [metadata-extraction](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction) - Extract and analyze file metadata for forensic purposes.
- [threat-hunting-with-sigma-rules](https://github.com/jthack/threat-hunting-with-sigma-rules-skill) - Use Sigma detection rules to hunt for threats and analyze security events.

### Assistive Technology

- [ASD-AuDHD-PAI-Skills](https://github.com/emory/ASD-AuDHD-PAI-Skills) - New collection, first skill [pda-reframing](https://github.com/emory/ASD-AuDHD-PAI-Skills/blob/main/Skills/pda-reframing/SKILL.md) can reframe requests or decisions to defeat Persistent Demand Avoidance flavors of autism spectrum disorders, or people with ADHD that struggle to Start tasks and need help aligning with a task.

### App Automation via Composio

Pre-built workflow skills for 78 SaaS apps via [Rube MCP (Composio)](https://composio.dev/). Each skill includes tool sequences, parameter guidance, known pitfalls, and quick reference tables — all using real tool slugs discovered from Composio's API.

**CRM & Sales**

- [Close Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/close-automation) - Automate Close CRM: leads, contacts, opportunities, activities, and pipelines.
- [HubSpot Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/hubspot-automation) - Automate HubSpot CRM: contacts, deals, companies, tickets, and email engagement.
- [Pipedrive Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/pipedrive-automation) - Automate Pipedrive: deals, contacts, organizations, activities, and pipelines.
- [Salesforce Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/salesforce-automation) - Automate Salesforce: objects, records, SOQL queries, and bulk operations.
- [Zoho CRM Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/zoho-crm-automation) - Automate Zoho CRM: leads, contacts, deals, accounts, and modules.

**Project Management**

- [Asana Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/asana-automation) - Automate Asana: tasks, projects, sections, assignments, and workspaces.
- [Basecamp Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/basecamp-automation) - Automate Basecamp: to-do lists, messages, people, groups, and projects.
- [ClickUp Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/clickup-automation) - Automate ClickUp: tasks, lists, spaces, goals, and time tracking.
- [Jira Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/jira-automation) - Automate Jira: issues, projects, boards, sprints, and JQL queries.
- [Linear Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/linear-automation) - Automate Linear: issues, projects, cycles, teams, and workflows.
- [Monday Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/monday-automation) - Automate Monday.com: boards, items, columns, groups, and workspaces.
- [Notion Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/notion-automation) - Automate Notion: pages, databases, blocks, comments, and search.
- [Todoist Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/todoist-automation) - Automate Todoist: tasks, projects, sections, labels, and filters.
- [Trello Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/trello-automation) - Automate Trello: boards, cards, lists, members, and checklists.
- [Wrike Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/wrike-automation) - Automate Wrike: tasks, folders, projects, comments, and workflows.

**Communication**

- [Discord Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/discord-automation) - Automate Discord: messages, channels, servers, roles, and reactions.
- [Intercom Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/intercom-automation) - Automate Intercom: conversations, contacts, companies, tickets, and articles.
- [Microsoft Teams Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/microsoft-teams-automation) - Automate Teams: messages, channels, teams, chats, and meetings.
- [Slack Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/slack-automation) - Automate Slack: messages, channels, search, reactions, threads, and scheduling.
- [Telegram Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/telegram-automation) - Automate Telegram: messages, chats, media, groups, and bots.
- [WhatsApp Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/whatsapp-automation) - Automate WhatsApp: messages, media, templates, groups, and business profiles.

**Email**

- [Gmail Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/gmail-automation) - Automate Gmail: send/reply, search, labels, drafts, and attachments.
- [Outlook Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/outlook-automation) - Automate Outlook: emails, folders, contacts, and calendar integration.
- [Postmark Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/postmark-automation) - Automate Postmark: transactional emails, templates, servers, and delivery stats.
- [SendGrid Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/sendgrid-automation) - Automate SendGrid: emails, templates, contacts, lists, and campaign stats.

**Code & DevOps**

- [Bitbucket Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/bitbucket-automation) - Automate Bitbucket: repos, PRs, branches, issues, and workspaces.
- [CircleCI Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/circleci-automation) - Automate CircleCI: pipelines, workflows, jobs, and project configuration.
- [Datadog Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/datadog-automation) - Automate Datadog: monitors, dashboards, metrics, incidents, and alerts.
- [GitHub Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/github-automation) - Automate GitHub: issues, PRs, repos, branches, actions, and code search.
- [GitLab Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/gitlab-automation) - Automate GitLab: issues, MRs, projects, pipelines, and branches.
- [PagerDuty Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/pagerduty-automation) - Automate PagerDuty: incidents, services, schedules, escalation policies, and on-call.
- [Render Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/render-automation) - Automate Render: services, deploys, and project management.
- [Sentry Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/sentry-automation) - Automate Sentry: issues, events, projects, releases, and alerts.
- [Supabase Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/supabase-automation) - Automate Supabase: SQL queries, table schemas, edge functions, and storage.
- [Vercel Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/vercel-automation) - Automate Vercel: deployments, projects, domains, environment variables, and logs.

**Storage & Files**

- [Box Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/box-automation) - Automate Box: files, folders, search, sharing, collaborations, and sign requests.
- [Dropbox Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/dropbox-automation) - Automate Dropbox: files, folders, search, sharing, and batch operations.
- [Google Drive Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/google-drive-automation) - Automate Google Drive: upload, download, search, share, and organize files.
- [OneDrive Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/one-drive-automation) - Automate OneDrive: files, folders, search, sharing, permissions, and versioning.

**Spreadsheets & Databases**

- [Airtable Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/airtable-automation) - Automate Airtable: records, tables, bases, views, and field management.
- [Coda Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/coda-automation) - Automate Coda: docs, tables, rows, formulas, and automations.
- [Google Sheets Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/googlesheets-automation) - Automate Google Sheets: read/write cells, formatting, formulas, and batch operations.

**Calendar & Scheduling**

- [Cal.com Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/cal-com-automation) - Automate Cal.com: event types, bookings, availability, and scheduling.
- [Calendly Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/calendly-automation) - Automate Calendly: events, invitees, event types, scheduling links, and availability.
- [Google Calendar Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/google-calendar-automation) - Automate Google Calendar: events, attendees, free/busy, and recurring schedules.
- [Outlook Calendar Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/outlook-calendar-automation) - Automate Outlook Calendar: events, attendees, reminders, and recurring schedules.

**Social Media**

- [Instagram Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/instagram-automation) - Automate Instagram: posts, stories, comments, media, and business insights.
- [LinkedIn Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/linkedin-automation) - Automate LinkedIn: posts, profiles, companies, images, and comments.
- [Reddit Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/reddit-automation) - Automate Reddit: posts, comments, subreddits, voting, and moderation.
- [TikTok Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/tiktok-automation) - Automate TikTok: video uploads, queries, and creator management.
- [Twitter Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/twitter-automation) - Automate Twitter/X: tweets, search, users, lists, and engagement.
- [YouTube Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/youtube-automation) - Automate YouTube: videos, channels, playlists, comments, and subscriptions.

**Marketing & Email Marketing**

- [ActiveCampaign Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/activecampaign-automation) - Automate ActiveCampaign: contacts, deals, campaigns, lists, and automations.
- [Brevo Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/brevo-automation) - Automate Brevo: contacts, email campaigns, transactional emails, and lists.
- [ConvertKit Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/convertkit-automation) - Automate ConvertKit (Kit): subscribers, tags, sequences, broadcasts, and forms.
- [Klaviyo Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/klaviyo-automation) - Automate Klaviyo: profiles, lists, segments, campaigns, and events.
- [Mailchimp Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/mailchimp-automation) - Automate Mailchimp: audiences, campaigns, templates, segments, and reports.

**Support & Helpdesk**

- [Freshdesk Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/freshdesk-automation) - Automate Freshdesk: tickets, contacts, agents, groups, and canned responses.
- [Freshservice Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/freshservice-automation) - Automate Freshservice: tickets, assets, changes, problems, and service catalog.
- [Help Scout Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/helpdesk-automation) - Automate Help Scout: conversations, customers, mailboxes, and tags.
- [Zendesk Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/zendesk-automation) - Automate Zendesk: tickets, users, organizations, search, and macros.

**E-commerce & Payments**

- [Shopify Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/shopify-automation) - Automate Shopify: products, orders, customers, inventory, and GraphQL queries.
- [Square Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/square-automation) - Automate Square: payments, customers, catalog, orders, and locations.
- [Stripe Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/stripe-automation) - Automate Stripe: charges, customers, products, subscriptions, and refunds.

**Design & Collaboration**

- [Canva Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/canva-automation) - Automate Canva: designs, templates, assets, folders, and brand kits.
- [Confluence Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/confluence-automation) - Automate Confluence: pages, spaces, search, CQL, labels, and versions.
- [DocuSign Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/docusign-automation) - Automate DocuSign: envelopes, templates, signing, and document management.
- [Figma Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/figma-automation) - Automate Figma: files, components, comments, projects, and team management.
- [Miro Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/miro-automation) - Automate Miro: boards, sticky notes, shapes, connectors, and items.
- [Webflow Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/webflow-automation) - Automate Webflow: CMS collections, items, sites, publishing, and assets.

**Analytics & Data**

- [Amplitude Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/amplitude-automation) - Automate Amplitude: events, cohorts, user properties, and analytics queries.
- [Google Analytics Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/google-analytics-automation) - Automate Google Analytics: reports, dimensions, metrics, and property management.
- [Mixpanel Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/mixpanel-automation) - Automate Mixpanel: events, funnels, cohorts, annotations, and JQL queries.
- [PostHog Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/posthog-automation) - Automate PostHog: events, persons, feature flags, insights, and annotations.
- [Segment Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/segment-automation) - Automate Segment: sources, destinations, tracking, and warehouse connections.

**HR & People**

- [BambooHR Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/bamboohr-automation) - Automate BambooHR: employees, time off, reports, and directory management.

**Automation Platforms**

- [Make Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/make-automation) - Automate Make (Integromat): scenarios, connections, and execution management.

**Zoom & Meetings**

- [Zoom Automation](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/zoom-automation) - Automate Zoom: meetings, recordings, participants, webinars, and reports.

## Getting Started

### Using Skills in Claude.ai

1. Click the skill icon (🧩) in your chat interface.
2. Add skills from the marketplace or upload custom skills.
3. Claude automatically activates relevant skills based on your task.

### Using Skills in Claude Code

1. Place the skill in `~/.config/claude-code/skills/`:
	```
	mkdir -p ~/.config/claude-code/skills/
	cp -r skill-name ~/.config/claude-code/skills/
	```
2. Verify skill metadata:
	```
	head ~/.config/claude-code/skills/skill-name/SKILL.md
	```
3. Start Claude Code:
	```
	claude
	```
4. The skill loads automatically and activates when relevant.

### Using Skills via API

Use the Claude Skills API to programmatically load and manage skills:

```
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    skills=["skill-id-here"],
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

See the [Skills API documentation](https://docs.claude.com/en/api/skills-guide) for details.

## Creating Skills

### Skill Structure

Each skill is a folder containing a `SKILL.md` file with YAML frontmatter:

```
skill-name/
├── SKILL.md          # Required: Skill instructions and metadata
├── scripts/          # Optional: Helper scripts
├── templates/        # Optional: Document templates
└── resources/        # Optional: Reference files
```

### Basic Skill Template

```
---
name: my-skill-name
description: A clear description of what this skill does and when to use it.
---

# My Skill Name

Detailed description of the skill's purpose and capabilities.

## When to Use This Skill

- Use case 1
- Use case 2
- Use case 3

## Instructions

[Detailed instructions for Claude on how to execute this skill]

## Examples

[Real-world examples showing the skill in action]
```

### Skill Best Practices

- Focus on specific, repeatable tasks
- Include clear examples and edge cases
- Write instructions for Claude, not end users
- Test across Claude.ai, Claude Code, and API
- Document prerequisites and dependencies
- Include error handling guidance

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/CONTRIBUTING.md) for details on:

- How to submit new skills
- Skill quality standards
- Pull request process
- Code of conduct

### Quick Contribution Steps

1. Ensure your skill is based on a real use case
2. Check for duplicates in existing skills
3. Follow the skill structure template
4. Test your skill across platforms
5. Submit a pull request with clear documentation

## Resources

### Official Documentation

- [Claude Skills Overview](https://www.anthropic.com/news/skills) - Official announcement and features
- [Skills User Guide](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - How to use skills in Claude
- [Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) - Skill development guide
- [Skills API Documentation](https://docs.claude.com/en/api/skills-guide) - API integration guide
- [Agent Skills Blog Post](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Engineering deep dive

### Community Resources

- [Anthropic Skills Repository](https://github.com/anthropics/skills) - Official example skills
- [Claude Community](https://community.anthropic.com/) - Discuss skills with other users
- [Skills Marketplace](https://claude.ai/marketplace) - Discover and share skills

### Inspiration & Use Cases

- [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code) - 50 ways people use Claude Code
- [Notion Skills](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) - Notion integration skills
- [Top Claude Skills](https://composio.dev/content/top-claude-skills)

## Join the Community

- [Join our Discord](https://discord.com/invite/composio) - Chat with other developers building Claude Skills
- [Follow on Twitter/X](https://x.com/composio) - Stay updated on new skills and features
- Questions? [support@composio.dev](mailto:support@composio.dev)

---

**Join 20,000+ developers building agents that ship**

## License

This repository is licensed under the Apache License 2.0.

Individual skills may have different licenses - please check each skill's folder for specific licensing information.

---

**Note**: Claude Skills work across Claude.ai, Claude Code, and the Claude API. Once you create a skill, it's portable across all platforms, making your workflows consistent everywhere you use Claude.

- [AgentsKB](https://agentskb.com/) - Upgrade your AI with researched answers. We did the research so your AI gets it right the first time.