# 生成 10 个 1 到 100 之间的随机整数，存进列表。
import random

random_list = [random.randint(1, 100) for _ in range(10)]
print(random_list)
