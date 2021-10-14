class Father():
    def fun1(self):
        print('Father')

    def fun2(self):
         print('Singer')     

class Mother():
    def fun2(self):
        print('Mother')   

class Child(Mother, Father):
    def fun(self):

        self.fun2()
        print('Both Father Mother')   

obj =  Child()   
obj.fun1()
obj.fun2()
obj.fun()