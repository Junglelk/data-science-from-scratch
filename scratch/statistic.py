from collections import Counter
from typing import List
import math

import matplotlib.pyplot as plt

# 描述单个数据集
from scratch.linear_algebra import sum_of_squares, dot

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


# correlation
# 相关性

# 用户每天在本产品上花费的时间，分钟数
daily_minutes = [1, 68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, 54.01, 38.79, 47.59, 49.1,
                 27.66, 41.03, 36.73, 48.65, 28.12, 46.62, 35.57, 32.98, 35, 26.07, 23.77, 39.73, 40.57, 31.65, 31.21,
                 36.32, 20.45, 21.93, 26.02, 27.34, 23.49, 46.94, 30.5, 33.8, 24.23, 21.4, 27.94, 32.24, 40.57, 25.07,
                 19.42, 22.39, 18.42, 46.96, 23.72, 26.41, 26.97, 36.76, 40.32, 35.02, 29.47, 30.2, 31, 38.11, 38.18,
                 36.31, 21.03, 30.86, 36.07, 28.66, 29.08, 37.28, 15.28, 24.17, 22.31, 30.17, 25.53, 19.85, 35.37, 44.6,
                 17.23, 13.47, 26.33, 35.02, 32.09, 24.81, 19.33, 28.77, 24.26, 31.98, 25.73, 24.86, 16.28, 34.51,
                 15.23, 39.72, 40.8, 26.06, 35.76, 34.76, 16.13, 44.04, 18.03, 19.65, 32.62, 35.59, 39.43, 14.18, 35.24,
                 40.13, 41.82, 35.45, 36.07, 43.67, 24.61, 20.9, 21.9, 18.79, 27.61, 27.21, 26.61, 29.77, 20.59, 27.53,
                 13.82, 33.2, 25, 33.1, 36.65, 18.63, 14.87, 22.2, 36.81, 25.53, 24.62, 26.25, 18.21, 28.08, 19.42,
                 29.79, 32.8, 35.99, 28.32, 27.79, 35.88, 29.06, 36.28, 14.1, 36.63, 37.49, 26.9, 18.58, 38.48, 24.48,
                 18.95, 33.55, 14.24, 29.04, 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9, 27.2, 32.01, 29.27, 33, 13.74,
                 20.42, 27.32, 18.23, 35.35, 28.48, 9.08, 24.62, 20.12, 35.26, 19.92, 31.02, 16.49, 12.16, 30.7, 31.22,
                 34.65, 13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12, 24.42, 9.82, 23.39, 30.93, 15.03, 21.67,
                 31.09, 33.29, 22.61, 26.89, 23.48, 8.38, 27.81, 32.35, 23.84]

daily_hours = [dm / 60 for dm in daily_minutes]


# 协方差，方差衡量单个变量对其均值的偏离程度，协方差衡量两个变量对其均值的共同偏离程度
def covariance(x, y: List[float]) -> float:
    assert len(x) == len(y)
    return dot(de_mean(x), de_mean(y)) / (len(x) - 1)


assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60