# 典型的假设步骤如下所示：
# 首先有一个零假设H0，代表一个默认立场，而替代假设H1代表我们希望与零假设对比的立场。
# 用统计学判断H0是否错误，从而决定是否可以拒绝它。

from typing import Tuple
import math
import random

# 实例：掷硬币
# 假设有一枚硬币，我们想测试它是否均匀。假设掷硬币正面向上的概率为p，零假设是硬币均匀，即 p = 0.5,替代假设p != 0.5。
# 使用正态分布拟合二项式随机变量Binomial(n,p)
from scratch.probability import normal_cdf
from scratch.probability import inverse_normal_cdf
from typing import List


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
    return normal_cdf(lo, mu, sigma) - normal_cdf(hi, mu, sigma)


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

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print(mu_0)  # mu_0 为500
print(sigma_0)  # sigma_0 为 15.8

# 写到这里时发现运行报错 cannot import name 'ft2font' from...
# 执行python -m pip install -I matplotlib 强制安装 matplotlib 后好了（在IDE内部似乎又更新了一遍）

# 需要对显著性 significance 下定义以避免第一类错误（“假阳性”），即拒绝了H0，而实际上 H0 为真。
# 如果我们有5%的可能性错判，则 X 应当的区间是(469,531)，在区间外时，拒绝原假设H0。小提示，X 是指正面朝上的概率
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print(lower_bound)  # 531
print(upper_bound)  # 469

# 若p真的等于0.5 则，我们只有5%的概率观察倒一个位于这个区间之外的X。换句话说，若H0为真，则20次观测大约有19次可以得到正确结果。
# 第二类错误，“假阴性”，即零假设为假，但我们没能拒绝H0。我们称犯第二种错误的概率为“势”。
# 在探究势之前，我们必须知道 H0 为假究竟是什么意思。零假设为 p 为 0.5。如果仅仅说 p 不为 0.5 不能提供足够的信息。

# 当p是0.5时 95% 的边界
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# 当 p 是 0.55 时的真实mu 和 sigma
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
print("power")
print(power)  # 0.887

# 假设零假设是掷硬币不偏正面朝上，即 p <= 0.5。这种情况下，需要使用单边检验 one-side test。当 X 远大于500时拒绝原假设，但 X 小于 500 时不拒绝原假设。
# 因此，5%显著性检验需要使用 normal_probability_below 找到低于 95% 概率对应的截点

hi = normal_upper_bound(0.95, mu_0, sigma_0)
# 是 526 (< 531 因为在上尾部需要更多的概率)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
print(power)  # 0.936


# 这是一个更有效的检验，因为当 X 小于 469 时不再拒绝 H0 (如果 H1 为真，这种情况就太可能发生)，
# 当 X 在 526 和 531 之间时拒绝H0(如果 H1 为真，则很有可能发生这种情况)。


# p值
# P值（P value）就是当原假设为真时，比所得到的样本观察结果更极端的结果出现的概率。这是百度百科中的解释，而本书中，如下叙述p值：
# 我们不是根据某个概率截点选择临界值，而是计算概率：假设H0为真，则我们可以找到一个至少与实际观测到的值一样极端的值。
# 对于硬币是否均匀的双面检验，做以下运算
def two_side_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    如果数值来自于N(mu,sigma)，那么得到一个至少与x极限接近的值（在任意方向上）的可能性有多大
    :param x:
    :param mu:
    :param sigma:
    :return:
    """
    if x >= mu:
        # 如果 x 大于均值，tail代表所有比x大的数
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # 如果 x 小于均值，tail代表所有比x小的数
        return 2 * normal_probability_below(x, mu, sigma)


# 如果要观测到530次正面朝上，需要这么计算
print(two_side_p_value(529.5, mu_0, sigma_0))  # 0.062

# 连续校正 continuity correction 关于连续校正的说明如右 → https://www.statisticshowto.com/what-is-the-continuity-correction-factor/
# 用于精确拟合离散变量到连续变量上。所以529.5是比530更好的估计。

extreme_value_count = 0
for _ in range(1000):
    # sum 内的函数就是在模拟掷1000次硬币
    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1
# p 值是 0.062 即1000次观测中，极值大约出现62次
assert 59 < extreme_value_count <= 65, f"{extreme_value_count}"

# 由于6.2% > 5% ，所以不拒绝原假设。如果改为观测到532次正面向上，那么相应的p值为：
print(two_side_p_value(531.5, mu_0, sigma_0))  # 0.046
# 小于 5% 的显著性，所以拒绝原假设。
# 这含义为：观测到532次正面向上的概率为4.6%，而我们假设的正面朝上概率为0.5时出现这么极端的观测值的合理概率（显著性为5%）更低，所以拒绝原假设。

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below
# 观测到525次正面朝上
print(upper_p_value(524.5, mu_0, sigma_0))  # 0.061，接受原假设
# 观测到527次正面朝上
print(upper_p_value(526.5, mu_0, sigma_0))  # 0.047，拒绝原假设

# 上述检测与之前的结果一致，只是计算方式有所不同。
# 此外，词用normal_probability_above计算p值前，需确保原数据大致符合正态分布。

# 置信区间
# 上述都是关于正面朝上概率p的假设检验，是未知的“正面朝上”分布的参数。在这种情况下，第三种方式是围绕参数的观测值构建置信区间 confidence interval。
# 可以计算每次掷的伯努利变量的均值来估计不均匀硬币的概率，如果正面向上记为 1 ，否则记为 0 。如果在1000次掷硬币中观测到525次正面朝上，
# 那么可以估计 p 等于 0.525。
# 这个估计的可信度如何呢？如果已知p的精确值，那么依据中心极限定理（一个随机变量，定义为大量独立同分布的随机变量的均值，它本身就是接近正态分布的）
# 伯努利变量的均值应当近似于正态分布，均值为 p ，标准差为 sqrt( p *(1-p) /1000)。
# 由于p值位置，因此使用估计值：
p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)
# 可以近似计算出下列区间包含可真实参数p的“可信度有95%”
print(normal_two_sided_bounds(0.95, mu, sigma))  # (0.4940,0.5560)


# p-Hacking
def run_experiment() -> List[bool]:
    """翻转均匀硬币1000次，True=正面朝上 ， False=正面朝下"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment: List[bool]) -> bool:
    """使用5%的显著性水平"""
    # 1000的5%是50，
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531


random.seed(0)
# 重复进行1000次实验，每次实验掷硬币1000次
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment for experiment in experiments if reject_fairness(experiment)])
assert num_rejections == 46

# 这表示如果想得到一个具有“显著性”的结果，通常可以重复实验多次，直到达到一个显著性水平。或者删除右边的数据，从而得到一个低于0.05的p值，
# 这样就达到了符合期望的结果，当然这损害了部分客观性。这有时被成为 p-hacking。详细的可以看 The Earth Is Round , 由Jacob Cohen撰写的一篇文章。
