class A:
    def first(self, a):
        self.a = a
class B:
    def second(self, b):
        self.b = b
class C(A,B):
    def add(self):
        x = self.a + self.b
        print(x)

obj = C()
obj.add()
    
