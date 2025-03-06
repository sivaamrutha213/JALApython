class MultipleExceptionsExample:
    def __init__(self):
        self.handle_exceptions()

    def handle_exceptions(self):
        try:
            result = 10 / 0  
        except ZeroDivisionError:
            print("Caught a ZeroDivisionError: division by zero")
        
        try:
            result = int("not a number")  
        except ValueError:
            print("Caught a ValueError: invalid literal for int()")

        try:
            lst = [1, 2, 3]
            print(lst[5])  
        except IndexError:
            print("Caught an IndexError: list index out of range")

class Main:
    def __init__(self):
        instance = MultipleExceptionsExample()
main_instance = Main()
