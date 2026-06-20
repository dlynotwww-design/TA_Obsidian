import json, random

def gid():
    return ''.join(random.choice('0123456789abcdef') for _ in range(16))

nodes, edges = [], []

RC, PC, UC, PRC, CC, SC, AC = '#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7','#DDA0DD','#98D8C8'

def N(x,y,w,h,t,c):
    nid=gid(); nodes.append({'id':nid,'type':'text','x':x,'y':y,'width':w,'height':h,'text':t,'color':c}); return nid
def E(f,t,fs='bottom',ts='top'):
    eid=gid(); edges.append({'id':eid,'fromNode':f,'toNode':t,'fromSide':fs,'toSide':ts}); return eid

# ROOT
root = N(1550, 0, 500, 80, '# 影视项目UE流程化', RC)

# B1: 文件批量处理插件
b1 = N(120, 160, 280, 60, '## 文件批量处理插件', PC); E(root, b1)
b1y=260
for t in ['自动生成大纲文件夹','自动导入模型资产和贴图','自动赋予模型资产材质球信息','自动整理优化文件夹']:
    n=N(130, b1y, 260, 45, t, PC); E(b1, n); b1y+=65

# B2: 效率插件
b2 = N(510, 160, 220, 60, '## 效率插件', PC); E(root, b2)
b2n = N(520, 280, 200, 45, '控制台命令调用', PC); E(b2, b2n)

# UE 大纲 header
ue = N(850, 160, 240, 60, '## UE文件大纲', UC); E(root, ue)

# Common
common = N(800, 280, 200, 50, '### Common', UC); E(ue, common)
cy=380
for t in ['ALL (外部导入完整项目资产)','BP','Materials (Character/Props/Scenes)','Decal','VFX']:
    n=N(805, cy, 190, 45, t, UC); E(common, n); cy+=60

# Character
ch = N(1100, 280, 300, 50, '### Character (角色)', UC); E(ue, ch)
char_ex = N(1120, 380, 260, 50, 'C_ZhangShan (C_角色名称)', UC); E(ch, char_ex)
char_mesh = N(1130, 480, 240, 45, 'Mesh: C_ZhangShan_mod', UC); E(char_ex, char_mesh)
char_tex = N(1130, 540, 240, 45, 'Textures (贴图)', UC); E(char_ex, char_tex)
char_mat = N(1130, 600, 240, 45, 'Materials (材质)', UC); E(char_ex, char_mat)
char_rig = N(1130, 660, 240, 45, 'Rig (绑定)', UC); E(char_ex, char_rig)
rig_groom = N(1390, 660, 220, 45, 'Groom (毛发文件+材质)', UC); E(char_rig, rig_groom, 'right', 'left')
char_rig2 = N(1130, 720, 240, 45, 'C_ZhangShan_Rig', UC); E(char_rig, char_rig2)
char_bp = N(1130, 780, 240, 45, 'BP: C_ZhangShan_BP', UC); E(char_ex, char_bp)

# Props
prop = N(1700, 280, 300, 50, '### Props (道具)', UC); E(ue, prop)
prop_ex = N(1720, 380, 260, 50, 'P_ShiTou (P_道具名称)', UC); E(prop, prop_ex)
prop_mesh = N(1730, 480, 240, 45, 'Mesh: P_ShiTou_mod', UC); E(prop_ex, prop_mesh)
prop_tex = N(1730, 540, 240, 45, 'Textures (贴图)', UC); E(prop_ex, prop_tex)
prop_mat = N(1730, 600, 240, 45, 'Materials (材质)', UC); E(prop_ex, prop_mat)
prop_rig1 = N(1730, 660, 240, 45, 'Rig: P_ShiTou_Rig', UC); E(prop_ex, prop_rig1)
prop_bp = N(1730, 720, 240, 45, 'BP: P_ShiTou_BP', UC); E(prop_ex, prop_bp)

# Scenes
scenes = N(2080, 280, 300, 50, '### Scenes (场景)', UC); E(ue, scenes)
scene_ex = N(2100, 380, 260, 50, 'DDDD_ChuZhuWu (项目_场景)', UC); E(scenes, scene_ex)
scene_maps = N(2100, 480, 260, 50, 'Maps', UC); E(scene_ex, scene_maps)
scene_map1 = N(2100, 560, 260, 45, 'DDDD_ChuZhuWu_Map (总关卡)', UC); E(scene_maps, scene_map1)
scene_level = N(2100, 630, 260, 45, 'Level (子关卡)', UC); E(scene_maps, scene_level)
scene_env = N(2100, 710, 260, 45, 'Env (地编子关卡)', UC); E(scene_level, scene_env)
scene_light = N(2100, 780, 260, 45, 'Light (灯光子关卡)', UC); E(scene_level, scene_light)
vfx_assets = N(2080, 880, 200, 45, 'VFXAssets', UC); E(scenes, vfx_assets)

