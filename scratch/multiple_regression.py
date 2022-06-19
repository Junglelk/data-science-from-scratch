# 前面描述观测值与实际函数的相关关系 y_i = βx_i+α+e_i
# 参数换为
# beta=[alpha, beta_1, beta_2, ..., beta_k]
# x_i=p[1,x_i1,x_i2,...,x_ik]

from scratch.linear_algebra import dot, Vector
from typing import List
import random
import tqdm
from scratch.linear_algebra import vector_mean
from scratch.gradient_descent import gradient_step


# 模型为
def predict(x: Vector, beta: Vector) -> float:
    return dot(x, beta)


# 误差函数，与之前的没啥差别
def error(x: Vector, y: float, beta: Vector) -> float:
    return predict(x, beta) - y


# 平方误差函数，用于应用最小二乘法
def squared_error(x: Vector, y: float, beta: Vector) -> float:
    return error(x, y, beta) ** 2


x = [1, 2, 3]
y = 30
beta = [4, 4, 4]  # 预测结果 = 4 + 8 + 12 = 24
assert error(x, y, beta) == -6
assert squared_error(x, y, beta) == 36


# 梯度，此处即对x_i求导
def sqerror_gradient(x: Vector, y: float, beta: Vector) -> Vector:
    err = error(x, y, beta)
    return [2 * err * x_i for x_i in x]


assert sqerror_gradient(x, y, beta) == [-12, -24, -36]


def least_squares_fit(xs: List[Vector],
                      ys: List[float],
                      learning_rate: float = 0.001,
                      num_steps: int = 1000,
                      batch_size: int = 1) -> Vector:
    """
    假设模型y = dot(x, beta)
    找到使平方误差和最小的beta
    """
    # 先随机初始化权重
    guess = [random.random() for _ in xs[0]]
    for _ in tqdm.trange(num_steps, desc="least squares fit"):
        for start in range(0, len(xs), batch_size):
            batch_xs = xs[start:start + batch_size]
            batch_ys = ys[start:start + batch_size]
            # 求导
            # 获取误差函数列表（向量），求误差函数的梯度，并使用梯度的均值作为实际梯度（为什么，减小误差吗，常用的处理方式？）
            gradient = vector_mean([sqerror_gradient(x, y, guess) for x, y in zip(batch_xs, batch_ys)])
            # 梯度下降
            guess = gradient_step(guess, gradient, -learning_rate)
    return guess
