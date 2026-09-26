import csv



# 写入（w模式：清空文件，重新写，会覆盖原来所有内容！）
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])  # 表头
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])

# 读取csv
with open("scores.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    for row in reader:
        print(row[0], row[1])


#5常用标准库
import os, json, random, datetime
from pathlib import Path
 
print(Path.cwd())                        # 当前目录
print(os.listdir("."))                   # 目录下有哪些文件
print(random.randint(1, 100))            # 随机整数
print(datetime.date.today())             # 今天日期
print(json.dumps({"a": 1}))              # 字典转 JSON 字符串
print(json.loads('{"a": 1}'))            # JSON 字符串转字典