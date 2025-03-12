#pip install multimethod
from multimethod import multimethod
import math
class FiguraGeometrica:
    #Circulo
    @multimethod
    def area(self,radio:float):
        return math.pi*radio**2
    #Triangulo Rectangulo
    @multimethod
    def area(self, base:float, altura:float):
        return base * altura

    #Rectangulo
    @multimethod
    def area(self, base: float, altura: int):
        return (base * altura) / 2

    #Trapecio
    @multimethod
    def area(self, baseMayor:float, baseMenor:float, altura:float):
        return ((baseMayor + baseMenor) * altura) / 2

    #Pentagono
    @multimethod
    def area(self, longitud:int, apotema:float):
        return (5 / 2) * longitud * apotema

Figuras = FiguraGeometrica()
f1 = Figuras.area(1.0)
f2 = Figuras.area(2.0,3.0)
f3 = Figuras.area(3.0,7)
f4 = Figuras.area(2.0,3.0,5.0)
f5 = Figuras.area(3,5.0)

print("Circulo: ",f1)
print("Rectangulo: ", f2)
print("Triangulo rectangulo: ", f3)
print("Trapecio: ", f4)
print("Pentagono: ", f5)

