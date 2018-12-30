from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# windows和linux设置字体
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 5}
# matplotlib.rc('font', **font)

font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)
# 调整x轴刻度
_x_ticks = ['10点{}分'.format(i) for i in range(60)]
_x_ticks += ['11点{}分'.format(i) for i in range(60)]
plt.xticks(list(x)[::5], _x_ticks[::5], rotation=45, fontproperties=font)

# 添加描述信息
plt.xlabel('时间',fontproperties=font)
plt.ylabel('温度 单位（）',fontproperties=font)
plt.title('10点到12点每分钟的气温变化情况',fontproperties=font)
plt.show()
