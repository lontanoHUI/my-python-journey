class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "Student: %s | Score: %d" % (self.name, self.score)

    def is_pass(self):
        if self.score > 60:
            return True


s1 = Student("whh", 80)
print(s1)
is_pass = s1.is_pass()
print(is_pass)


# 写一个类 Counter，有 inc(n=1)、reset() 两个方法，以及一个只读属性 value
class Counter:
    def __init__(self):
        self._value = 0

    def inc(self, n=1):
        self._value += n

    def reset(self):
        self._value = 0

    @property
    def value(self):
        return self._value
