//Main.java
package Practica_8;
public class Main {
    public static void main(String[] args) {
        C num = new C(5, 10, 25);
        num.incrementaXYZ();
        System.out.println(num);

        num.incrementaZ();
        System.out.println(num);

        num.incrementaYZ();
        System.out.println(num);

        num.incrementaZ();
        System.out.println(num);

        num.incrementaXZ();
        System.out.println(num);
    }
}