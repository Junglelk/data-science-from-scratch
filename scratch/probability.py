import enum, random


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
