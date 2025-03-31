import math


class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # Sobrecarga de operadores
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, scalar):
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def longitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normal(self):
        length = self.longitud()
        if length == 0:
            return Vector3D(0, 0, 0)
        return self / length

    def producto_escalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def producto_vectorial(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,self.z * other.x - self.x * other.z,self.x * other.y - self.y * other.x
)

    def es_perpendicular(self, other, tol=1e-10):
        return abs(self.producto_escalar(other)) < tol

    def proyeccion(self, other):
        escalar = self.producto_escalar(other)
        longitud_other = other.longitud()
        if longitud_other == 0:
            return Vector3D(0, 0, 0)
        factor = escalar / (longitud_other ** 2)
        return other * factor

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# main
a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)

print("Operaciones básicas:")
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"2 * a = {2 * a}")
print(f"a / 2 = {a / 2}")

print("\nPropiedades del vector:")
print(f"Longitud de a: {a.longitud()}")
print(f"Vector normalizado de a: {a.normal()}")

print("\nProductos:")
print(f"Producto escalar a·b: {a.producto_escalar(b)}")
print(f"Producto vectorial a×b: {a.producto_vectorial(b)}")

print("\nRelaciones:")
print(f"¿a y b son perpendiculares? {a.es_perpendicular(b)}")

print("\nProyección:")
print(f"Proyección de a sobre b: {a.proyeccion(b)}")