---
name: srt-to-markdown
description: Convert SRT subtitle files to formatted Markdown notes with proper punctuation, paragraph structure, and screenshot placeholders. Use when the user asks to convert subtitles, SRT files, or video captions into notes.
---

# SRT to Markdown Skill

Convert SRT subtitle files into well-structured Obsidian Markdown notes. This skill handles the full pipeline: parsing SRT timestamps, merging fragmented subtitle lines into coherent paragraphs, translating English content to Chinese (preserving proper nouns), adding Chinese punctuation, organizing content under `##` headings, inserting screenshot/slide placeholders, auto-generating relevant tags, saving the Markdown to an existing knowledge base folder under `01_知识库/`, and copying the original SRT to the `01_知识库/srt/已处理/` archive (preserving the original file).

## Workflow: Converting an SRT File to Markdown

### Step 1: Read the SRT File

Read the SRT file to understand its content. SRT format consists of:
- Sequence number
- Timestamp line (`HH:MM:SS,mmm --> HH:MM:SS,mmm`)
- One or more lines of subtitle text
- Blank line separator

### Step 2: Parse and Merge

Extract all subtitle text, stripping timestamps and sequence numbers. Merge fragmented subtitle lines into coherent paragraphs. The key challenge: SRT files break text at arbitrary points (42 chars for English, ~20 chars for Chinese per line), so you must intelligently merge adjacent lines that belong to the same sentence or paragraph.

**Merging rules:**
- If a subtitle line ends without sentence-ending punctuation and the next line starts with a lowercase letter or continues the same thought → merge
- If a subtitle line ends with `.`, `?`, `!`, `。`, `？`, `！` → likely a sentence boundary
- If there's a timestamp gap > 1.5 seconds between adjacent cues → likely a paragraph or topic boundary
- When in doubt, merge conservatively — it's easier to add breaks later than to fix over-merged text

### Step 3: Translate to Chinese (if source is not already Chinese)

**⚠️ CRITICAL: This is the most important step.** The final Markdown output MUST be in Chinese, regardless of the SRT source language. If the SRT is already in Chinese, skip this step and proceed directly to Step 4.

**Translation rules:**

1. **Translate all content to natural, fluent Chinese.** The output must read as if originally written in Chinese — not a stiff word-for-word translation.
2. **Preserve English proper nouns and technical terms in their original form.** Never translate:
   - Company/product names: YouTube, Dropbox, Google Drive, Final Cut Pro, iPhone, Android
   - Technical terms: DAG, CDN, API, HTTP, SHA-256, H.264, VP9, AV1, HEVC, ProRes, WebM, MP4
   - Protocol/format names: HTTP Range, Blob Storage, pre-signed URL
   - Codec/container names: H.264, VP9, AV1, HEVC, ProRes, WebM, MP4
   - Acronyms that are universally used in English: CDN, DAG, API, GB, MB
3. **Translation quality guidelines:**
   - Adjust sentence structure to fit Chinese natural word order (topic-comment structure)
   - Break long English sentences into shorter Chinese ones when needed
   - Use Chinese idiomatic expressions where appropriate
   - Convert imperial/English measurements to Chinese conventions if applicable
4. **Section headings must also be translated to Chinese**, keeping proper nouns in English: e.g., "基于 DAG 的并行处理", "CDN 边缘分发"
5. **Screenshot placeholders translated to Chinese**: e.g., `> [在 HH:MM:SS 处添加截图 — 描述画面内容]`

### Step 4: Add Punctuation

SRT files often omit punctuation since each line break acts as a natural pause. After translation, you must ensure proper **Chinese punctuation (full-width)** throughout:

- **Periods (。)**: At the end of declarative sentences
- **Commas (，)**: Between clauses, after introductory phrases, in lists
- **Question marks (？)**: For questions
- **Exclamation marks (！)**: For emphasis or exclamations
- **Colons (：)**: Before lists, explanations, or quoted speech
- **Semicolons (；)**: Between closely related independent clauses

**Do NOT add punctuation** to lines that are clearly slide titles, on-screen labels, or code snippets.

### Step 5: Determine Paragraph Structure

Analyze the merged text and identify natural topic boundaries:

