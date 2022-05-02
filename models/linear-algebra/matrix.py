from typing import List, Tuple

Matrix = List[List[float]]
Vector = List[float]

if __name__ == '__main__':
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


