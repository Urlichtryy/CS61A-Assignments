class A:
    x,y=0,0
    def __init__(self):
        return

class B(A):
    def __init__(self):
        return

class C(A):
    def __init__(self):
        return

print(A.x,B.x,C.x)
obj = C()
obj.y = 1
A.y = obj.y
print(A.y, B.y, C.y, obj.y)