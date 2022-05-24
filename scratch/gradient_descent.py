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
from scratch.linear_algebra import distance, add, scalar_multiply


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
