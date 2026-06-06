# VEX

## GPT辅助节点设计以及VEX

### // 洛伦兹系统参数 float sigma = 10.0; float rho = 28.0; float beta = 8.0 / 3.0;  // 初始点和步长 vector pos = {0.0, 1.0, 1.05};  // 初始位置 float dt = 0.01;  // 时间步长  // 获取外部调节的步数参数（整数类型） int steps = chi("steps");  // chi() 用于整数参数  // 检查是否有正的步数 if (steps > 0) {     // 创建洛伦兹曲线     for (int i = 0; i < steps; i++) {         // 计算洛伦兹微分方程         float dx = sigma * (pos.y - pos.x) * dt;         float dy = (pos.x * (rho - pos.z) - pos.y) * dt;         float dz = (pos.x * pos.y - beta * pos.z) * dt;                  // 更新位置         pos.x += dx;         pos.y += dy;         pos.z += dz;                  // 在每个位置上添加一个点         addpoint(geoself(), pos);     } }

## [入门中文教程，有工程文件](https://www.bilibili.com/video/BV1Zp411d7Hw/?spm_id_from=333.999.0.0&vd_source=089349bc15fe4a0508fc235b6d5563a8)

## [Houdini Python城市[中文翻译]](https://www.bilibili.com/video/av20882458/?vd_source=089349bc15fe4a0508fc235b6d5563a8)

## 小案例

### [Houdini中使用VEX对任意四边面进行随机分割](https://www.bilibili.com/video/BV1nJ411g7Mg/?spm_id_from=333.337.search-card.all.click&vd_source=089349bc15fe4a0508fc235b6d5563a8)

## 湖边小屋

### [中文拆解教程](https://www.bilibili.com/video/BV1Ly4y1i7Vx/?spm_id_from=333.999.0.0&vd_source=089349bc15fe4a0508fc235b6d5563a8)

### [付费课程](https://www.aboutcg.org/courseDetails/2103/introduce)

### 不适应实际工作流

## [Houdini Vex编程全面教程 中英文字幕](https://www.bilibili.com/video/BV1aX4y1N7fi/?spm_id_from=333.337.search-card.all.click&vd_source=089349bc15fe4a0508fc235b6d5563a8)
