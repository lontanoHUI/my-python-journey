#1
print("Hello,world!")
print("Hello, whh! Today is 2026-09-21!")

#2
name=input("please enter your name:")  # input拿到的是字符串， 输入的内容是字符串
print(f"hello,{name},welcome to python world!")

#3
num1=int(input("please enter a number:")) # 输入的内容是字符串，需要转换为整数
num2=int(input("please enter another number:"))
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}/{num2}={num1/num2}")

#4 输入一个整数，判断他是奇数还是偶数
num=int(input("please enter an integer:"))
if num%2==0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

#5 输入一个 0–100 的成绩，输出等级：90 以上 A，80 以上 B，70 以上 C，60 以上 D，否则 F
score=float(input("please enter your score:"))
if score>=90:
    print("A")
elif score>=80 and score<90:
    print("B")
elif score>=70 and score<80:
    print("C")
elif score>=60 and score<70:
    print("D")
else:
    print("F")

#6 输入一个年份，判断是不是闰年。（提示：能被 4 整除且不能被 100 整除，或者能被 400 整除）
year=int (input("please enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 7 for  o-100 的加和
sum=0
for i in range(101):
    sum=sum+i
print(f"0-100的加和为:{sum}")  

# 8 1-100所有的偶数打印
for i in range(1,101):
    if i%2==0:
        print(i)


#9 打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}"+"\t",end="")
    print()  # 换行
