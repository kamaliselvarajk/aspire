class BaseClass:  
    def add(self, a, b):  
        return a + b   
class DerivedClass(BaseClass):  
    def add(self, a, b):            #Method Overriding, Runtime polymorphism
        return a - b  
obj = DerivedClass() 
obj1 = BaseClass()
print(obj.add(20, 10))
print(obj1.add(20, 10))
print('------------------------------')
 
class Main:  
     
    
    def add(self, a, b):  
        return a + b  
    def add(self, a, b, c=0):         #Method Overloading, Compile tile polymorphism, doesn't support
        print (a + b + c)      

obj = Main()  
obj.add(10,20)
obj.add(10,20,30)