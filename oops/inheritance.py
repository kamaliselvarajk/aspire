class BaseClass():                  #Encapsulation, combines the data and method together within in a class
    a=10
    b=20

    def add(self):                  
        c=self.a + self.b
        return c

    def sub(self):
        c=self.a - self.b 
        print(c)

    def mul(self):
        c=self.a * self.b 
        return c

    def div(self):
        c=self.a / self.b 
        return c


obj =  BaseClass()
print(obj.add())
(obj.sub())
print(obj.mul())
print(obj.div())
