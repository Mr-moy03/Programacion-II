import math
class Estadistica():
    def __init__(self,v):
        self.vector = v

    def promedio(self):
        s = 0
        for i in range(len(self.vector)):
            s += self.vector[i]
        return s / len(self.vector)

    def desviacion(self):
        p = self.promedio()
        s = 0
        for i in range(len(self.vector)):
            s += ((self.vector[i] - p) ** 2)
        s /= len(self.vector) - 1
        return math.sqrt(s)
    def __str__(self):
        return f"El promedio es {self.promedio():.2f}\nLa desviación estándar es {self.desviacion():.5f}"



v = list(map(float, input().split()))
est = Estadistica(v)
print(est)
