from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
 @abstractmethod
 def abstract_method(self):
  pass

 def non_abstract_method(self):
  print("This is a non-abstract method.")

class ConcreteClass(MyAbstractClass):
 def abstract_method(self):
  print("This is the implementation of the abstract method.")
  
 def call_abstract_method(self):
  self.abstract_method()

obj=ConcreteClass()
obj.call_abstract_method()
