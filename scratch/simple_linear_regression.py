# 一个简单的线性预测函数 y = βx+α+e
# 假设描述的是朋友数量 x 和在线时长 y 的关系，e是噪声，代表与真实值的差异（越小越好），其余两个是使线性猜测关系成立的参数
from typing import Tuple
from scratch.linear_algebra import Vector
from scratch.statistics import correlation, standard_deviation, mean, de_mean, num_friends_good, daily_minutes_good
import random
import tqdm
from scratch.gradient_descent import gradient_step


def predict(alpha, beta, x_i: float) -> float:
    return beta * x_i + alpha


def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """
    当实际值为y_i时
    返回预测结果beta * x_i + alpha与实际值的误差
    """
    return predict(alpha, beta, x_i) - y_i


# 求总误差，为了防止正负抵消，故求平方的和
def sum_of_sqerrors(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))


# 学了两天最小二乘法，被折磨了两天，当然还有最近必不可少的加班环节
# 上面完了就是大家喜闻乐见的线性回归求值环节

def least_squares_fit(x: Vector, y: Vector) -> Tuple[float, float]:
    """
    给定两个向量x和y
    找到alpha和beta的最小二乘值
    斜率在这里用的是x，y的相关性系数乘y的标准差，最后除以x的标准差
    截距是y的平均值减去x的平均值乘以斜率
    """
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)
print(alpha, beta)
assert 22.9 < alpha < 23.0
assert 0.9 < beta < 0.905


# 衡量拟合准确度，决定系数（coefficient of determination）或 R 平方 （R-squared），它表示模型捕获的因变量变化在总变化中的占比。R 平方越高，模型与数据的拟合程度越好。
def total_sum_of_squares(y: Vector) -> float:
    """y_i与其均值差的平方和"""
    return sum(v ** 2 for v in de_mean(y))


def r_squared(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    """
    模型捕获的y的变化量，等于
    1 - 模型未捕获的y的变化量
    """
    return 1.0 - (sum_of_sqerrors(alpha, beta, x, y) / total_sum_of_squares(y))


rsq = r_squared(alpha, beta, num_friends_good, daily_minutes_good)
print(rsq)
assert 0.328 < rsq < 0.330

# 梯度下降


num_epochs = 10000
random.seed(0)
guess = [random.random(), random.random()]  # 选择随机数开始
learning_rate = 0.00001
# tqdm是一个进度条，可以让我们看到进度
with tqdm.trange(num_epochs) as t:
    for _ in t:
        alpha, beta = guess
        # 损失函数对于alpha的偏导数
        grad_a = sum(2 * error(alpha, beta, x_i, y_i)
                     for x_i, y_i in zip(num_friends_good,
                                         daily_minutes_good))
        # 损失函数对于beta的偏导数
        grad_b = sum(2 * error(alpha, beta, x_i, y_i) * x_i
                     for x_i, y_i in zip(num_friends_good,
                                         daily_minutes_good))
        # 在tqdm描述中计算损失
        loss = sum_of_sqerrors(alpha, beta,
                               num_friends_good, daily_minutes_good)
        t.set_description(f"loss: {loss:.3f}")
        # 最后更新guess
        guess = gradient_step(guess, [grad_a, grad_b], -learning_rate)
# 我们应该得到基本一致的结果
alpha, beta = guess
print(alpha, beta)
assert 22.9 < alpha < 23.0
assert 0.9 < beta < 0.905
