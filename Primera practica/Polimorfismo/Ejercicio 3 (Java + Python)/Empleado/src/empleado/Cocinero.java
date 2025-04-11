package empleado;

class Cocinero extends Empleado {
    private int horasExtra;
    private double sueldoHora;

    public Cocinero(String nombre, double sueldoMes, int horasExtra, double sueldoHora) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }

    @Override
    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora);
    }
}