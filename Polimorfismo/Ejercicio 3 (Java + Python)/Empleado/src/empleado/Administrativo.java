package empleado;

class Administrativo extends Empleado {
    private String cargo;

    public Administrativo(String nombre, double sueldoMes, String cargo) {
        super(nombre, sueldoMes);
        this.cargo = cargo;
    }
}