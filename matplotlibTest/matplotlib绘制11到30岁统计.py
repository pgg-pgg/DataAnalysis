from matplotlib import pyplot as plt
from matplotlib import font_manager

font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 1, 1, 6, 4, 3, 7, 4, 4, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1]

x = range(11, 31)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y_1, label='自己', color='orange', linestyle=':')
plt.plot(x, y_2, label='同桌', color='cyan', linestyle='-.')

#   设置x轴刻度
_x_ticks = ['{}岁'.format(i) for i in x]
plt.xticks(x, _x_ticks, fontproperties=font)
plt.grid(alpha=0.4)
# 添加描述信息
plt.xlabel('岁数', fontproperties=font)
plt.ylabel('男（女）朋友数', fontproperties=font)
plt.title('11岁到30岁男（女）朋友统计', fontproperties=font)
plt.legend(prop=font, loc='upper left')
plt.show()
