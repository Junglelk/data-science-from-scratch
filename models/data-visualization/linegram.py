from matplotlib import pyplot as plt

if __name__ == '__main__':
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
