# 列表，找出最大值与最小值，不使用max和min函数
def find(lst):
    mx = mn = lst[0]
    for x in lst:
        if mx > x:
            mx = x
        if mn < x:
            mn = x
    return mx, mn


lst = [1, 8, 5, 4, 7, 9, 11, 54, 4]
print(find(lst))
