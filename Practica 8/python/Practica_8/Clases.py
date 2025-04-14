class A:
    def __init__(self,x,z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1

class B:
    def __init__(self,y,z):
        self.y = y
        self.z = z
    def incrementaYZ(self):
        self.y += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1

class C(A,B):
    def __init__(self,x,y,z):
        A.__init__(self,x,z)
        B.__init__(self,y,z)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1

    def __str__(self):
        return f"x:{self.x} , y:{self.y} , z:{self.z}"


num = C(5,10,25)
num.incrementaXYZ()
print(num)

num.incrementaZ()
print(num)
num.incrementaYZ()
print(num)


num.incrementaZ()
print(num)
num.incrementaXZ()
print(num)

