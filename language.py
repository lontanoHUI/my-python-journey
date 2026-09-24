from collections import Counter
name = "whh" #str
age=22  #int
height=1.70  #float
is_student=True  #bool

print(type(age))
print(type(height))
print(type(is_student))
print(f"我叫{name},今年{age}岁，身高{height}米，是否是学生：{is_student}")



#字符串常用操作
print("-----------字符串常用操作-----------")
s="hello,python!"
print(len(s))
print(s[0],s[-1]) # 输出第一个和最后一个字符
print(s[0:5]) # 输出前五个字符,切片
print(s.upper()) # 转换为大写
print(s.lower()) # 转换为小写
print(s.replace("python","world")) # 替换字符串
print("a,b,c".split(",")) # 分割字符串,a,b,c拆分
print("  hi  ".strip())# 去掉字符串两端的空格
print("py" in s) # 判断字符串中是否包含子串



# 3 列表（有序，可变）
print("-----------列表常用操作-----------")

nums=[3,-2,2,7,5]
nums.append(9) # 在列表末尾添加元素
nums.sort() # 对列表进行排序
print(nums[0],nums[-1])
print(nums[1:4]) # 切片
print(len(nums),sum(nums),max(nums)) # 列表长度,求和，最大值
print(9 in nums)
nums.remove(2) # 删除元素,按值删除



#4 字典（键值对，统计方便）
print("-----------字典常用操作-----------")
student={"name":"whh","age":22,"height":1.70}
print(student["name"]) # 访问字典中的值
student["age"]=23 # 修改字典中的值
print(student.get("grade","N/A")) # 获取字典中的值，如果键不存在则返回默认值
student["grade"]="A" # 添加新的键值对
print(student) # 输出整个字典
print("name" in student) # 判断字典中是否存在某个键
for k,v in student.items(): # 遍历字典中的键值对
    print(k,v)

#统计次数
print("-----------统计次数-----------")
count1={}
for ch in "aaabbtttyhp":
    count1[ch]=count1.get(ch,0)+1
print(count1)

#Counter类可以用来统计元素出现的次数
counts = Counter("aaabbtttyhp")
print(counts)

# 5 条件判断（注意冒号和缩进）
print("-----------条件判断-----------")

score=85
if score>=90:
    print("A")
elif score>=80 and score<90: # 是 elif 不是 else if
    print("B")
else:
    print("C")


#  6 循环
print("-----------循环(for and while)-----------")
for i in range(1,6):
    print(i) # 输出1到5

for item in ["apple","banana","cherry"]:
    print(item) # 遍历列表中的元素

for k,v in student.items():
    print(k,v) # 遍历字典中的键值对

n=0
while n<5:
    print(n)
    n+=1 # 注意缩进，避免死循环,python没有自增运算符++，需要使用+=1

# 7 输入与输出
print("-----------输入与输出-----------")
name=input("please enter your name:")  # input拿到的是字符串， 输入的内容是字符串
age=int(input("please enter your age:")) # 输入的内容是字符串，需要转换为整数
print(f"Hello,{name},you are {age} years old.")

#  8 列表推导式
print("-----------列表推导式-----------")
squares=[i*i for i in range(1,6)] # 生成1到5的平方数列表
evens=[i for i in range(10) if i%2==0] # 生成1到10的偶数列表
words={w:len(w) for w in ["hello","world","python"]} # 字典推导式，生成单词长度的字典，键值对，一一对应
# 列表推导式（方括号）→ 得到列表
lengths = [len(w) for w in ["hello", "world", "python"]]
# [5, 5, 6]
