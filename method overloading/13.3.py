class ExampleClass:
    def method(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            self.method_int(a, b)
        elif isinstance(a, str) and isinstance(b, str):
            self.method_str(a, b)

    def method_int(self, a, b):
        print("This is the integer method with parameters:", a, b)

    def method_str(self, a, b):
        print("This is the string method with parameters:", a, b)

class Main:
    def __init__(self):
        instance = ExampleClass()
        
        instance.method(5, 10)
        instance.method("Hello", "Ammu")  


main_instance = Main()
