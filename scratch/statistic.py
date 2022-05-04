from collections import Counter
from typing import List
import math

import matplotlib.pyplot as plt

# 描述单个数据集
from scratch.linear_algebra import sum_of_squares

num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12,
               11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")


# plt.show()

#  中心倾向 一般而言，描述数据中心位置最常见的方式是使用均值。
def mean(array: List[float]) -> float:
    return sum(array) / len(array)


print(mean(num_friends))  # 7.333333333333333


# 中位数,中间点的值(数据量为奇数时),中间两个点的值的平均值(数据量为偶数)
def _median_odd(array: List[float]) -> float:
    return sorted(array)[len(array) // 2]


def _median_even(array: List[float]) -> float:
    return sum(sorted(array)[len(array) // 2 - 1:len(array) // 2 + 1]) / 2


# 找到中位数
def median(array: List[float]) -> float:
    return _median_even(array) if len(array) % 2 == 0 else _median_odd(array)


# 中位数有一个广义上的定义:分位数(quantile)，它是一个百分比，指的是数据中的某个数值。中位数是50%分位数的值
def quantile(array: List[float], p: float) -> float:
    p_index = int(p * len(array))
    return sorted(array)[p_index]


assert quantile([1, 2, 3, 4, 5], 0.25) == 2


# 众数,出现最多次数的数,众数可能为多个
def mode(x: List[float]) -> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


# 离散度
# 极差，指最大值于最小值的差
def data_range(x: List[float]) -> float:
    return max(x) - min(x)


assert data_range(num_friends) == 99


def de_mean(x: List[float]) -> List[float]:
    x_bar = mean(x)
    """将xs变换为每个元素减去该向量均值的向量，因此新向量的均值为 0 """
    return [x_i - x_bar for x_i in x]


def variance(x: List[float]) -> float:
    """计算方差"""
    n = len(x)
    deviations = de_mean(x)
    """除以 n - 1 的原因是，当数据量很大时，x_bar只是实际均值的估计，
        因此使用(x_i - x_bar) ** 2是x_i的方差对均值的低估值，所以需要用 n - 1 做加权
    """
    return sum_of_squares(deviations) / (n - 1)


assert 81.54 < variance(num_friends) < 81.56


# 标准差，是方差的根，主要是为了方便统一单位
def standard_deviation(x: List[float]) -> float:
    return math.sqrt(variance(x))


# 标准差和极差都会受到异常值的干扰，更为稳妥的方式是计算75%分位数和25%分位数的分位数之差
def inter_quartile_range(x: List[float]) -> float:
    return quantile(x, 0.75) - quantile(x, 0.25)
