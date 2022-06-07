import random
from typing import Tuple, List, TypeVar

X = TypeVar('X')  # 定义一个数据点的泛型类型


def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """将数据按照分数[prob, 1 - prob]划分"""
    data = data[:]  # 浅副本
    random.shuffle(data)  # 打乱数据重排列表
    cut = int(len(data) * prob)  # 按比例去划分数据集
    return data[:cut], data[cut:]  # 切分打乱后的列表
