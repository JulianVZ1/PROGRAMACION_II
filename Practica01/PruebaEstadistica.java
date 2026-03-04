import java.util.Scanner;

public class PruebaEstadistica {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double[] numeros = new double[10];

        System.out.println("Ingrese 10 numeros:");

        for (int i = 0; i < 10; i++) {
            numeros[i] = sc.nextDouble();
        }

        Estadistica estadistica = new Estadistica(numeros);

        System.out.println("El promedio es "
                + String.format("%.2f",estadistica.promedio()));

        System.out.println("La desviación estándar es "
                + String.format("%.5f", estadistica.desviacion()));

        sc.close();
    }
}
