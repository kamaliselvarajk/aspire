class Firstclass:
    def __init__(self, name, age):
        self.n = name
        self.a = age
        
x = Firstclass('Kamali', 21) #object for the class 'Firstclass'
y = Firstclass('Dharshini', 20)

print(x.n, ',', x.a)
print(y.n, ',', y.a)
print(dir(x))
print(type(x))

print("****************************************")

from datetime import date
class Firstclass:
    def __init__(self, firstname, lastname, dob):
        self.fname = firstname
        self.lname = lastname
        self.dob = dob
        
    def fullname(self):
        name = f"The fullname is {self.fname} {self.lname}"
        return name

    def age(self):
        current_year = date.today().year
        present_age = f'{self.fname} {self.lname} is {current_year-self.dob} years old'
        return present_age
        
x = Firstclass('Kamali', 'Selvaraj', 2000)
y = Firstclass('Dharshini', 'Selvaraj', 2001)

print(x.fullname())
print(y.fullname())

print(x.age())
print(y.age())

print("*********************************************")


