package Figuras;

public class FiguraGeometrica {
    //Circulo
    double area(double radio){
        return Math.PI * radio * radio;
    }
    //Rectangulo
    double area(double base, double altura){
        return base * altura;
    }

    //Triangulo Rectangulo
    double area(double base, int altura){
        return (base * altura)/2;
    }
    //Trapecio
    double area(double baseMayor, double baseMenor, double altura){
        return ((baseMayor * baseMenor) * altura) / 2;
    }
    //Pentagono
    double area(int longitud, double apotema){
        return (5.0/2.0)*longitud * apotema;
    }

    public static void main(String[] args){
        FiguraGeometrica f1 = new FiguraGeometrica();
        FiguraGeometrica f2 = new FiguraGeometrica();
        FiguraGeometrica f3 = new FiguraGeometrica();
        FiguraGeometrica f4 = new FiguraGeometrica();
        FiguraGeometrica f5 = new FiguraGeometrica();


        System.out.println("Circulo: "+f1.area(1.0));
        System.out.println("Rectangulo: "+f2.area(2.0,3.0));
        System.out.println("Triangulo Rectangulo: "+f3.area(3.0,7));
        System.out.println("Trapecio: "+f4.area(2.0,3.0,5.0));
        System.out.println("Pentagono: "+f5.area(3,5.0));
    }
}
