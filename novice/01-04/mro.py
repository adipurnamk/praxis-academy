class A:
    num = 4
    
class B(A):
    pass

class C(A):
    num = 5
    
class D(B,C):
    pass