//Sea la clase Videojuego: 
    //a) Instanciar al menos 2 videojuegos 
    //b) Sobrecargar el constructor 2 veces 
    //c) Implementar un método mostrar() 
    //d) Sobrecargar el método agregarJugadores() donde en el primero se agregue solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.  

package ejercicios.pkg1;

public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = 1;
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Cantidad de jugadores: " + cantidadJugadores);
    }

    public void agregarJugadores() {
        cantidadJugadores++;
    }

    public void agregarJugadores(int cantidad) {
        cantidadJugadores += cantidad;
    }

    public static void main(String[] args) {
        Videojuego juego1 = new Videojuego("FIFA 24", "PlayStation", 4);
        Videojuego juego2 = new Videojuego("Among Us", "PC");

        juego1.mostrar();
        System.out.println();
        juego2.mostrar();

        System.out.println("\nAgregando jugadores...");
        juego1.agregarJugadores();           
        juego2.agregarJugadores(3);         

        System.out.println();
        juego1.mostrar();
        System.out.println();
        juego2.mostrar();
    }
}