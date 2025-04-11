#Crea una clase Coche con marca, modelo y velocidad
    #a)Agrega un método acelerar () que aumente la velocidad en 10
    #b)Agrega un método frenar () que disminuya la velocidad en 5
    #c)Crea dos coches, aceléralos, frénalos y muestra sus velocidades

class Coche:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        
    def frenar(self):
        self.velocidad -= 5
        
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Nissan", "Sentra")

coche1.acelerar()
coche1.acelerar()
coche2.acelerar()
coche2.frenar()

print(f"Velocidad del {coche1.marca} {coche1.modelo}: {coche1.velocidad}")
print(f"Velocidad del {coche2.marca} {coche2.modelo}: {coche2.velocidad}")
