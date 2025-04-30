#Platea
from Boleto import Boleto
class Platea(Boleto):
    def __init__(self, numero: int, dias_anticipacion: int):
        self._dias_anticipacion = dias_anticipacion
        super().__init__(numero)

    def calcular_precio(self) -> None:
        if self._dias_anticipacion >= 10:
            self.establecer_precio(50.00)
        else:
            self.establecer_precio(60.00)