#!/usr/bin/env python3
"""Ultra-compact single-page Chinese resume PDF for 跃迁引擎 PCG TA position."""

from fpdf import FPDF
import os

VAULT = "D:/TA/TA_Obsidian/Obsidian_TA"
FONT = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"

class ResumePDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.add_font("yh", "", FONT)
        self.add_font("yh", "B", FONT_BOLD)
        self.set_auto_page_break(True, 8)
        self.add_page()
        self.m = 10  # margin
        self.w = 210 - 2 * self.m
        self.x0 = self.m
        self.pri = (43, 87, 151)
        self.dk = (30, 30, 30)
        self.gr = (100, 100, 100)

    def h2(self, t):
        self.ln(2.5)
        self.set_font("yh", "B", 10)
        self.set_text_color(*self.dk)
        self.cell(self.w, 4, t, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.pri)
        self.set_line_width(0.4)
        self.line(self.x0, self.get_y()+0.3, self.x0+self.w, self.get_y()+0.3)
        self.ln(1.8)

    def h3(self, t):
        self.set_font("yh", "B", 8.5)
        self.set_text_color(*self.pri)
        self.cell(self.w, 3.8, t, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)

    def b(self, t):
        self.set_font("yh", "", 7.5)
        self.set_text_color(*self.dk)
        self.cell(4, 3.2, "")
        self.cell(3, 3.2, "•")
        self.multi_cell(self.w-7, 3.2, t, new_x="LMARGIN", new_y="NEXT")

    def pt(self, title, meta):
        """Project title + meta on same line."""
        self.set_font("yh", "B", 7.8)
        self.set_text_color(*self.dk)
        tw = self.get_string_width(title)
        self.cell(tw+1, 3.5, title)
        self.set_font("yh", "", 7)
        self.set_text_color(*self.gr)
        self.cell(self.w-tw-1, 3.5, meta, new_x="LMARGIN", new_y="NEXT")

    def jr(self, jd, m):
        """Compact JD→match row."""
        self.set_font("yh", "", 7)
        self.set_text_color(*self.dk)
        self.cell(2.5, 3, "•")
        self.set_font("yh", "B", 7)
        jw = self.get_string_width(jd)+1
        self.cell(jw, 3, jd)
        self.set_font("yh", "", 7)
        self.multi_cell(self.w-2.5-jw, 3, m, new_x="LMARGIN", new_y="NEXT")

    def sk(self, cat, skills, lv):
        self.set_font("yh", "B", 7.5)
        self.set_text_color(*self.dk)
        self.cell(24, 3.5, cat)
        self.set_font("yh", "", 7.5)
        self.cell(self.w-24-16, 3.5, skills)
        self.set_text_color(*self.pri)
        self.cell(16, 3.5, lv, align="R")
        self.set_text_color(*self.dk)
        self.ln(3.5)


pdf = ResumePDF()