# Shot
shot = N(2400, 280, 280, 50, '### Shot (镜头)', UC); E(ue, shot)
shot_ep = N(2410, 380, 260, 45, 'EP01 (集数)', UC); E(shot, shot_ep)
shot_sc = N(2410, 450, 260, 45, 'SC001 (场次)', UC); E(shot_ep, shot_sc)
shot_cam = N(2410, 520, 280, 50, 'ep01_sc01_c001 (镜头号)', UC); E(shot_sc, shot_cam)
sy=590
for t in ['总序列','Ani','VFX','CFX']:
    n=N(2420, sy, 260, 40, t, UC); E(shot_cam, n); sy+=50

# ShotAssets
shot_assets = N(2400, 850, 280, 50, '### ShotAssets', UC); E(shot, shot_assets)
sa_ep = N(2410, 940, 260, 45, 'EP01 (集数)', UC); E(shot_assets, sa_ep)
sa_sc = N(2410, 1010, 260, 45, 'SC001 (场次)', UC); E(sa_ep, sa_sc)
sa_cam = N(2410, 1080, 280, 50, 'ep01_sc01_c001 (镜头号)', UC); E(sa_sc, sa_cam)
say=1150
for t in ['Ani (动画文件)','Cfx (解算)','Vfx (特效)']:
    n=N(2420, say, 260, 40, t, UC); E(sa_cam, n); say+=50

# ==== BOTTOM ROW: 规范/流程 ====
row_y = 920

# 道具规范
prop_norm = N(120, row_y, 280, 60, '## 道具规范', PRC); E(root, prop_norm)
py=1020
for t in ['贴图: 命名规范/位数/尺寸 规则化自动导入','材质: 命名规范/材质球属性区分 自动生成','模型: Maya自动导出 UE自动导入 规则命名','优化: 面数合理性布局 保证质量优化布线','质量: UE精度问题处理']:
    n=N(110, py, 300, 50, t, PRC); E(prop_norm, n); py+=65

# 角色规范
char_norm = N(520, row_y, 280, 60, '## 角色规范', CC); E(root, char_norm)
cy2=1020
for t in ['贴图: 命名规范/位数/尺寸 自动导入','材质: 命名规范/材质球属性 自动生成','模型: Maya自动导出 UE自动导入','骨骼: 骨骼信息/蒙皮修型 插件导入 自动化','解算: 解算导入/合并骨骼 批量化镜头','毛发: 材质球效果测试 动态 导入缓存']:
    n=N(510, cy2, 300, 50, t, CC); E(char_norm, n); cy2+=65

# 场景规范
scene_norm = N(920, row_y, 280, 60, '## 场景规范', SC); E(root, scene_norm)
sy2=1020
for t in ['快速搭建: PCG技术 场景制作插件 资产充足','资产库: 资产库搭建/流程大纲/软件确立','插件: 各种插件运用体系','效果: 提交审核场景效果标准确立','灯光: 基础标准灯光确立']:
    n=N(910, sy2, 300, 50, t, SC); E(scene_norm, n); sy2+=65

# AI技术运用
ai_norm = N(1320, row_y, 280, 60, '## AI技术运用', AC); E(root, ai_norm)
ay=1020
for t in ['生成三视图','图片生成模型资产','摆放']:
    n=N(1330, ay, 260, 50, t, AC); E(ai_norm, n); ay+=65

# Validation
nids = set()
for n in nodes:
    assert n['id'] not in nids, f'Duplicate node {n["id"]}'
    nids.add(n['id'])
for e in edges:
    assert e['id'] not in nids, f'Duplicate edge {e["id"]}'
    assert e['fromNode'] in nids, f'Dangling fromNode {e["fromNode"]}'
    assert e['toNode'] in nids, f'Dangling toNode {e["toNode"]}'
    nids.add(e['id'])

print(f'VALID: {len(nodes)} nodes, {len(edges)} edges')

# Write
output_path = 'D:/TA/TA_Obsidian/Obsidian_TA/00_展示/00_流程规范/影视项目UE流程化.canvas'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({'nodes': nodes, 'edges': edges}, f, ensure_ascii=False, indent=2)
print(f'Written to: {output_path}')
