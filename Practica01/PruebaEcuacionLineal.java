import java.util.Scanner;

public class PruebaEcuacionLineal {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese a, b, c, d, e, f:");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double d = sc.nextDouble();
        double e = sc.nextDouble();
        double f = sc.nextDouble();

        EcuacionLineal ecuacion = 
            new EcuacionLineal(a, b, c, d, e, f);

        if (ecuacion.tieneSolucion()) {

            System.out.println("x = " + ecuacion.getX());
            System.out.println("y = " + ecuacion.getY());

        } else {
            System.out.println("La ecuación no tiene solución");
        }

        sc.close();
    }
}
