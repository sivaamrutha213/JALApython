class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def raise_custom_exception():
    raise CustomException("This is a custom exception message.")

def main():
    raise_custom_exception()
main()
