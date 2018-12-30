from matplotlib import pyplot as plt
from matplotlib import font_manager

font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊"]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]

x = range(len(a))
y = b
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)
plt.barh(x, b, height=0.3, color='orange')
plt.yticks(x, a, fontproperties=font, rotation=45)

# 添加描述信息
plt.xlabel('调用名称', fontproperties=font)
plt.ylabel('票房（单位：亿）', fontproperties=font)
plt.title('2017年内地电影票房', fontproperties=font)

plt.show()
