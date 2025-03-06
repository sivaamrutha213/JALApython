class ClassOne:
    def _init_(self, value):
        self.value = value

    def display_value(self):
        return f"ClassOne Value: {self.value}"


class ClassTwo:
    def _init_(self, value):
        self.value = value

    def display_value(self):
        return f"ClassTwo Value: {self.value}"


if _name_ == "__main__":
    obj1 = ClassOne(10)
    obj2 = ClassTwo(20)

    print(obj1.display_value())
    print(obj2.display_value())
