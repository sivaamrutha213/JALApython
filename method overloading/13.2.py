class MethodOverloading:
    def display(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                print("Method with one integer parameter:", args[0])
            elif isinstance(args[0], str):
                print("Method with one string parameter:", args[0])
        elif len(args) == 2:
            print("Method with two parameters:", args[0], "and", args[1])

class Main:
    def __init__(self):
        obj = MethodOverloading()
        
        obj.display(10)
        obj.display("Hello")
        obj.display("Hello", 10)

main_instance = Main()