# ── HEADER ──
pdf.set_font("yh", "B", 14)
pdf.set_text_color(*pdf.dk)
pdf.cell(pdf.w, 6, "资深技术美术（PCG 程序化内容生成）", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(0.5)
pdf.set_font("yh", "", 7.5)
pdf.set_text_color(*pdf.gr)
pdf.cell(pdf.w, 4, "上海 · 25-40K·14薪 · 目标：跃迁引擎", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("yh", "", 7)
pdf.set_text_color(*pdf.dk)
pdf.cell(pdf.w, 3.5, "建筑学本科（五年制）| CET-6 | Grasshopper 参数化 3 年 → Houdini + UE5 PCG", align="C", new_x="LMARGIN", new_y="NEXT")

# ── 个人概述 ──
pdf.h2("个人概述")
pdf.set_font("yh", "", 7.5)
pdf.set_text_color(*pdf.dk)
pdf.multi_cell(pdf.w, 3.2,
    "建筑学本科，从 Grasshopper 参数化城市设计迁移至游戏 PCG。专注 Houdini + UE5 大型程序化城市/场景管线，"
    "具备从 0 到 1 搭建可复用 PCG 管线的完整经验，独立完成 2km² 长安城及 600m×600m 概念城市的程序化生成，"
    "覆盖布局、建筑、道路、街景全链路。精通 Houdini Engine 与 UE5 集成，能将程序化能力高效沉淀为工程化工具与流程。",
    new_x="LMARGIN", new_y="NEXT")

# ── 核心能力 ──
pdf.h2("核心能力")
for jd, m in [
    ("Houdini VEX/Python/SOP", "VEX 逐点逐属性 + Python 管线批量 + HDA 封装 + PDG 分布式 Cook + COP 图像处理"),
    ("Houdini Engine 集成", "H→UE 三通路（Heightmap/FBX/Point Cloud）；HDA 模板库部署；批量 Cook 管线"),
    ("UE5 场景/资产/性能", "PCG Graph + 自定义节点（UPCGSettings）+ Shape Grammar + World Partition + HISM/ISM"),
    ("管线工程化", "两条 0→1 PCG 管线（弥华+万维猫）；HDA 模板库 + 数据规范 + 文档化 + 培训落地"),
    ("技术调研 & AI+PCG", "Claude Code/MCP/WFC/Houdini-Agent/fxhoudinimcp；近十年 PCG 进化追踪；200+ 资源体系化"),
]:
    pdf.jr(jd, m)

# ── 项目经验 ──
pdf.h2("项目经验")

pdf.h3("▎大型程序化城市生成（对标 UE City Sample）")
pdf.pt("2km² 长安城 (万维猫·2025·UE5+Houdini)", "")
pdf.b("Spline 主干道→棋盘式次级路网→地块划分→Shape Grammar 建筑填充→植被生态散布")
pdf.b("分块生成+World Partition 解决 2km² 内存瓶颈；Seed 变体+随机扰动消除重复感，500+ 建筑变体")
pdf.b("对比 City Sample：覆盖 Road→Block→Building→Scatter 核心链路，额外实现中式棋盘路网+古代城市肌理")
pdf.pt("600m×600m 概念城市 (万维猫·2025·UE5)", "")
pdf.b("Level Instance 街区单元（含灯光/碰撞/蓝图），PCG Graph 散布，独立编辑+独立 Cook")
pdf.pt("Grasshopper 城市生成工具 (个人·2017-2024)", "")
pdf.b("参数输入→一键生成路网/地块/建筑/绿化/停车；核心逻辑迁移至 UE PCG 城市生成")

pdf.h3("▎Houdini Engine × UE5 管线搭建")
pdf.pt("PSD→街区体块工具 (万维猫·2025·Houdini COP+SOP)", "")
pdf.b("COP 读取手绘 PSD→颜色区分建筑类型→消锯齿→一键生成街区体块，批量生成效率提升约 60%")
pdf.pt("Shape Grammar 建筑变体 (万维猫·2025·UE5)", "")
pdf.b("5 种基础模块 × Seed 变体 = 500+ 不重复建筑；语法字符串切换中式/欧式/现代风格")
pdf.pt("HDA 模板库+数据桥接 (万维猫·2025·Houdini Engine)", "")
pdf.b("三通路：Heightmap(16bit RAW→Landscape)/FBX(Interchange)/Point Cloud(CSV→PCG Graph)；Python 贴图批量处理")

pdf.h3("▎植被 & 道路 PCG · 室内 PCG · 性能优化")
pdf.pt("植被工具集 (万维猫·2025·UE5 PCG)", "")
pdf.b("分层：Poisson Disk 乔木 → 林缘灌木 → Density Noise 花草 | Layer 笔刷 Mask | HISM 万级实例化")
pdf.pt("道路工具 (万维猫·2025·UE5)", "")
pdf.b("Spline 多宽度道路 + 交叉口自动检测 + 附属设施（树/灯/消防栓）沿路散布")
pdf.pt("室内 PCG 系统 (弥华宇宙·2024-2025·UE5 蓝图)", "")
pdf.b("房间分割→家具匹配→碰撞避让；纯蓝图自定义 UPCGSettings 节点；文档化提升协作效率 30%")
pdf.pt("《盘丝洞》性能优化 (万维猫·2025·UE5)", "")
pdf.b("材质复杂度-40% Shader 指令 | HISM 合批 | Nanite 适用范围判断 | 贴图 4K→2K | DrawCall 800+→200+")

pdf.h3("▎AI + PCG 前沿探索")
pdf.set_font("yh", "", 7.5)
pdf.set_text_color(*pdf.dk)
pdf.multi_cell(pdf.w, 3.2,
    "Claude Code 辅助 VEX/Python 开发 | Houdini-Agent（40+ 工具 AI Agent）| fxhoudinimcp（168 工具 MCP 服务器）"
    " | WFC 算法验证与城市街区排布 | UE 5.8 MCP（AI 控制引擎）| 近十年 PCG 技术进化 | 200+ 资源体系化",
    new_x="LMARGIN", new_y="NEXT")

# ── 技能清单 ──
pdf.h2("技能清单")
for cat, skills, lv in [
    ("PCG 算法", "网格划分/地块分配/Shape Grammar/WFC/Poisson Disk/Density Noise/Tensor Field", "●●●●○"),
    ("Houdini", "SOP/VEX Wrangle/Python管线/HDA封装/PDG/COP/HeightField", "●●●●○"),
    ("Houdini Engine", "HDA→UE5 集成/三通路数据桥接/批量 Cook 管线", "●●●●○"),
    ("UE5", "PCG Graph/自定义节点/Shape Grammar/World Partition/HISM·ISM/Niagara", "●●●●○"),
    ("编程", "Python（管线/UE API）/VEX/蓝图/C++（阅读源码 Trace 调用链）", "●●●○○"),
    ("AI 工具链", "ComfyUI+LoRA/Claude Code/MCP 协议/Houdini-Agent", "●●●○○"),
    ("DCC+辅助", "3ds Max/ZBrush/Substance/RizomUV/Marmoset/HLSL(辅助)", "●●●○○"),
]:
    pdf.sk(cat, skills, lv)

# ── JD 覆盖（极简） ──
pdf.h2("JD 逐条覆盖")
for jd, m in [
    ("PCG 管线搭建", "2 条 0→1 管线+ HDA 模板库+ UE5 集成+数据规范+文档化"),
    ("对标 City Sample 城市", "2km² 长安城完整链路+中式棋盘路网+古代城市肌理"),
    ("Houdini Engine→UE5", "三通路桥接+ HDA 引擎部署+ Python 批量 Cook"),
    ("Houdini VEX/Python", "SOP 全栈：VEX 逐点属性+ Python 管线+ HDA+ PDG"),
    ("UE5 场景/资产/性能", "PCG Graph+自定义节点+ Shape Grammar+ World Partition+ HISM"),
    ("技术调研", "AI+PCG (Claude/MCP/WFC/Agent)+ 200+资源+论文转化"),
    ("加分：数学+调研+论文", "高数优异+线性代数→WFC/Shape Grammar；论文→方案落地"),
]:
    pdf.jr(jd, m)

# ── 教育背景 ──
pdf.h2("教育背景")
pdf.set_font("yh", "B", 8)
pdf.set_text_color(*pdf.dk)
pdf.cell(pdf.w, 3.8, "南京工程学院 | 五年制建筑学本科（含两年美术训练）| CET-6 | 高数成绩优异", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("yh", "", 7)
pdf.set_text_color(*pdf.gr)
pdf.cell(pdf.w, 3.2, "Grasshopper 参数化 3 年 | CAD 高程→地形程序（建模缩短 70%）| 辅导同学获墨尔本大学研究生录取",
    new_x="LMARGIN", new_y="NEXT")

# ── SAVE ──
out = os.path.join(VAULT, "02_个人/00_面试准备/岗位/技术美术简历.pdf")
pdf.output(out)
print(f"PDF saved: {out}")
print(f"   Pages: {pdf.pages_count}, Size: {os.path.getsize(out)/1024:.0f} KB")
