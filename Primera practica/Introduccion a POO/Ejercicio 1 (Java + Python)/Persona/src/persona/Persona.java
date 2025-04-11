//Crea una clase Persona con nombre, edad y ciudad 
    //a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}” 
    //b) Crea tres personas y muestra su saludo 
    //c) Agrega un método para verificar si es mayor de edad 
package persona;

public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }
    
    public String saludo() {
        return "Hola, soy " + nombre + " de " + ciudad;
    }
    
    public String esMayorDeEdad() {
        if (edad >= 18) {
            return nombre + " es mayor de edad";
        } else {
            return nombre + " es menor de edad";
        }
    }
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Luis", 25, "La Paz");
        Persona persona2 = new Persona("Ana", 17, "Cochabamba");
        Persona persona3 = new Persona("Pedro", 30, "Santa Cruz");

        System.out.println(persona1.saludo());
        System.out.println(persona2.saludo());
        System.out.println(persona3.saludo());

        System.out.println(persona1.esMayorDeEdad());
        System.out.println(persona2.esMayorDeEdad());
        System.out.println(persona3.esMayorDeEdad());
    }
}
