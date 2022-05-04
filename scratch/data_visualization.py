from collections import Counter
from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# 以[0, 1, 2, 3, 4] 为横坐标，[num_oscars] 为高度制作条形图
plt.bar(range(len(movies)), num_oscars)

# 添加标题
plt.title("My Favorite Movies")
# 添加Y轴标签
plt.ylabel("# of Academy Awards")

# X轴以电影名为标签
plt.xticks(range(len(movies)), movies)
plt.show()

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# // 表示整数除法，向下取整
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
# 每个条形向右移动5个单位，设置每个条形的高度，每个条形设置宽度为 10 ，边框为黑色。直条是以长方形的左下角为基准
plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0))
# x 轴取值范围为 (-5,105) ，y 轴取值范围为 (0,5)
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.xlabel("# of Students")
plt.title("Distribution of Exam 1 Grands")

plt.show()

years = [2017, 2018]
mentions = [500, 505]
plt.bar(years, mentions, 0.8)
plt.xticks(years)
# 虽然书上讲，这不这么写，matplotlib会将x轴的刻度设置为0，1
# 然后在角上加上+2.013e3。但我跑出来的好像没看到...
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5, 2018.5, 0, 506])
# 下面这个y的范围会非常离谱
# plt.axis([2016.5, 2018.5, 499, 506])
plt.show()

# dot
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# 此时散点图已经完成
plt.scatter(friends, minutes)
# 给每个点加标签
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),  # 把标签放在对应的点上
                 xytext=(5, -5),  # 也别正好放上去，设置点偏移量
                 textcoords='offset points'
                 )
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# line
print("hello world")
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14952.3]
# 创建一个以GDP为y轴，年份为x轴的线图
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# 添加标题
plt.title("Nominal GDP")
# 添加Y轴标签
plt.ylabel("Billions of $")
plt.show()

# linegraph
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
# enumerate 能获取下标的迭代器
xs = [i for i, _ in enumerate(variance)]
# 多次调用plt.plot，可以在同一张图上绘制多个序列
plt.plot(xs, variance, 'g-', label='variance')  # 绿色实线
plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # 红色点虚线
plt.plot(xs, total_error, 'b:', label='total error')  # 蓝色点线
# 9 表示“顶部中央”
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()
