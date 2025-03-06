class MyClass:
 static_variable="This is a static variable"

 @classmethod
 def change_static_variable(cls, new_value):
  cls.static_variable=new_value

MyClass.change_static_variable("Modified static variable")

print(MyClass.static_variable)
