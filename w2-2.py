import time
from functools import wraps


def greet(name):
    return f"hello {name}"


f = greet
print(f("hh"))
print(greet.__name__)


def make_counter():
    count = 0

    def inc():
        nonlocal count  # 修改外层变量时需要加nonlocal
        count += 1
        return count

    return inc


c = make_counter()
print(c(), c(), c())


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        cost = time.perf_counter() - start
        print(f"{func.__name__} cost{cost*1000:.2f}ms")
        return res

    return wrapper


@timer
def slow_add(n):
    time.sleep(0.15)
    return sum(range(n))


print("result:", slow_add(100))
print("name:", slow_add.__name__)


# 写一个retry装饰器，被装饰的函数如果抛出异常给，就自动重试最多三次，每次打印第N次重试。
def retry(times=3, delay=0.5):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_err = e
                    print(
                        f"[{func.__name__}] 第 {attempt} 次失败：{type(e).__name__}: {e}"
                    )
                    if attempt < times:
                        time.sleep(delay)
            raise last_err  # 抛出最后一次的真实异常，别覆盖它

        return wrapper

    return deco


@retry()
def add(a, b):

    print("正在执行 add 函数...")
    # 模拟前几次执行抛出异常
    if not hasattr(add, "count"):
        add.count = 0
    add.count += 1

    if add.count < 3:
        raise ValueError("模拟网络请求失败")

    return a + b


# 测试运行
print("最终结果:", add(1, 2))


# 写一个log装饰器，每次调用函数时打印条用函数名，参数是...
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数:{func.__name__},参数是:{args},{kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log
def test(a, b):
    return a + b


print(test(1, 2))
# 测试运行
print("最终结果:", test(1, 2))
