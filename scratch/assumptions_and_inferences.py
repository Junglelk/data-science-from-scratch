# 典型的假设步骤如下所示：
# 首先有一个零假设H0，代表一个默认立场，而替代假设H1代表我们希望与零假设对比的立场。
# 用统计学判断H0是否错误，从而决定是否可以拒绝它。

from typing import Tuple
import math


# 实例：掷硬币
# 假设有一枚硬币，我们想测试它是否均匀。假设掷硬币正面向上的概率为p，零假设是硬币均匀，即 p = 0.5,替代假设p != 0.5。
# 使用正态分布拟合二项式随机变量Binomial(n,p)
def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """
    返回一个Binomial(n,p)分布的mu和sigma
    """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma
