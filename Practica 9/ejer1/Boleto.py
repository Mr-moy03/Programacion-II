#Boleto
from abc import ABC, abstractmethod
class Boleto(ABC):
    def __init__(self, numero: int):
        self._numero = numero
        self._precio = 0.0
        self.calcular_precio()

    def obtener_numero(self) -> int:
        return self._numero

    def establecer_numero(self, numero: int) -> None:
        self._numero = numero

    def obtener_precio(self) -> float:
        return self._precio

    def establecer_precio(self, precio: float) -> None:
        self._precio = precio

    @abstractmethod
    def calcular_precio(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Número: {self.obtener_numero()}, Precio: {self.obtener_precio():.1f}"