1. **Content shifts**: When the speaker moves to a new topic
2. **Slide transitions**: When "接下来"、"下一个"、"next" or similar phrases appear
3. **Time gaps**: Large gaps between subtitle cues (e.g., scene changes)
4. **Question-answer pairs**: A question followed by an explanation
5. **Enumerations**: "第一"、"第二"、"首先"、"其次"、"first"、"second" markers

### Step 6: Create Section Headings

For each identified topic section, create a `##` heading:

```markdown
## Section Title
```

**Heading naming rules:**
- Derive the heading from the key topic of that section
- Keep headings concise (under 20 characters preferred)
- **All headings MUST be in Chinese** (the output is always Chinese)
- Preserve proper nouns and technical terms in their original English within Chinese headings
- If the section topic is unclear, use a descriptive phrase from the content

### Step 7: Insert Screenshot/Slide Placeholders

Insert screenshot placeholders at natural visual breakpoints:

- **Slide transitions**: When the speaker changes slides or topics
- **Diagrams or visuals**: When the speaker says "as shown in this diagram", "请看这张图", etc.
- **Code demonstrations**: When code is shown on screen
- **Key tables or charts**: When data is referenced visually

Use this placeholder format (Chinese):

```markdown
> [!info] 📸 截图 / 幻灯片
> [在 HH:MM:SS 处添加截图 — 描述画面内容]
```

The timestamp helps locate the exact frame in the video.

### Step 8: Write the Output Markdown

Assemble the final Markdown note following this structure. **All content MUST be in Chinese** (except preserved English proper nouns and technical terms):

```markdown
---
tags:
  - subtitles
  - [topic tags]
source: "[Video/Content Title]"
date: YYYY-MM-DD
---

[Chinese introduction paragraph — the first topic/opening remarks, NO heading]

## 中文章节标题

[Chinese content with proper full-width punctuation]

> [!info] 📸 截图 / 幻灯片
> [在 HH:MM:SS 处添加截图 — 画面描述]

[continued Chinese content]
```

**Structure rules:**
1. First paragraph is always the introduction — no `##` heading
2. Each topic section uses exactly `## Title` (h2 only, no h3/h4 nesting)
3. Natural paragraphs within sections are separated by blank lines
4. Screenshot placeholders appear at the point in the flow where they appear in the video
5. Frontmatter includes tags and source attribution

### Step 8: Generate Tags

After writing the Markdown content, analyze the document and generate a comprehensive set of tags. Tags enable notes to be discovered through Obsidian search, graph view, and Dataview queries.

**Tag generation process:**

1. **Read through the full document content** — especially section headings, key terms, and recurring concepts.
2. **Identify the following tag categories:**

| Category | Examples | Source in Document |
|----------|----------|-------------------|
| Topic/Subject | `machine-learning`, `graphics`, `python` | Main topic of the video |
| Technology/Tool | `unreal-engine`, `houdini`, `docker` | Tools or software discussed |
| Domain/Field | `game-design`, `rendering`, `ai` | Knowledge domain |
| Content Type | `tutorial`, `lecture`, `talk`, `paper` | Type of content |
| Skill Level | `beginner`, `intermediate`, `advanced` | Target audience |
| Language | `chinese`, `english`, `bilingual` | Language of content |
| Project/Context | `project-alpha`, `course-xxx` | Specific project or course |

3. **Tag naming conventions:**
   - Use lowercase, hyphen-separated English for technical tags: `machine-learning`, `unreal-engine`
   - Use Chinese for domain concepts that lack clear English equivalents
   - Keep tags concise (1-3 words)
   - Avoid overly broad tags like `tech` or `video` — prefer specific tags
   - Include the source/creator as a tag if notable: e.g., `gdc`, `siggraph`, `bilibili`

4. **Always include these base tags:**
   - `subtitles` (marks this note as subtitle-derived)
   - One content-type tag: `tutorial`, `lecture`, `talk`, `course`, `documentary`, `podcast`
   - The primary topic tag

5. **Tag count:**
   - Minimum: 3 tags
   - Typical: 5-8 tags
   - Maximum: 12 tags (too many tags dilute their usefulness)

6. **Add tags to the frontmatter** in the existing YAML section:

```yaml
---
tags:
  - subtitles
  - tutorial
  - machine-learning
  - supervised-learning
  - python
  - beginner
source: "Machine Learning Tutorial"
date: 2026-07-12
---
```

### Step 9: Auto-Save Markdown and Copy Original SRT

This step has two parts:

**Part A: Save the generated Markdown to an existing knowledge base folder**

