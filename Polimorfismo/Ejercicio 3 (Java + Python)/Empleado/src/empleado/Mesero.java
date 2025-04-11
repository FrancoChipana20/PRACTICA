package empleado;

class Mesero extends Empleado {
    private int horasExtra;
    private double sueldoHora;
    private double propina;

    public Mesero(String nombre, double sueldoMes, int horasExtra, double sueldoHora, double propina) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    @Override
    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora) + propina;
    }
}