import java.util.Random;

public class PruebaCronometro {

    public static void main(String[] args) {

        int[] numeros = new int[100000];
        Random random = new Random();

        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = random.nextInt(100000);
        }

        Cronometro cronometro = new Cronometro();

        cronometro.inicia();

        for (int i = 0; i < numeros.length - 1; i++) {

            int minimo = i;

            for (int j = i + 1; j < numeros.length; j++) {
                if (numeros[j] < numeros[minimo]) {
                    minimo = j;
                }
            }

            int temp = numeros[i];
            numeros[i] = numeros[minimo];
            numeros[minimo] = temp;
        }

        cronometro.detener();

        System.out.println("Tiempo de ejecución: "
                + cronometro.lapsoDeTiempo()
                + " milisegundos");
    }
}
