#Galeria
from Platea import Platea
class Galeria(Platea):
    def __init__(self, numero: int, dias_anticipacion: int):
        super().__init__(numero,dias_anticipacion)

    def calcular_precio(self) -> None:
        if self._dias_anticipacion >= 10:
            self.establecer_precio(25.00)
        else:
            self.establecer_precio(30.00)

    def __str__(self) -> str:
        return f"Número: {self.obtener_numero()}, Precio: {self.obtener_precio():.1f}"
