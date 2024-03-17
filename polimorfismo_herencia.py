# Polimorfismo con Herencia
class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')

class Aguila:
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('La gallina no puede volar')

objeto_ave = Aves()
objeto_ave.volar()


objeto_aguila = Aguila()
objeto_aguila.volar()

objeto_gallina = Gallina()
objeto_gallina.volar()

