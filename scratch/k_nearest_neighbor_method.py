# 基于如下要求：
#       某种距离概念
#       彼此接近的点相似
from typing import List
from collections import Counter


def raw_majority_vote(labels: List[str]) -> str:
    """
    Return the most common label in the list of labels.
    """
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


# k最近邻法，我总想念成“k最邻近法”...
assert raw_majority_vote(['a', 'd', 'b', 'b', 'c', 'c', 'd', 'd']) == 'd'
