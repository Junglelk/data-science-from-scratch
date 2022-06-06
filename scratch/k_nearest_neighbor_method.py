# 基于如下要求：
#       某种距离概念
#       彼此接近的点相似
from typing import List, NamedTuple
from collections import Counter
from linear_algebra import distance, Vector
from typing import Dict
import csv
from collections import defaultdict


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


# 这是python的继承机制
class LabeledPoint(NamedTuple):
    labels: str
    point: Vector


# k nearest neighbors classification algorithm
# k-近邻分类算法
def knn_classify(k: int, labeled_points: List[LabeledPoint], new_point: Vector) -> str:
    """
    Return the classification of new_point based on its k nearest neighbors
    """
    by_distance = sorted(labeled_points, key=lambda lp: distance(lp.point, new_point))
    # k 个最邻近的标签
    k_nearest_labels = [label for _, label in by_distance[:k]]
    # 投票
    return majority_vote(k_nearest_labels)
