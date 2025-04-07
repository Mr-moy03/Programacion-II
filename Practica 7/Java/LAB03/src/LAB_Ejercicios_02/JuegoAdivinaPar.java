//JuegaAdivinaPar.java
package LAB_Ejercicios_02;
public class JuegoAdivinaPar extends JuegoAdivinaNumero{
    public JuegoAdivinaPar(int numeroDeVidas) {
        super(numeroDeVidas);
        setNumeroAAdivinar((int)(Math.random() * 6) * 2);
    }
    @Override
    public boolean validarNumero(int numero) {
        if (numero % 2 != 0){
            System.out.println("El numero debe ser Par");
            return true;
        }
        if (numero > 0 && numero < 10) {
            return false;
        }
        return true;
    }
}
