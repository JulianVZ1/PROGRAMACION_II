public class EcuacionCuadratica {

    private double a;
    private double b;
    private double c;

    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return b * b - 4 * a * c;
    }

    public double getRaiz1() {
        return (-b + Math.sqrt(getDiscriminante())) / (2 * a);
    }

    public double getRaiz2() {
        return (-b - Math.sqrt(getDiscriminante())) / (2 * a);
    }
}
