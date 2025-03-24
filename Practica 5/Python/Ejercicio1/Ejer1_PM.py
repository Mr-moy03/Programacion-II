import math

def discriminante(a,b,c):
    return (b ** 2) - 4 * a * c
def raiz1(a,b,c):
    r1 = (-b + math.sqrt(discriminante(a,b,c))) / (2 * a)
    return r1
def raiz2(a,b,c):
    r2 = (-b - math.sqrt(discriminante(a,b,c))) / (2 * a)
    return r2

def resolver(a,b,c):
    if discriminante(a, b, c) > 0:
        return f"La ecuación tiene dos raíces {raiz1(a, b, c)} y { raiz2(a, b, c)}"
    if discriminante(a, b, c) == 0:
        return f"La ecuación tiene una raíz {raiz1(a, b, c)}"
    else:
        return "La ecuacion no tiene raıces reales"

a, b, c = map(float, input("Ingrese a, b, c: ").split())
print(resolver(a,b,c))








