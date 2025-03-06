class A:
    def __init__(self):
        self.__private_field = 10

    def __private_method(self):
        print("Private method in Class A")

    def public_method(self):
        print(f"Private field value from public method: {self.__private_field}")
        self.__private_method()

class B(A):
    def __init__(self):
        super().__init__()

    def try_access_private(self):
        try:
            print(f"Accessing private field from subclass: {self.__private_field}")
        except AttributeError:
            print("Cannot access private field from subclass.")
        
        try:
            self.__private_method()
        except AttributeError:
            print("Cannot access private method from subclass.")

class Main:
    def main(self):
        a = A()
        a.public_method()

        b = B()
        b.try_access_private()

if __name__ == "__main__":
    m = Main()
    m.main()
