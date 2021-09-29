class Animal:  
    def speak(self):  
        print("Animal Speaking")  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak() 
print('------------------------------')


class BaseClass:  
    def __init__(self):  
        self.a = 10  
class DerivedClass(Animal):  
    def __init__(self):
        BaseClass.__init__(self)
        self.b = 4  
    def add(self):
        print (self.a + self.b)   
obj = DerivedClass()  
obj.add()  