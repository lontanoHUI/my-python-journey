def count_word(text):
    dic = {}
    for word in text.lower().split():
        dic[word] = dic.get(word, 0) + 1
    return dic


text = input("enter a text:")
print(count_word(text))