After generating the Markdown file and tags, determine the best target folder under `01_知识库/` based on the document's tags:

**Tag-to-folder mapping logic:**

1. Look at the generated tags and identify the primary topic/domain tag (e.g., `machine-learning`, `game-design`, `python`, `rendering`)
2. Map the primary tag to an **existing** folder under `01_知识库/`:
   - Check if a folder matching the primary tag name exists (e.g., `01_知识库/machine-learning/`)
   - If no exact match, check for a semantically related existing folder (e.g., `02_计算机基础` for `system-design`/`computer-science`, `03_UE` for `unreal-engine`, `01_图形学` for `rendering`)
   - **Do NOT create new folders.** If no suitable existing folder is found, fall back to `02_计算机基础` (the general CS/knowledge folder)
3. If the document has a secondary important tag (e.g., a sub-topic or tool), consider using a subfolder if one already exists:
   - `01_知识库/<existing-folder>/<existing-subfolder>/`
4. Priority: always prefer an existing folder that semantically matches. Never create new top-level folders.

**Folder matching examples:**

| Primary Tag | Target Folder |
|-------------|---------------|
| `machine-learning` | `00_AI` (if exists) or `02_计算机基础` |
| `system-design` | `02_计算机基础` |
| `game-design` | `00_GameDesign` (if exists) or `02_计算机基础` |
| `python` | `05_Python` (if exists) or `02_计算机基础` |
| `rendering` | `01_图形学` (if exists) or `02_计算机基础` |

**Save the file:**

After determining the target folder, ensure it exists (create if needed), then write the complete Markdown:
```
01_知识库/<target-folder>/中文标题.md
```

**Part B: Copy the original SRT file to the processed folder**

After the Markdown file is successfully saved, **copy** (do NOT move) the original SRT file to the processed archive:

**Copy path:** `01_知识库/srt/已处理/`

This is the fixed archive folder for ALL processed SRT source files.

```bash
cp "<original-srt-path>" "01_知识库/srt/已处理/<original-filename>.srt"
```

If the destination already has a file with the same name, append a number suffix: `<original-filename>-2.srt`, `<original-filename>-3.srt`, etc.

**⚠️ IMPORTANT: Keep the original SRT file in place.** Use `cp` (copy), NOT `mv` (move). The original file stays at its original location.

**Ensure the folders exist** before saving/moving. If either folder does not exist, create it first.

**File naming (Markdown):**
- Use the source title or derived topic as the filename, translated to Chinese
- Format: `中文标题.md`
- Keep it readable and descriptive
- Avoid special characters: no `:`, `/`, `\`, `*`, `?`, `"`, `<`, `>`, `|`
- Example: `机器学习入门教程.md` or `YouTube 系统设计深入解析.md`

After both operations complete, confirm to the user:
- `已保存 Markdown 到 [[01_知识库/<target-folder>/中文标题.md]]`
- `已复制原始 SRT 到 01_知识库/srt/已处理/<filename>.srt（原文件已保留）`

### Step 10: Verify

Check the output against these criteria:
- [ ] Every word from the SRT is preserved in meaning (spot-check 3 random sections)
- [ ] Content is translated to natural, fluent Chinese
- [ ] English proper nouns and technical terms are preserved (not translated)
- [ ] Punctuation is full-width Chinese and reads naturally
- [ ] Section breaks align with topic transitions
- [ ] Screenshot placeholders are in Chinese and at correct positions
- [ ] First section has no heading
- [ ] All headings use `##` format and are in Chinese
- [ ] Tags include at minimum: `subtitles`, content-type, and primary topic
- [ ] Tags are lowercase-hyphenated English (unless Chinese concept)
- [ ] Total tag count is between 3-12
- [ ] Markdown file is saved to an existing knowledge base folder under `01_知识库/` based on primary tag
- [ ] No new top-level folder was created
- [ ] Original SRT file is copied to `01_知识库/srt/已处理/` (original preserved in place)
- [ ] Filename is descriptive, in Chinese, and free of special characters
- [ ] User is notified with a wikilink to the saved Markdown file and the copied SRT path

## SRT Format Reference

```
1
00:00:01,000 --> 00:00:04,000
First subtitle line here

2
00:00:04,500 --> 00:00:08,000
Second subtitle line
spanning multiple text lines

3
00:00:09,000 --> 00:00:12,500
Third line with punctuation.
```

