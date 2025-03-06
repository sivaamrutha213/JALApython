class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

def check_value(value):
    if value < 0:
        raise MyCustomException("Negative values are not allowed!")

def main():
    try:
        check_value(-10)
    except MyCustomException as e:
        print("Caught an exception:", e.message)

main()
