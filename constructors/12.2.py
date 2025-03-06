class SuperClass:
    def __init__(self, arg1=None):
        if arg1 is not None:
            print(f"SuperClass argument constructor called with arg1: {arg1}")
        else:
            print("SuperClass default constructor called")

class SubClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        if arg2 is not None:
            super().__init__(arg1)
            print(f"SubClass two-argument constructor called with arg1: {arg1} and arg2: {arg2}")
        elif arg1 is not None:
            super().__init__(arg1)
            print(f"SubClass one-argument constructor called with arg1: {arg1}")
        else:
            super().__init__()
            print("SubClass default constructor called")
instance1 = SubClass()
instance2 = SubClass(arg1="Hello")
instance3 = SubClass(arg1="Hello", arg2="World")
