//AppJuego2.java
package LAB_Ejercicios_02;
public class AppJuego2 {
    public static void main(String[] args) {
        JuegoAdivinaNumero Juego1 = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar Juego2 = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar Juego3 = new JuegoAdivinaImpar(3);
        System.out.println("PRIMER JUEGO ");
        Juego1.juega();
        System.out.println("SEGUNDO JUEGO: Numeros Pares");
        Juego2.juega();
        System.out.println("TERCER JUEGO: Numero Impares");
        Juego3.juega();
    }
}
