class Calculator:
    def add(self, a, b=None):
        if b is not None:
            return a + b
        return a

class Main:
    def __init__(self):
        calculator_instance = Calculator()
        
        result_one_argument = calculator_instance.add(5)
        print("Result with one argument:", result_one_argument)
        
        result_two_arguments = calculator_instance.add(5, 10)
        print("Result with two arguments:", result_two_arguments)

main_instance = Main()
