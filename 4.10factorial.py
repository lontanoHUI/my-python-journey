# 写一个函数 factorial(n)，计算 n 的阶乘（0 的阶乘是 1）
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def factorial2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
