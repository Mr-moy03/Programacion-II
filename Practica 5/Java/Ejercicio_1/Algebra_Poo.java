package Ejercicio_1;

import java.util.Scanner;

public class Algebra_Poo {
    private float a;
    private float b;
    private float c;
    public Algebra_Poo(float a,float b, float c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public float getDiscriminante(){
        return (float) Math.pow(b,2) - 4 * a * c;
    }
    public float getRaiz1(float disc){
        return (float)(-this.b + Math.sqrt(getDiscriminante())) / (2 * a);
    }
    public float getRaiz2(float disc){
        return (float)(-this.b - Math.sqrt(getDiscriminante())) / (2 * a);
    }

    @Override
    public String toString(){
        float disc = getDiscriminante();
        if (disc > 0 ){
            return String.format("La ecuación tiene dos raíces %.6f y %.5f",getRaiz1(disc),getRaiz2(disc));
        }
        if (disc == 0 ){
            return String.format("La ecuación tiene una raíz %.0f",getRaiz1(disc));
        }
        else {
            return "La ecuación no tiene raíces reales";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese a, b, c: ");
        String[] input= sc.nextLine().split(" ");
        float a = Float.parseFloat(input[0]);
        float b = Float.parseFloat(input[1]);
        float c = Float.parseFloat(input[2]);

        Algebra_Poo ec = new Algebra_Poo(a,b,c);
        System.out.println(ec);
    }

}
