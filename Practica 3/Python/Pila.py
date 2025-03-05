class Pila:
    def __init__(self, n):
        self.arreglo = [None] * n
        self.top = -1
        self.n = n

    def push(self, e):
        if self.isFull():
            print("Pila llena")
        self.top += 1
        self.arreglo[self.top] = e

    def pop(self):
        if self.isEmpty():
            print("Pila vacía")
        elemento = self.arreglo[self.top]
        self.top -= 1
        return elemento

    def peek(self):
        if self.isEmpty():
            print("Pila vacía")
        return self.arreglo[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

pila = Pila(10)  # Crea una pila de tamaño 10
pila.push(10)
pila.push(20)
pila.push(30)
print(pila.peek())  # Muestra el elemento en el tope (30)
print("pop() =", pila.pop())  # Elimina y muestra el tope (30)
print(pila.peek())  # Muestra el nuevo tope (20)
print("pop() =", pila.pop())  # Elimina y muestra el tope (20)
print("pop() =", pila.pop())  # Elimina y muestra el tope (10)