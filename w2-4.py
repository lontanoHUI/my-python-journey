# asyncio
import asyncio, time


async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} completed"


async def serial():
    out = []
    for n in ["A", "B", "C", "D", "E"]:
        out.append(await fetch(n, 0.5))
    return out


async def concurrent():
    return await asyncio.gather(
        fetch("A", 0.5),
        fetch("B", 0.5),
        fetch("C", 0.5),
        fetch("D", 0.5),
        fetch("E", 0.5),
    )


async def main():
    t = time.perf_counter()
    r1 = await serial()
    t1 = time.perf_counter() - t
    print(f"serial: {t1:.2f}")
    t = time.perf_counter()
    r2 = await concurrent()
    t2 = time.perf_counter() - t
    print(f"concurrent: {t2:.2f}")
    print(f"并发快了{t1/t2:.1f}倍")


asyncio.run(main())


async def bad():
    time.sleep(0.2)


async def good():
    await asyncio.sleep(0.2)


async def demo():
    t = time.perf_counter()
    await asyncio.gather(bad(), bad(), bad())
    print(f"用 time.sleep三个任务耗时:{time.perf_counter()-t:.2f}秒")

    t = time.perf_counter()
    await asyncio.gather(good(), good(), good())
    print(f"用 asyncio.sleep三个任务耗时:{time.perf_counter()-t:.2f}秒")