Key facts:
- Timestamp format: `HH:MM:SS,mmm` (comma before milliseconds)
- Text can span 1-3 lines within a single cue
- Cues are separated by blank lines
- May contain `<i>italic</i>`, `<b>bold</b>`, `<u>underline</u>` HTML tags
- May contain `♪` for music, `>>` for speaker indicators

## Merging Algorithm (Detailed)

When merging subtitle lines into paragraphs, use this decision tree:

1. Read all subtitle text lines into an array, preserving their order
2. For each pair of adjacent lines (current, next):
   - **Merge if**: current ends without `.?!。？！` AND next starts without a capital letter in English content OR next continues the same Chinese sentence
   - **Break if**: current ends with `.?!。？！` AND timestamp gap > 1.0 second
   - **Break if**: timestamp gap > 2.0 seconds (scene/topic change)
3. After merging text lines, scan the merged text for natural paragraph breaks:
   - Transitional phrases: "另外"、"此外"、"接下来"、"然而"、"所以"、"then"、"next"、"however"、"therefore"
   - Enumerations: "第一"、"第二"、"首先"、"其次"、"最后"、"first"、"second"、"finally"
4. Group merged lines into paragraphs (3-6 sentences per paragraph is a good default)

## Handling Special SRT Patterns

### Speaker Indicators
```srt
>> Speaker A: Hello
>> Speaker B: Hi there
```
Convert to:
```markdown
**Speaker A:** Hello

**Speaker B:** Hi there
```

### Music/Sound Notation
```srt
♪ background music ♪
```
Convert to:
```markdown
> [!note] 🎵 [Background music]
```

### On-Screen Text / UI Labels
If the subtitle appears to be on-screen text (short, no natural speech flow, often in ALL CAPS or brackets):
```markdown
**On-screen:** [text content]
```

### Italic/Bold HTML Tags
```srt
<i>whispering</i> something important
```
Convert to Markdown:
```markdown
*whispering* something important
```

## Example Conversion

### Input SRT:
```
1
00:00:00,000 --> 00:00:03,500
Welcome to this tutorial
on machine learning

2
00:00:04,000 --> 00:00:07,500
Today we will cover three topics
first supervised learning

3
00:00:08,000 --> 00:00:12,000
second unsupervised learning
and finally reinforcement learning

4
00:00:13,000 --> 00:00:16,500
Let's start with supervised learning
it's the most common approach
```

### Output Markdown (Chinese):
```markdown
---
tags:
  - subtitles
  - tutorial
  - machine-learning
  - supervised-learning
  - unsupervised-learning
  - reinforcement-learning
  - beginner
source: "Machine Learning Tutorial"
date: 2026-07-12
---

欢迎来到机器学习教程。今天我们将涵盖三个主题：第一，监督学习；第二，无监督学习；最后，强化学习。

## 监督学习

让我们从监督学习开始。这是最常见的方法。
```

**Saved to:** `01_知识库/00_AI/机器学习教程.md`（使用已有文件夹）  
**Original SRT copied to:** `01_知识库/srt/已处理/`（原文件保留）

> After saving, confirm to the user with:  
> `已保存 Markdown 到 [[01_知识库/00_AI/机器学习教程.md]]：标签 #subtitles #tutorial #machine-learning #supervised-learning #beginner`  
> `已复制原始 SRT 到 01_知识库/srt/已处理/machine-learning-tutorial.srt（原文件已保留）`

## Notes

- **All output must be in Chinese.** Translate English SRT content to natural, fluent Chinese. Preserve English proper nouns and technical terms.
- Always preserve **every piece of information** from the original SRT — this is a transcription+translation, not a summary
- If the SRT content is unclear or seems to have errors, add an inline comment: `%% 可能的转录错误 %%`
- For very long SRT files (>500 cues), consider outputting to multiple Markdown files, split by major topic boundaries
- Chinese punctuation uses full-width characters: `，。！？：；` — never use half-width `, . ! ? : ;` in Chinese text
- English proper nouns (company names, product names, technical terms) should remain in English within Chinese text
- All output files go to an existing knowledge base folder under `01_知识库/` matched by primary tag — do NOT create new top-level folders; fall back to `02_计算机基础` if no match
- Original SRT files are always **copied** (not moved) to `01_知识库/srt/已处理/` after successful conversion — the original stays in place
