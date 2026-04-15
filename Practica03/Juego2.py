import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("Partida reiniciada")

    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas:", self.numeroDeVidas)

        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            num = int(input("Número (0-10): "))

            if not self.validaNumero(num):
                print("Número inválido")
                continue

            if num == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("Mayor")
                    else:
                        print("Menor")
                else:
                    print("Sin vidas")
                    break


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            return False

        if num % 2 != 0:
            print("Error: número impar")
            return False

        return True


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            return False

        if num % 2 == 0:
            print("Error: número par")
            return False

        return True

if __name__ == "__main__":
    juego1 = JuegoAdivinaNumero(3)
    juego2 = JuegoAdivinaPar(3)
    juego3 = JuegoAdivinaImpar(3)

    print("\n Juego normal ")
    juego1.juega()

    print("\n Juego pares ")
    juego2.juega()

    print("\n Juego impares ")
    juego3.juega()
