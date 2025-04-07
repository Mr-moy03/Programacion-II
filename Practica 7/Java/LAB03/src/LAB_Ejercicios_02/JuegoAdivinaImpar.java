//JuegaAdivinaImpar.java
package LAB_Ejercicios_02;
public class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
        setNumeroAAdivinar((int)(Math.random() * 5) * 2 + 1);
    }
    @Override
    public boolean validarNumero(int numero) {
        if (numero % 2 == 0){
            System.out.println("El numero debe ser Impar");
            return true;
        }
        if (numero > 0 && numero < 10) {
            return false;
        }
        return true;
    }
}
