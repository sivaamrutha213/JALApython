class MyClass:
    def __init__(self, name, age):
        self.name = name   
        self.age = age     
    
    def greet(self):        
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def set_name(self, name):   
        self.name = name
    
    def get_name(self):        
        return self.name
def main():
    person = MyClass("John", 30)
    print(person.name)
    person.greet()  
    person.set_name("Alice")
    print(person.get_name())  
    
if __name__ == "__main__":
    main()
