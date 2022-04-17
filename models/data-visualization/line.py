from matplotlib import pyplot as plt

if __name__ == '__main__':
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
