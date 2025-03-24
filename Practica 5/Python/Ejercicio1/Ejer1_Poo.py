import math
class Algebra:
    def __init__(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return (self.__b ** 2) - 4 * self.__a * self.__c
    def getRaiz1(self):
        r1 = (-self.__b + math.sqrt(self.getDiscriminante())) / (2 * self.__a)
        return r1
    def getRaiz2(self):
        r2 = (-self.__b - math.sqrt(self.getDiscriminante())) / (2 * self.__a)
        return r2

    def __str__(self):
        disc = self.getDiscriminante()
        if disc > 0:
            return f"La ecuación tiene dos raíces {self.getRaiz1():.6f} y {self.getRaiz2():.5f}"
        if disc == 0:
            return f"La ecuación tiene una raíz {self.getRaiz1()}"
        else:
            return "La ecuacion no tiene raıces reales"

a, b, c = map(float, input("Ingrese a, b, c: ").split())
ec = Algebra(a,b,c)
print(ec)








