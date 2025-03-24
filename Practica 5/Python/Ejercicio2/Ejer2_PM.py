import math

def promedio(v):
    s = 0
    for i in range (len(v)):
        s += v[i]
    return s / len(v)

def desviacion(v):
    s = 0
    for i in range (len(v)):
        s += ((v[i] - promedio(v)) ** 2)
    s /= len(v) - 1
    return math.sqrt(s)


v = list(map(float, input().split()))
p = promedio(v)
d = desviacion(v)
print(f"El promedio es {p}")
print(f"La desviacion estandard es {d}")




