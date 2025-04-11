#Crea una clase Persona con nombre, edad y ciudad
    #a)Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
    #b)Crea tres personas y muestra su saludo
    #c)Agrega un método para verificar si es mayor de edad

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
    def saludo(self):
        return f"Hola, soy {self.nombre} de {self.ciudad}"
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad"
        else:
            return f"{self.nombre} es menor de edad"
        
persona1 = Persona("Luis", 25, "La Paz")
persona2 = Persona("Ana", 17, "Cochabamba")
persona3 = Persona("Pedro", 30, "Santa Cruz")

print(persona1.saludo())
print(persona2.saludo())
print(persona3.saludo())

print(persona1.es_mayor_de_edad())
print(persona2.es_mayor_de_edad())
print(persona3.es_mayor_de_edad())
