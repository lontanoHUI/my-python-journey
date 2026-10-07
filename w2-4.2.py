import time
import asyncio


async def bad():
    time.sleep(0.2)  # time.sleep()是同步阻塞的，不让出控制权，实际上仍在排队执行


async def good():
    await asyncio.sleep(0.2)  # 让出控制权


async def demo():
    t = time.perf_counter()
    await asyncio.gather(bad(), bad(), bad())
    print(f"用 time.sleep三个任务耗时:{time.perf_counter()-t:.2f}秒")

    t = time.perf_counter()
    await asyncio.gather(good(), good(), good())
    print(f"用 asyncio.sleep三个任务耗时:{time.perf_counter()-t:.2f}秒")


async def may_fail(n):
    if n == 2:
        raise ValueError(f"任务{n}失败")
    return n


async def handle():
    results = await asyncio.gather(
        may_fail(1), may_fail(2), may_fail(3), return_exceptions=True
    )
    # 不加 return_exceptions=True 的话，任何一个任务抛异常，整个 gather 都会失败，
    # 其他任务的结果全丢。加上之后，异常会作为结果之一返回，可逐个判断
    # 这在「同时调 5 个 API，其中一个挂了」的场景里非常重要。
    print(results)


asyncio.run(handle())
asyncio.run(demo())
