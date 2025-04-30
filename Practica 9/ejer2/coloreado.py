from abc import ABC, abstractmethod
import math
import random
#Interfaz
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass
#clase abstracta
class Figura(ABC):
    def __init__(self,color):
        self.__color = color

    def setColor(self,color) -> None:
        self.__color = color

    def getColor(self) -> str:
        return self.__color

    def __str__(self):
        return f"{self.getColor()}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura,Coloreado):
    def __init__(self,color,lado):
        self.__lado = lado
        super().__init__(color)

    def getLado(self):
        return self.__lado

    def setLado(self,lado):
        self.__lado = lado


    def area(self):
        return self.__lado ** 2


    def perimetro(self):
        return 4 * self.__lado

    def __str__(self):
        return f"Cuadrado:[Lados:{self.getLado()},color:{self.getColor()}]"

    def comoColorear(self) -> str:
        return f"Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self,color,radio):
        self.__radio = radio
        super().__init__(color)

    def getRadio(self):
        return self.__radio

    def setRadio(self,radio):
        self.__radio = radio

    def area(self) -> float:
        return math.pi * (self.__radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.__radio

    def __str__(self):
        return f"Circulo:[Radio:{self.getRadio()},color:{self.getColor()}]"


# main
colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco"]
figuras = []

for _ in range(5):
    tipo = random.randint(1, 2)
    color = random.choice(colores)

    if tipo == 1:
        lado = random.uniform(1.0, 10.0)
        figuras.append(Cuadrado(color, lado))
    else:
        radio = random.uniform(1.0, 10.0)
        figuras.append(Circulo(color, radio))


for fig in figuras:
    print(fig)
    print(f"area: {fig.area()}")
    print(f"perimetro: {fig.perimetro()}")
    if isinstance(fig, Coloreado):
        print(fig.comoColorear())
    print("\n")