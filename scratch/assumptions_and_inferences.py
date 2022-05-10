# 典型的假设步骤如下所示：
# 首先有一个零假设H0，代表一个默认立场，而替代假设H1代表我们希望与零假设对比的立场。
# 用统计学判断H0是否错误，从而决定是否可以拒绝它。

from typing import Tuple
import math

# 实例：掷硬币
# 假设有一枚硬币，我们想测试它是否均匀。假设掷硬币正面向上的概率为p，零假设是硬币均匀，即 p = 0.5,替代假设p != 0.5。
# 使用正态分布拟合二项式随机变量Binomial(n,p)
from scratch.probability import normal_cdf
from scratch.probability import inverse_normal_cdf


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """
    返回一个Binomial(n,p)分布的mu和sigma
    """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# 当随机变量服从正态分布时，我们可以使用normal_cdf函数来计算实现值位于特定区间之内或之外的概率。

# normal_cmf 是一个变量在某个阈值以下的概率
normal_probability_below = normal_cdf


# 如果不在阈值以下，就在阈值以上
def normal_probability_above(lo: float, mu: float = 0, sigma: float = 1) -> float:
    """一个N(mu,sigma)分布大于lo的概率"""
    return 1 - normal_cdf(lo, mu, sigma)


# 如果它小于hi，但大于等于lo
def normal_probability_between(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """一个N(mu,sigma)分布在lo和hi之间的概率"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# 如果不在区间之内，就在区间之外
def normal_probability_outside(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """一个N(mu,sigma)分布在lo和hi之外的概率"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)


# 可以找到非尾区域或者在均值两边（对称）区间。该区间代表特定比例的可能性。简而言之就是在中央（均值）两边寻找一个区间，由钟形曲线的两个尾端各自代表概率 p
# 则均值周围的区间概率为 1-2p
def normal_upper_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
    """"返回P(Z<=z) = 某概率的z值"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
    """"返回P(Z>=z) = 某概率的z值"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability: float, mu: float = 0, sigma: float = 1) -> Tuple[float, float]:
    """返回（关于均值）对称边界内的概率"""
    tail_probability = (1 - probability) / 2
    # 上界应有在它之上的tail_probability
    upper_bound = normal_upper_bound(tail_probability, mu, sigma)
    # 下界应有在它之下的tail_probability
    lower_bound = normal_lower_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound

# 看完上面的东西，突然意识到不知道 z值是什么东西，于是去搜了一下：
# Z 值是 Z 检验的检验统计量，它度量观测到的统计量与假设总体参数之间的差值，以标准差为单位。
# 例如，一系列工厂模具的平均深度为 10 厘米，标准差为 1 厘米。深度为 12 厘米的模具的 Z 值为 2，因为它的深度比均值大两个标准差；
# 可以使用 Z 值来确定是否要否定原假设。为了确定是否要否定原假设，请将 Z 值与临界值（可在大多数统计书籍中的标准正态表中找到）进行比较。
# 对于双侧检验，临界值是 Z1-α/2；对于单侧检验，临界值是 Z1-α。如果 Z 值的绝对值大于临界值，则否定原假设。否则，无法否定原假设。
#
# 例如，要了解另一组模具的平均深度是否也为 10 厘米。度量第二组中每个模具的深度，并计算组的平均深度。
# A 1 样本 Z 检验计算 -1.03 的 Z 值。可选择值为 0.05 的 α，这将产生临界值 1.96。
# 由于 Z 值的绝对值小于 1.96，因此不能拒绝原假设，并且不能断定模具的平均深度不是 10 厘米。
