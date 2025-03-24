package Ejercicio_2;

import java.util.*;

public class Estadistica_PM {
    public static float promedio(float[] v){
        float sum = 0;
        for(float vi : v){
            sum += vi;

        }
        return sum / v.length;

    }

    public static float desviacion(float[] v){
        float sum = 0;
        float p = promedio(v);
        for (float vi : v) {
            sum += (float)(Math.pow((vi - p),2) );
        }
        return (float)Math.sqrt(sum / (v.length - 1));
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] vStr = sc.nextLine().split(" ");

        float[] v = new float[vStr.length]; // Crear array de float
        for (int i = 0; i < vStr.length; i++) {
            v[i] = Float.parseFloat(vStr[i]); // Convertir cada elemento a float
        }


        float p = promedio(v);
        float d = desviacion(v);

        System.out.println(String.format("EL promedio es %.2f",p));
        System.out.println(String.format("La desviación estándar es %.5f",d));



    }
}
