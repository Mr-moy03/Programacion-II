from multimethod import multimethod
import math
class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x; self.y = y; self.z = z
    # Sobrecarga de operadores
    def __add__(self, other):
        return AlgebraVectorial(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return AlgebraVectorial(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):  # Producto punto
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __mod__(self, other):  # Producto cruz
        nuevo_x = self.y * other.z - self.z * other.y
        nuevo_y = self.z * other.x - self.x * other.z
        nuevo_z = self.x * other.y - self.y * other.x
        return AlgebraVectorial(nuevo_x, nuevo_y, nuevo_z)
    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    @multimethod
    def perpendicular(self, other: 'AlgebraVectorial') -> bool:
        return abs(self * other) < 1e-10
    @perpendicular.register
    def _(self, other: 'AlgebraVectorial', metodo: int) -> bool:
        "Metodos"
        if metodo == 1:  # |a + b| = |a - b|
            suma = self + other; resta = self - other
            return abs(suma.norma() - resta.norma()) < 1e-10
        elif metodo == 2:  # |a - b| = |b - a|
            resta1 = self - other;resta2 = other - self
            return abs(resta1.norma() - resta2.norma()) < 1e-10
        elif metodo == 3:  # a · b = 0
            return abs(self * other) < 1e-10
        elif metodo == 4:  # |a + b|² = |a|² + |b|²
            suma = self + other
            return abs(suma.norma() ** 2 - (self.norma() ** 2 + other.norma() ** 2)) < 1e-10
        else:
            return False

    @multimethod
    def paralelo(self, other: 'AlgebraVectorial') -> bool:
        return (self % other).norma() < 1e-10
    @paralelo.register
    def _(self, other: 'AlgebraVectorial', metodo: int) -> bool:
        """métodos"""
        if metodo == 1:  # a = r*b
            if other.x == 0 or other.y == 0 or other.z == 0:
                return False
            r = self.x / other.x
            return (abs(self.y / other.y - r) < 1e-10) and (abs(self.z / other.z - r) < 1e-10)
        elif metodo == 2:  # a × b = 0
            return (self % other).norma() < 1e-10
        else:
            return "Método no válido para paralelismo"

    def proyeccion(self, other):
        producto_punto = self * other; norma_b_cuadrado = other.norma() ** 2
        if norma_b_cuadrado == 0:
            return AlgebraVectorial(0, 0, 0)
        factor = producto_punto / norma_b_cuadrado
        return AlgebraVectorial(other.x * factor, other.y * factor, other.z * factor)

    def componente(self, other):
        producto_punto = self * other; norma_b = other.norma()
        if norma_b == 0:
            return 0
        return producto_punto / norma_b
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Main
v1 = AlgebraVectorial(1, 0, 0)
v2 = AlgebraVectorial(0, 1, 0)
v3 = AlgebraVectorial(2, 0, 0)

print("Vectores:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")

print("\nPruebas de perpendicularidad:")
print(f"v1 perpendicular a v2 (Default): {v1.perpendicular(v2)}")
print(f"v1 perpendicular a v2 (método 1): {v1.perpendicular(v2, 1)}")
print(f"v1 perpendicular a v2 (método 2): {v1.perpendicular(v2, 2)}")
print(f"v1 perpendicular a v2 (método 3): {v1.perpendicular(v2, 3)}")
print(f"v1 perpendicular a v2 (método 4): {v1.perpendicular(v2, 4)}")

print("\nPruebas de paralelismo:")
print(f"v1 paralelo a v3 (método por defecto): {v1.paralelo(v3)}")
print(f"v1 paralelo a v3 (método 1): {v1.paralelo(v3, 1)}")
print(f"v1 paralelo a v3 (método 2): {v1.paralelo(v3, 2)}")

print("\nProyección de v1 sobre v2:")
print(v1.proyeccion(v2))

print("\nComponente de v1 en v2:")
print(v1.componente(v2))