#Realiza la abstracción de una Computadora
    #a)Muestra los componentes principales de la computadora
    #b)Muestra el estado de la computadora (encendido o apagado)
    #c)Crea una instancia y simula encender y apagar la computadora.

class Computadora:
    def __init__(self):
        self.estado = "apagado"
        self.componentes = ["CPU", "RAM", "Disco Duro", "Tarjeta Gráfica"]

    def encender(self):
        if self.estado == "apagado":
            self.estado = "encendido"
            print("Computadora encendida.")
        else:
            print("La computadora ya está encendida.")

    def apagar(self):
        if self.estado == "encendido":
            self.estado = "apagado"
            print("Computadora apagada.")
        else:
            print("La computadora ya está apagada.")

    def mostrar_componentes(self):
        return self.componentes

mi_pc = Computadora()
print("Componentes:", mi_pc.mostrar_componentes())
mi_pc.encender()
mi_pc.apagar()
