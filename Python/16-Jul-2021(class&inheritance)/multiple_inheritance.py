class A:
    def __init__(self, a):
        self.a = a
class B:
    def __init__(self, b):
        self.b = b
class C(A,B):
    def add(self):
        x = A.a + B.b
        print(x)

obA = A(1)
oBb = B(2)
obj = C()
obj.add()
    
