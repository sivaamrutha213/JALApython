class AccessModifiers:
    def __init__(self, public_var):
        self.public_var = public_var
        print(f"Public constructor called with public_var: {self.public_var}")
    def _protected_init(self, protected_var):
        self._protected_var = protected_var
        print(f"Protected constructor called with _protected_var: {self._protected_var}")
    def __private_init(self, private_var):
        self.__private_var = private_var
        print(f"Private constructor called with __private_var: {self.__private_var}")
    def call_protected_constructor(self, protected_var):
        self._protected_init(protected_var)
    def call_private_constructor(self, private_var):
        self.__private_init(private_var)


class MainClass:
    def __init__(self):
        instance = AccessModifiers("PublicValue")
        instance.call_protected_constructor("ProtectedValue")
        instance.call_private_constructor("PrivateValue")
main_instance = MainClass()
