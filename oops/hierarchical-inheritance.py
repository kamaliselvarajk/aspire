class Animal:  
    def sound(self):  
        print("Animal Sound")    
class Dog(Animal):  
	def dogsound(self):  
	    print("dog barking") 
class Cat(Animal):  
	def catsound(self):  
	    print("cat meow") 
class Cow(Animal):  
	def cowsound(self):  
	    print("cow maa")

cow = Cow()
cow.sound()
cow.cowsound()  

cat = Cat()
cat.sound()
cat.catsound() 

dog = Dog()
dog.sound()
dog.dogsound() 

cow = Cow()
cow.sound()
cow.cowsound() 
print('------------------------------')

class Common:
    def __init__(self):
        self.__name='name'              #Abstraction __ is used to hide the varibale from user
        self.__gender='gender'

    def show(self):
        print("Name: ", self.__name)
        print("Gender: ", self.__gender)   
class Employee(Common):
    def __init__(self):
        self.__id=1
        Common.__init__(self)

    def display(self):
        print('Id: ', self.__id)
        self.show()
class Manager(Common):
    def __init__(self):
        self.__domain='Python'
        Common.__init__(self)

    def display(self):        
        self.show()
        print('Domain: ', self.__domain) 

emp =  Employee()
emp.display() 

man = Manager() 
man.display() 
               