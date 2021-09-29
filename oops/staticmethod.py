class BaseClass():                  
    a=10
    b=20

    @staticmethod
    def add():                  
        c=BaseClass.a + BaseClass.b
        print(c, 'hi') 
        print('hi')

class DerivedClass(BaseClass):  
    def bark(self):  
        print("dog barking") 
             
obj =  BaseClass()
obj.add() 
BaseClass.add() 
obj1 =  DerivedClass()
obj1.add()
print('------------------------------')

class Common:
    @staticmethod
    def show():
        print("Dept: IT")
        print("Clg Name: KNCET ")         

class Student(Common):
    def __init__(self):
        self.__rollno=1

    def display(self):
        print('RollNo: ', self.__rollno)
        Common.show()
class Faculty(Common):
    def __init__(self):
        self.__doj='02/01/2021'

    def display(self): 
        print('DOJ: ', self.__doj) 
        Common.show()

stu =  Student()
stu.display() 

fac = Faculty() 
fac.display()         