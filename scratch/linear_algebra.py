import math
from typing import List, Tuple

Matrix = List[List[float]]
Vector = List[float]


# 废话不多说了，表示矩阵的方式为数组列表，或者你说列表的列表也行
# value_1 if condition else value_2 是python的三目运算符，python中，非空和非0即为true
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_lines = len(A[0]) if A else 0
    return num_rows, num_lines


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, i: int) -> Vector:
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]


# 上面俩函数顾名思义啦

# vector
Vector = List[float]
height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]


# 向量相加 （长度不同的向量无法相加）
def add(v: Vector, w: Vector) -> Vector:
    """加对应的元素"""
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


# 矩阵乘常数，就直接乘就好了，没啥特别的，略过
# 点乘，向量对应位置处的元素的乘积之和，延申用于求向量平方和以及长度，不做赘述
def dot(v, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(sum_of_squares(add(v, w)))


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))
