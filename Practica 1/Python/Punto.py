import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return f"({self.x}, {self.y})"

    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return f"(r: {r}, θ: {math.degrees(theta)}°)"

    def __str__(self):
        return f"Punto: {self.coord_cartesianas()}"

# Ejemplo de uso
p = Punto(3, 4)
print(p)
print("Coordenadas polares:", p.coord_polares())
