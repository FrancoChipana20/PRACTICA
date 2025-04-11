#Se hace referencia a algunos animales mediante las siguientes clases:
    #a)Instanciar 1 Perro, 1 Gato y 1 Pájaro.
    #b)Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico.
    #c)Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.).

class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} corre sobre sus patas.")
        
class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} salta ágilmente.")

class Pajaro:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Pío!")

    def moverse(self):
        print(f"{self.nombre} vuela por el cielo.")

perro1 = Perro("Max", 5, "Labrador")
gato1 = Gato("Michi", "Negro")
pajaro1 = Pajaro("Piolín", "Canario")

perro1.hacerSonido()
perro1.moverse()

gato1.hacerSonido()
gato1.moverse()

pajaro1.hacerSonido()
pajaro1.moverse()
