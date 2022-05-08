import enum, random
import math
import matplotlib.pyplot as plt


# 条件概率
# 当事件E与事件F相互独立时，概率P(E, F) = P(E) * P(F)
# 如果两者不一定独立，那么将E关于F的概率记为P(E | F) = P(E,F) / P(F)，可以理解为已知F发生的情况下，E的概率
# 更常用的是 P(E,F) = P(E | F) * P(F)
# 当 E 与 F 相互独立时，P(E | F) = P(E)
# 下述例子是一个条件概率的例子：
# 该例子基于如下假设
# 1. 每个孩子是男孩还是女孩的概率是相同的
# 2. 老二的性别与老大的性别概率相互独立
# 问：事件 B “两个孩子都是女孩” 关于事件 G “老大是女孩” 的条件概率是多少？
# 回答：P(B | G) = P(B, G) / P(G) = P(B) / P(G) = 1/2


# 那么事件 B “两个孩子是女孩”关于 事件 L “至少一个孩子是女孩”的概率是多少？至少一个是女孩有几种可能性呢？ 男男，男女，女男，女女
# P(B | L) = P(B, L) / P(L) = P(B) / P(L) = 1/3
# 下面简单验证一下
class Kid(enum.Enum):
    BOY = 0
    GIRL = 1


# 随机生成孩子
def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girls = 0
either_girls = 0

random.seed(0)

for _ in range(1000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girls += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girls += 1

print("P(both | older):", both_girls / older_girls)
print("P(both | either):", both_girls / either_girls)

# 贝叶斯定理
# 假如要计算事件 E 基于已发生的事件 F 的条件概率，但仅仅已知事件 F 基于已发生的事件 E 的条件概率。则有：
#                                   P(E|F) = P(E,F)/P(F) = P(F|E) * P(E) / P(F)
# 其中，P(F|E) 是 F 基于 E 的条件概率，P(E) 是 E 的概率，P(F) 是 F 的概率。
# 事件 F 可以分成一对互斥事件：F 与 E 同时发生，或 F 发生而 E 不发生。将 E 不发生记为 ¬E ，那么
#                                   P(F) = P(F, E) + P(F, ¬E)
# 所以：
#                                   P(E|F) = P(F|E) * P(E) / [P(F | E) * P(E) + P(F | ¬E) * P(¬E)]
# 这就是贝叶斯定理的常用表达式。
# 下面依据一个简单的例子来说明贝叶斯定理：
# 某疾病在人群中的发病率为 0.01%，针对该病的检测，正确率为 99%(意思为：“患病”测试时，表示患病，“无病”测试时，表示为无病)，也就是说，存在 1% 的误诊率。
# 那么当一个患者被检测结果为阳性时，代表了什么？
# 用 T 表示“测试结果为阳性”，用 D 表示患病。依据贝叶斯定理，测试结果为阳性时，患病的概率为：
#                                   P(D|T) = P(T|D) * P(D) / [P(T|D) * P(D) + P(T|¬D) * P(¬D)]
# 通俗解释来说，就是检测结果为阳性，且患病的概率为：患病且阳性的概率，除以患病且阳性的概率加上不患病且阳性的概率
# 编程为：
T = 0.99
D = 0.0001


# d 患病率，t 诊断正确率
def disease_rate(d, t: float) -> float:
    return (t * d) / ((t * d) + (1 - t) * (1 - d))


print(disease_rate(D, T))

# Google了一下，白癜风的误诊率约为 72%，而白癜风世界发病率为 0.5%，那么一个人被诊断为白癜风后，确实患有白癜风的概率为：
print("患白癜风概率为")
print(disease_rate(0.005, 1 - 0.72))


# 当然，这仅仅是概率

# 概率密度函数 Probability Density Function
# 当区间连续时，使用连续分布的概率密度函数来表示区间内某个值的概率，这个概率即为该区间内的概率密度函数的积分。
# 均匀分布的概率密度函数
def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0


# 累积分布函数 Cumulative Distribution Function
# CDF给出了一个随机变量小于或等于某个特定值的概率。
# 均匀分布的累积分布函数
def uniform_cdf(x: float) -> float:
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


# 正态分布
# 钟形曲线分布（os：传说中的万物之理），仅由两个参数决定其形态：均值μ和标准差σ
# 均值表示曲线的中心位置，标准差表示曲线的宽度。
# 正态分布的概率密度函数

SQRT_TWO_PI = math.sqrt(2 * math.pi)


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma)


# 多个正态分布的概率密度函数
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")

plt.show()


# 当 μ = 0 且 σ = 1 时，称为标准正态分布 standard normal distribution，如果Z是服从标准正态分布的随机变量，那么会有如下关系：
#                                   X = σX + μ
# 其中 X 是正态分布，但均值是 μ ，标准差是 σ。相反，如果 X 是有均值 μ 和标准差 σ 的正态随机变量，则：
#                                   Z = (X - μ) / σ
# 是标准正态分布的随机变量

# 正态分布的累积分布函数不能用"基本"的方式编写 <- 实际上就是不能用初等函数表示，俗称“积不出”。但可以用误差函数math.erf编写：
def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# 多个正态分布的累积分布函数
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label="mu = 0,sigma = 1")
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu = 0,sigma = 2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu = 0,sigma = 0.5')
plt.plot(xs, [normal_cdf(x, mu=-1, sigma=1) for x in xs], '-.', label='mu = -1,sigma = 1')
plt.legend(loc=4)  # 底部右边
plt.title("Various Normal cdfs")
plt.show()


# 逆运算正态分布函数
# 通过逆运算来找到对应的特定概率的值，由于normal_cdf是连续的并且严格递增，所以可以使用二分查找来实现（突然想到这不就是传说中的查表法么）：
def inverse_normal_cdf(p: float, mu=0, sigma=1, tolerance: float = 0.00001) -> float:
    """使用二分查找来得到近似值"""
    mid_z = 0.0
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z = -10.0  # normal_cdf(-10) 非常接近 0
    hi_z = 10.0  # normal_cdf(10) 非常接近 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z
    return mid_z

# 中心极限定理 central limit theorem
# 中心极限定理表示，一个随机变量定义为大量独立同分布的随机变量的均值，它本身就是接近于正态分布的。
# 具体来说，如果x1,x2,...,xn是均值 μ，标准差 σ 的随机变量，那么当 n 很大时，有：
#                       (x1+...+xn)/n
# 近似正态分布，且均值为 μ ，标准差为 σ / √n 。等价于
#                       ((x1+...+xn)-μn)/σ√n
# 此结果近似于正态分布，且均值为 0 ，标准差为 1

