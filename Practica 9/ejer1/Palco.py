#Palco
from Boleto import Boleto
class Palco(Boleto):
    def calcular_precio(self) -> None:
        self.establecer_precio(100.00)