# 基于如下要求：
#       某种距离概念
#       彼此接近的点相似
import random
from typing import List, NamedTuple, Tuple
from collections import Counter
from linear_algebra import distance, Vector
from typing import Dict
import csv
from collections import defaultdict
from machine_learning import split_data


# 假设案例为：住的近的人更容易给同一个人投票
def raw_majority_vote(labels: List[str]) -> str:
    """
    Return the most common label in the list of labels.
    """
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


# k最近邻法，我总想念成“k最邻近法”...虽然这里还不是
assert raw_majority_vote(['a', 'd', 'b', 'b', 'c', 'c', 'd', 'd']) == 'd'


def majority_vote(labels: List[str]) -> str:
    vote_count = Counter(labels)
    winner, winner_count = vote_count.most_common(1)[0]
    num_winners = len([count for count in vote_count.values() if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])


# 这是python的继承机制，原来类的参数的顺序决定了构造函数中参数的顺序...
class LabeledPoint(NamedTuple):
    point: Vector
    label: str


# k nearest neighbors classification algorithm
# k-近邻分类算法
def knn_classify(k: int, labeled_points: List[LabeledPoint], new_point: Vector) -> str:
    """
    Return the classification of new_point based on its k nearest neighbors;
    将会比较并排序所有的数据集，然后选择前k个最近的点
    """
    by_distance = sorted(labeled_points, key=lambda lp: distance(lp.point, new_point))
    # k 个最邻近的标签
    k_nearest_labels = [label for _, label in by_distance[:k]]
    # 投票
    return majority_vote(k_nearest_labels)


# Comma Separated Values (CSV) 文件，即逗号分割值，一行中以逗号分割所有值，约定优于配置。

def parse_iris_row(row: List[str]) -> LabeledPoint:
    """
    sepal_length, sepal_width, petal_length, petal_width, class
    """
    measurements = [float(value) for value in row[:-1]]
    # python 的语法写起来好难受啊...
    label = row[-1].split("-")[-1]
    return LabeledPoint(measurements, label)


with open("dataset/iris.data") as iris_csv:
    reader = csv.reader(iris_csv)
    next(reader)
    iris_data = [parse_iris_row(row) for row in reader]

# defaultdict(list),key-value的形式，value是一个list
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

random.seed(12)
iris_train, iris_test = split_data(iris_data, 0.70)
assert len(iris_train) == 104
assert len(iris_test) == 45

# 记录我们做了多少次(预测值, 真实值)
confusion_matrix: Dict[Tuple[str, str], int] = defaultdict(int)

num_correct = 0
for iris in iris_test:
    predicted = knn_classify(5, iris_train, iris.point)
    actual = iris.label
    if predicted == actual:
        num_correct += 1
    confusion_matrix[(predicted, actual)] += 1

pct_correct = num_correct / len(iris_test)
print(pct_correct, confusion_matrix)
