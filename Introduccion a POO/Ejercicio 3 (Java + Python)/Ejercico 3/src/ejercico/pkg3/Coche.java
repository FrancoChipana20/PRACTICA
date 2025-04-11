//Crea una clase Coche con marca, modelo y velocidad
    //a) Agrega un método acelerar () que aumente la velocidad en 10 
    //b) Agrega un método frenar () que disminuya la velocidad en 5 
    //c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
    
package ejercico.pkg3;

public class Coche {
    private String marca;
    private String modelo;
    private int velocidad;

    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0; 
    }
    
    public void acelerar() {
        velocidad += 10;
    }
    
    public void frenar() {
        velocidad -= 5;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }
    
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Nissan", "Sentra");

        coche1.acelerar();
        coche1.acelerar();

        coche2.acelerar();
        coche2.frenar();

        System.out.println("Velocidad del " + coche1.getMarca() + " " + coche1.getModelo() + ": " + coche1.getVelocidad());
        System.out.println("Velocidad del " + coche2.getMarca() + " " + coche2.getModelo() + ": " + coche2.getVelocidad());
    }
}