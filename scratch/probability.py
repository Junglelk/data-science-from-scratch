import enum, random


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
