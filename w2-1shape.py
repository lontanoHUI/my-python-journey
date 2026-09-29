class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return f"{self.name}(shape={self.area():.2f})"

    def __repr__(self):
        return f"Shape(name={self.name!r})"  #!r 表示对 self.name 使用 repr() 进行格式化，即自动为字符串加上引号。

    def describe(self):
        return f"This is a {self.name}"


class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self.r = r

    def area(self):
        return 3.1415926 * self.r**2

    def __len__(self):
        return int(self.r)

    def describe(self):
        return super().describe()


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__("Rectangle")
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Triangle(Shape):
    def __init__(self, w, h):
        super().__init__("Triangle")
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h * 0.5


for s in [Circle(4), Rectangle(3, 4), Triangle(3, 4)]:
    print(s)

print(repr(Rectangle(4, 6)))

print(len(Circle(4)))

print(Circle(4).describe())


def total_area(shapes):
    return sum(s.area() for s in shapes)


print("total area :", total_area([Circle(4), Rectangle(3, 4), Triangle(3, 4)]))
