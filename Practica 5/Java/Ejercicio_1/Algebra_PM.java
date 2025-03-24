package Ejercicio_1;
import java.util.Scanner;

public class Algebra_PM {
    public static float getDiscriminante(float a,float b,float c){
        return (float)Math.pow(b,2) - 4 * a * c;
    }
    public static float getRaiz1(float a,float b,float c){
        return (float)(-b + Math.sqrt(getDiscriminante(a,b,c))) / (2 * a);
    }
    public static float getRaiz2(float a,float b,float c){
        return (float)(-b - Math.sqrt(getDiscriminante(a,b,c))) / (2 * a);
    }
    public static String resolver(float a,float b,float c){
        if (getDiscriminante(a,b,c) > 0 ){
            return String.format("%.6f %.5f",getRaiz1(a, b, c),getRaiz2(a, b, c));
        }
        if (getDiscriminante(a,b,c) == 0 ){
            return String.format("%.2f",getRaiz1(a, b, c));
        }
        else {
            return "La ecuacion no tiene raıces reales";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input= sc.nextLine().split(" ");
        float a = Float.parseFloat(input[0]);
        float b = Float.parseFloat(input[1]);
        float c = Float.parseFloat(input[2]);
        System.out.println(resolver(a,b,c));


    }
}
