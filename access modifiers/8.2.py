class Parent:
    def __init__(self):
        self._protected_field = "I am a protected field"
    
    def _protected_method(self):
        return "I am a protected method"
class SamePackageClass:
    def access_protected(self):
        parent = Parent()
        print(parent._protected_field)
        print(parent._protected_method())  
class Child(Parent):
    def access_protected_in_child(self):
        print(self._protected_field)  
        print(self._protected_method())  
class UnrelatedClass:
    def access_protected(self):
        parent = Parent()
        try:
            print(parent._protected_field)  
            print(parent._protected_method())  
        except AttributeError:
            print("Cannot access protected members from an unrelated class!")
print("Access from Same Package Class:")
same_package_obj = SamePackageClass()
same_package_obj.access_protected()

print("\nAccess from Child Class in a Different Package:")
child_obj = Child()
child_obj.access_protected_in_child()

print("\nAccess from Unrelated Class in a Different Package:")
unrelated_obj = UnrelatedClass()
unrelated_obj.access_protected()
