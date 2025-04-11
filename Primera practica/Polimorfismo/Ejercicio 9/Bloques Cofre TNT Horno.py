#Para los bloques del juego Minecraft se usará los siguientes objetos:
    #a)Crear e instanciar al menos 2 bloques de cada tipo
    #b)Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque.
    #c)Sobrecarga colocar() para permitir colocar un bloque en diferentes orientaciones (por ejemplo, en el suelo o en la pared).
    #d)Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque y que puede suceder al romperlos.


class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo

    def accion(self):
        print(f"Bloque Cofre tipo {self.tipo}: Abriendo el cofre...")

    def colocar(self, ubicacion):
        print(f"Cofre colocado en el {ubicacion}.")

    def romper(self):
        print(f"Cofre roto. Se caen los objetos que tenía guardados.")

class BloqueTnt:
    def __init__(self, tipo, dano):
        self.tipo = tipo
        self.dano = dano

    def accion(self):
        print(f"Bloque TNT tipo {self.tipo}: Preparando para explotar...")

    def colocar(self, ubicacion):
        print(f"TNT colocada en el {ubicacion}. ¡Cuidado!")

    def romper(self):
        print(f"TNT rota. ¡Explota causando {self.dano} de daño!")

class BloqueHorno:
    def __init__(self, color, capacidadComida):
        self.color = color
        self.capacidadComida = capacidadComida

    def accion(self):
        print(f"Horno {self.color}: Cocinando comida... Capacidad: {self.capacidadComida}")

    def colocar(self, ubicacion):
        print(f"Horno colocado en el {ubicacion}.")

    def romper(self):
        print("Horno roto. Se pierden los alimentos cocinados.")

# ---------------------
cofre1 = BloqueCofre(30, 100, "Madera")
cofre2 = BloqueCofre(50, 200, "Hierro")

tnt1 = BloqueTnt("Explosiva", 100)
tnt2 = BloqueTnt("SuperExplosiva", 200)

horno1 = BloqueHorno("Gris", 10)
horno2 = BloqueHorno("Negro", 20)

# ---------------------
for bloque in [cofre1, cofre2, tnt1, tnt2, horno1, horno2]:
    bloque.accion()
    bloque.colocar("suelo")
    bloque.romper()
    print("-" * 30)
