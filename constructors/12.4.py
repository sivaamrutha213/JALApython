class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Main:
    def __init__(self):
        person_instance = Person("Alice", 30)
        person_instance.display()
main_instance = Main()
