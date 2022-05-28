# 梯度下降
# 数据科学的工作会尝试为某种场景找到最佳模型，“最佳”一般指"最小化模型残差"或"最大化数据的可能性"。
# 梯度下降是一种算法，用于求解这种最佳模型的损失函数的最小值。
# 梯度下降的基本思想是：
# 1. 初始化一个模型参数，
# 2. 对模型参数进行更新，
# 3. 重复步骤2，直到模型参数不再改变。
# 上面从梯度下降的介绍开始，就是GitHub Copilot不知道从哪抄来的，还算有点用(doge
import random

from scratch.linear_algebra import Vector, dot
from typing import Callable
from scratch.linear_algebra import distance, add, scalar_multiply, vector_mean


def sum_of_squares(v: Vector) -> float:
    """v的平方和"""
    return dot(v, v)


# Callable 是一个函数类型，即可以调用的对象。
# f是单变量函数，下面这个可以视为f的求导
def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
    """
    :param f: 函数
    :param x: 参数
    :param h: 增量（趋近于0）
    :return: f的导数
    """
    return (f(x + h) - f(x)) / h


# f为多变量函数时，它有多个偏导数.
def partial_difference_quotient(f: Callable[[Vector], float], v: Vector, i: int, h: float) -> float:
    """
    返回f在v的第i个元素的偏导数（偏差商）
    :param f: 函数
    :param v: 参数
    :param i: 参数索引
    :param h: 增量（趋近于0）
    :return: f的第i个偏导数
    """
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


# 估算梯度
def estimate_gradient(f: Callable[[Vector], float], v: Vector, h: float = 0.00001) -> Vector:
    """
    估算梯度
    :param f: 函数
    :param v: 参数
    :param h: 增量（趋近于0）
    :return: 梯度
    """
    return [partial_difference_quotient(f, v, i, h) for i in range(len(v))]


# 使用梯度
def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """
    从 v 朝着 ‘gradient’ 方向，前进 step_size 距离
    :param v: 参数
    :param gradient: 梯度
    :param step_size: 步长
    :return: 更新后的参数
    """
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


# 就是求导啊，淦
def sum_of_squares_gradient(var: Vector) -> Vector:
    """
    对于v的平方和的梯度
    :param var: 参数
    :return: 梯度
    """
    return [2 * v_i for v_i in var]


# 选择一个随机的初始值
v = [random.randint(-10, 10) for i in range(3)]

for epoch in range(1000):
    # 估算梯度
    gradient = sum_of_squares_gradient(v)
    # 更新参数
    v = gradient_step(v, gradient, -0.01)
    print("epoch {}, v = {}".format(epoch, v))

assert distance(v, [0, 0, 0]) < 0.001
print(distance(v, [0, 0, 0]))

# 使用梯度下降拟合模型
# 使用梯度下降拟合参数化模型到数据，并且使用损失函数来衡量模型与数据的匹配程度
# 一个简单的线性函数(计算所得的数据集)
inputs = [(x, x * 20 + 5) for x in range(-50, 50)]


# 使用梯度下降来找到最小化平方误差的斜率和截距
def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    # 斜率与截距
    slope, intercept = theta
    predicted = slope * x + intercept  # 模型的预测结果
    error = predicted - y  # 残值是(预测值-真实值)
    squared_error = error ** 2  # 最小化平方误差，损失函数
    grad = [2 * error * x, error * 2]  # 梯度，梯度是损失函数对slop和intercept的偏导数，最终求的是损失函数的最小值
    return grad


# 我不能理解的是为什么这样计算梯度。最小化平方误差是为了修正负数带来的比较问题吗？
# 梯度是：是一个向量（矢量），表示某一函数在该点处的方向导数沿着该方向取得最大值。
# 接下来的流程是
# 1. 随机初始化theta
# 2. 计算梯度的均值
# 3. 沿该方向调整theta
# 4. 重复上述步骤
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
learning_rate = 0.001
for epoch in range(100):
    for x, y in inputs:
        # 计算梯度的均值
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
        # 更新参数
        theta = gradient_step(theta, grad, -learning_rate)
        print("epoch {}, theta = {},grad = {}".format(epoch, theta, grad))

slope, intercept = theta
print(slope)
print(intercept)
