# 回文串判断
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]


input_string = input("请输入一个字符串：")
if is_palindrome(input_string):
    print(f'"{input_string}" 是回文串。')
else:
    print(f'"{input_string}" 不是回文串。')
