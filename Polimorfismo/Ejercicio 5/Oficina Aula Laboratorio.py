#Se hace referencia a algunos de los diferentes ambientes de la Universidad mediante las siguientes clases:
    #a)Instanciar 2 objetos Oficina, 2 Aulas y 1 Laboratorio
    #b)Crear un método mostrar() para mostrar los datos de cada objeto
    #c)Sobrecargar el método cantidadMuebles(), para conocer el número total de muebles dentro de cada ambiente

class Oficina:
    def __init__(self, nroSillas, nroEscritorios, nroEstanterias):
        self.nroSillas = nroSillas
        self.nroEscritorios = nroEscritorios
        self.nroEstanterias = nroEstanterias

    def mostrar(self):
        print(f"Oficina - Sillas: {self.nroSillas}, Escritorios: {self.nroEscritorios}, Estanterías: {self.nroEstanterias}")

    def cantidadMuebles(self):
        return self.nroSillas + self.nroEscritorios + self.nroEstanterias


class Aula:
    def __init__(self, nombre, capacidad, nroPupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroPupitres = nroPupitres

    def mostrar(self):
        print(f"Aula {self.nombre} - Capacidad: {self.capacidad}, Pupitres: {self.nroPupitres}")

    def cantidadMuebles(self):
        return self.nroPupitres


class Laboratorio:
    def __init__(self, nombre, nroMesas, nroSillas):
        self.nombre = nombre
        self.nroMesas = nroMesas
        self.nroSillas = nroSillas

    def mostrar(self):
        print(f"Laboratorio {self.nombre} - Mesas: {self.nroMesas}, Sillas: {self.nroSillas}")

    def cantidadMuebles(self):
        return self.nroMesas + self.nroSillas


oficina1 = Oficina(5, 2, 3)
oficina2 = Oficina(6, 3, 2)
aula1 = Aula("A101", 30, 30)
aula2 = Aula("B202", 25, 25)
laboratorio1 = Laboratorio("Lab Computación", 10, 20)

ambientes = [oficina1, oficina2, aula1, aula2, laboratorio1]

for ambiente in ambientes:
    ambiente.mostrar()

print("\nCantidad de muebles en cada ambiente:")
for ambiente in ambientes:
    print(f"{ambiente.__class__.__name__}: {ambiente.cantidadMuebles()} muebles")
