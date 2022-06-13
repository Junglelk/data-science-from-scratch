# 前面描述观测值与实际函数的相关关系 y_i = βx_i+α+e_i
# 参数换为
# beta=[alpha, beta_1, beta_2, ..., beta_k]
# x_i=p[1,x_i1,x_i2,...,x_ik]

from scratch.linear_algebra import dot, Vector
from typing import List


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
