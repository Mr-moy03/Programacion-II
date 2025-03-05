class Cola:
    def __init__(self, n):
        self.arreglo = [None] * n
        self.inicio = 0
        self.fin = -1
        self.n = n
        self.size = 0

    def insert(self, e):
        if self.isFull():
            print("Cola llena")
        self.fin = (self.fin + 1) % self.n
        self.arreglo[self.fin] = e
        self.size += 1

    def remove(self):
        if self.isEmpty():
            print("Cola vacía")
        elemento = self.arreglo[self.inicio]
        self.inicio = (self.inicio + 1) % self.n
        self.size -= 1
        return elemento

    def peek(self):
        if self.isEmpty():
            print("Cola vacía")
        return self.arreglo[self.inicio]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.n

    def size(self):
        return self.size

cola = Cola(10)
cola.insert(10)
cola.insert(20)
cola.insert(30)

print(cola.peek())
print("remove() =", cola.remove())
print(cola.peek())
print("remove() =", cola.remove())
print("remove() =", cola.remove())
print("remove() =", cola.remove())