class ExceptionExample:
    def raise_exception(self):
        raise Exception("This is an intentionally raised exception")

class Main:
    def __init__(self):
        instance = ExceptionExample()
        instance.raise_exception()

main_instance = Main()
