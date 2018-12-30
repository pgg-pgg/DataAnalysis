from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
# 数据在y轴的位置，是一个可迭代对象

plt.plot(x, y)
plt.show()
 