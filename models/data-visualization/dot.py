from matplotlib import pyplot as plt

if __name__ == '__main__':
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
