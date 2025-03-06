class MyClass:
 static_variable="This is a static var"

obj=MyClass()
obj.static_variable="Modified static var"
print(MyClass.static_variable)
print(obj.static_variable)
