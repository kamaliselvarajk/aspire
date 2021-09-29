class Grandfather:  
	def fun(self):  
         print("Dancer")   
class Father(Grandfather):  
	def fun(self):  		#Method overriding
	    print("Singer") 
class Son(Father):  
	def fun(self):  
         print("Both dancer and singer") 

obj = Son()
obj.fun() 

obj1 = Father()
obj1.fun()
print('------------------------------')

class A: 
    def __init__(self):  
        self.a = 10

    def fun(self):  
         print("Dancer")   
class B(A):  
    def __init__(self):  
        self.b = 20 
        A.__init__(self)

    def fun(self):  		#Method overriding
	         print("Singer") 
class C(B): 
     def __init__(self):  
        self.c = 30 
        B.__init__(self)

     def fun(self):
         d = self.a  + self.b  + self.c
         print(d)
         print("Both dancer and singer")

obj = C() 
obj.fun()         