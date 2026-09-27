# 列表去重，原有顺序
lst = [2, 3, 2, 5, 3, 6, 5]
new_lst = list(dict.fromkeys(lst))
print(new_lst)
# 输出：[2, 3, 5, 6]


def remove_duplicates(lst):
    new_list = []
    for x in lst:
        if x not in new_list:
            new_list.append(x)
    return new_list


lst = [2, 3, 2, 5, 3, 6, 5]
new_lst = remove_duplicates(lst)
print(new_lst)
# 输出：[2, 3, 5, 6]
