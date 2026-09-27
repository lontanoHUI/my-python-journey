# 找出第二大的数，重复的最大值算一次
def findSecondMax(num):
    unique = list(set(num))  # 去重
    unique.sort(reverse=True)  # 降序排列
    return unique[1]  # 返回第二大的数


print(findSecondMax([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]))  # 输出：8
