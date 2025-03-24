package Ejercicio_2;

import java.util.Scanner;

public class Estadistica_Poo {
    public float[] v;

    public Estadistica_Poo(float[] v){
        this.v = v;
    }

    public float promedio() {
        float suma = 0;
        for (double numero : this.v) {
            suma += numero;
        }
        return suma / v.length;
    }

    public float desviacion() {
        float p = promedio();
        float sum = 0;
        for (double vi : this.v) {
            sum += Math.pow(vi - p, 2);
        }
        return (float)Math.sqrt(sum / (v.length - 1));
    }

    @Override
    public String toString() {
        return String.format("El promedio es %.2f\nLa desviación estándar es %.5f", promedio(), desviacion());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] vStr = sc.nextLine().split(" ");

        float[] v = new float[vStr.length];
        for (int i = 0; i < vStr.length; i++) {
            v[i] = Float.parseFloat(vStr[i]);
        }
        Estadistica_Poo est = new Estadistica_Poo(v);
        System.out.println(est);
    }

}
