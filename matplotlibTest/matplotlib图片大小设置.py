from matplotlib import pyplot as plt

# 图片大小
fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
# 数据在y轴的位置，是一个可迭代对象

plt.plot(x, y)

# 设置x轴刻度
_tick_labels = [i / 2 for i in range(4, 49)]
plt.xticks(_tick_labels)

# 设置y轴刻度
plt.yticks(range(min(y), max(y)))

# 保存图片
# plt.savefig('./t1.png')
plt.show()
