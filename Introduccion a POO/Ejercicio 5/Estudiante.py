#Crea una clase Estudiante con nombre, nota_1, nota_2
    #a)Agrega un método para calcular el promedio
    #b)Agrega un método para verificar si aprobó (promedio >=6)
    #c)Crea tres estudiantes, muestra sus promedios y si aprobaron

class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def promedio(self):
        return (self.nota_1 + self.nota_2) / 2

    def aprobo(self):
        if self.promedio() >= 6:
            return "Aprobo"
        else:
            return "Reprobo"

est1 = Estudiante("Carlos", 7, 8)
est2 = Estudiante("Maria", 5, 6)
est3 = Estudiante("Lucia", 10, 10)
for est in [est1, est2, est3]:
    print(f"{est.nombre}: Promedio = {est.promedio()}, {est.aprobo()}")
