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

    def validarNumero(self,numero):
        if (numero < 0 or numero > 10):
            return True
        return False


    def juega(self):
        super().reiniciaPartida()
        print("__AdivinaAdivinador__")
        print("VIDAS: ", self.getnumeroDeVidas())
        while (self.getnumeroDeVidas() > -1):
            print("Ingresa tu numero: ")
            numeroUsuario = int(input())
            while (self.validarNumero(numeroUsuario)):
                print("Ingresa tu numero entre 0 y 10: ")
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
                    print("Te quedastes sin vidas")
                    print(f"El numero era {self.getnumeroAAdivinar()}")
                    return

                if (numeroUsuario > self.getnumeroAAdivinar()):
                    print("El numero a adivinar es menor");
                else :
                    print("El numero a adivinar es mayor");

                print("Vidas Restantes: ", self.getnumeroDeVidas())
                print("_________________________________")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self,numeroDeVidas):
        super().__init__(numeroDeVidas)
        super().setnumeroAAdivinar(random.randint(0, 5) * 2)

    def validarNumero(self, numero):
        if (numero % 2 != 0):
            print("El numero debe ser Par")
            return True
        if (numero > 0 and numero < 10):
            return False
        return True

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self,numeroDeVidas):
        super().__init__(numeroDeVidas)
        super().setnumeroAAdivinar(random.randint(0, 4) * 2 + 1)


    def validarNumero(self, numero):
        if (numero % 2 == 0):
            print("El numero debe ser Impar")
            return True
        if (numero > 0 and numero < 10):
            return False
        return True


game1 = JuegoAdivinaNumero(3)
game2 = JuegoAdivinaPar(3)
game3 = JuegoAdivinaImpar(3)
print("Primer Juego")
game1.juega()

print("Segundo Juego")
game2.juega()

print("Tercer Juego")
game3.juega()
