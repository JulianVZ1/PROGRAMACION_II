import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("Partida reiniciada")

    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan vidas:", self.numeroDeVidas)

        if self.numeroDeVidas > 0:
            return True
        else:
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()

        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            numero = int(input("Adivina un número entre 0 y 10: "))

            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if numero < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")
                else:
                    print("Perdiste, no quedan vidas")
                    break

if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)
    juego.juega()
