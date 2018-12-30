from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


def random_list(start, stop, length):
    if length >= 0:
        length = int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


a = random_list(78, 156, 100)

# 计算组数
d = 3  # 组距
num_bins = (max(a) - min(a)) // d

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(a, num_bins, normed=True)
plt.xticks(range(min(a), max(a) + d, d))
plt.grid()
plt.show()
