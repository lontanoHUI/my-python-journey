import random

num = random.randint(1, 101)

count = 0
while True:
    count += 1
    n = int(input("please enter a number:"))
    if n < num:
        print("too small")
    elif n > num:
        print("too big")
    else:
        print((f"you win,you guess {count} times"))
        break
