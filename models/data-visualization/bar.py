from collections import Counter

from matplotlib import pyplot as plt

if __name__ == '__main__':
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
