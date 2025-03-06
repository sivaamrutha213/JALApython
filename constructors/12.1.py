class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is not None and arg2 is not None:
            print(f"Two-argument constructor called with arg1: {arg1} and arg2: {arg2}")
        elif arg1 is not None:
            print(f"One-argument constructor called with arg1: {arg1}")
        else:
            print("Default constructor called")

class MainClass:
    def __init__(self):
        
        instance1 = MyClass()
        instance2 = MyClass(arg1="Hello")
        instance3 = MyClass(arg1="Hello", arg2="World")
main_instance = MainClass()
