#1.1函数
def add(a,b=0):
    return a+b

#1.2调用函数
print(add(5))  # 输出: 5
print(add(5,3))  # 输出: 8
print(add(b=3,a=5))  # 输出: 8, 使用关键字参数调用函数
#def 定义，return 返回结果，没有 return 就返回 None。默认参数必须放在后面。


#2.1异常处理
try:
    n=input("please enter a number:")
except ValueError:
    print("Invalid input. Please enter a valid number.")
finally:
    print("This block will always execute.")

#2.2 实际写法：把可能出错的输入包起来
raw = input("请输入一个数字：")
try:
    n = int(raw)
    print(f"你输入了 {n}")
except ValueError:
    print("这不是数字，请重输")


#3 文件读写，必须加encoding="utf-8" 否则中文会乱码
#3.1 写文件
with open("a.txt","w",encoding="utf-8") as f:
    f.write("Hello, world!\n")
    f.write("你好，世界！\n")
    f.write("today is 2026-09-26\n")

#3.2 读文件  模式说明："r" 读（默认）、"w" 写（会清空原内容）
# "a" 追加、"r" + encoding 是读文本文件的标准写法。
# 忘记 encoding="utf-8" 是中文乱码的头号原因。

#按行读
with open("a.txt",encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() 去掉换行符
#读整个文件
with open("a.txt",encoding="utf-8") as f:
    lines=f.readlines()  # 读取所有行，返回一个列表
    print(len(lines))  # 输出行数

#"a" 追加
with open("a.txt","a",encoding="utf-8") as f:
    f.write("追加一行内容\n")



#类与对象
class Student:
    def __init__(self,name,score):#构造方法
        self.name=name
        self.score=score

    def is_pass(self):#实例方法
        return self.score>=60
    
    def __str__(self):#决定print出来的样子
        return f"Student(self.name,self.score)"
    
s=Student("zhangsan",88)
print(s)
print(s.is_pass())
print(Student("lisi",54).is_pass())



#继承
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
g1=Dog("baby")
print(g1.speak())
c1=Cat("whiskers")
print(c1.speak())