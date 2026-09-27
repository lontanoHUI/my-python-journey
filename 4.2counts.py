# 输入一段英文句子，统计有多少个单词,空格切分
def count_words(s):
    return len(s.split())


s = input("请输入一段英文句子：")
word_count = count_words(s)
print(f"句子中有 {word_count} 个单词。")
