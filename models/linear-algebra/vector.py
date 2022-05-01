import math
from typing import List

if __name__ == '__main__':
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
