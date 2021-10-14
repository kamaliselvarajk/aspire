class Baseclass(object):
    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

    def isEmployee(self):
        return False

class Derivedclass(Baseclass):
    def isEmployee(self):
        return True
issubclass(Derivedclass, Baseclass)
a = 'Kamali'
x = Baseclass(a)
print(x.getname(), x.isEmployee())

y = Derivedclass("Kamali")
print(y.getname(), y.isEmployee())
