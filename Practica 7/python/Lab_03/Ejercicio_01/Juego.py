import random
class Juego:
    def __init__(self,numeroDeVidas,record):
        self.__numeroDeVidas = numeroDeVidas
        self.__record = record
    def getnumeroDeVidas(self):
        return self.__numeroDeVidas
    def setnumeroDeVidas(self,numeroDeVidas):
        self.__numeroDeVidas = numeroDeVidas

    def getrecord(self):
        return self.__record
    def setrecord(self,record):
        self.__record = record

    def reiniciaPartida(self):
        self.setnumeroDeVidas(self.getnumeroDeVidas())
        self.setrecord(0)

    def actualizaRecord(self):
        self.setrecord(self.getrecord() + 10)

    def quitaVida(self):
        if (self.getnumeroDeVidas() > 1):
            self.setnumeroDeVidas(self.getnumeroDeVidas()-1)
            return True
        return False

class JuegoAdivinaNumero(Juego):
    def __init__(self,numeroDeVidas,record=0):
        super().__init__(numeroDeVidas,record)
        self.__numeroAAdivinar = random.randint(0,10)
    def getnumeroAAdivinar(self):
        return self.__numeroAAdivinar
    def setnumeroAAdivinar(self,numeroAAdivinar):
        self.__numeroAAdivinar = numeroAAdivinar

    def juega(self):
        super().reiniciaPartida()
        print("__AdivinaAdivinador__")
        print("VIDAS: ", self.getnumeroDeVidas())
        while (self.getnumeroDeVidas() > -1):
            print("Ingresa tu numero: ")
            numeroUsuario = int(input())
            if (numeroUsuario == self.getnumeroAAdivinar):
                print(f"Acertaste, el nuemro era {self.getnumeroAAdivinar()}")
                super().actualizaRecord()
                print("Record: ",self.getrecord())
                print("Vidas: ",self.getnumeroDeVidas())
                if (self.getnumeroDeVidas() > 0):
                    print("Siguiente Numero a adivinar ???");
                    self.setnumeroAAdivinar(random.randint(0,10))
                    continue
                return
            else:
                if (not super().quitaVida()):
                    print("GAME OVER")
                    print("Te quedastes sin vidas ")
                    return

                if (numeroUsuario > self.getnumeroAAdivinar()):
                    print("El numero a adivinar es menor");
                    print("_________________________________")

                else :
                    print("El numero a adivinar es mayor");
                    print("_________________________________")

                print("Vidas Restantes: ", self.getnumeroDeVidas())


game1 = JuegoAdivinaNumero(10)
game1.juega()
