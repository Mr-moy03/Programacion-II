//JuegoAdivinaNumero.java
package LAB_Ejercicios_02;
import java.util.Scanner;
public class JuegoAdivinaNumero extends Juego{
    //Atributos
    private int numeroAAdivinar;
    //metodos
    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas, 0);
        this.numeroAAdivinar = (int)(Math.random() * 10) + 1;;
    }
    public int getNumeroAAdivinar() {
        return numeroAAdivinar;
    }
    public void setNumeroAAdivinar(int numeroAAdivinar) {
        this.numeroAAdivinar = numeroAAdivinar;
    }
    public boolean validarNumero(int numero) {
        if (numero < 0 || numero > 10) {
            return true;
        }
        return false;
    }
    public void juega(){
        reiniciaPartida();
        System.out.println("__AdivinaAdivinador__");
        System.out.println("VIDAS: "+ getNumeroDeVidas());
        Scanner sc = new Scanner(System.in);

        while (getNumeroDeVidas() > 0){
            System.out.println("Ingresa tu numero: ");

            int numeroUsuario = sc.nextInt();
            while (validarNumero(numeroUsuario)){
                System.out.println("Ingresa tu numero entre 0 y 10: ");
                numeroUsuario = sc.nextInt();
            }
            if (numeroUsuario == this.numeroAAdivinar) {
                System.out.printf("Acertaste, el nuemro era %s",this.numeroAAdivinar);
                actualizaRecord();
                System.out.println("\nRecord: "+getRecord());
                System.out.println("Vidas: "+getNumeroDeVidas());
                if (getNumeroDeVidas() > 0){
                    System.out.println("Siguiente Numero a adivinar ???");
                    setNumeroAAdivinar((int)(Math.random() * 10) + 1);;
                    continue;
                }
                return;
            }
            else {
                if (!quitaVida()){
                    System.out.println("GAME OVER");
                    System.out.println("Te quedastes sin vidas ");
                    System.out.print("EL numero era: "+getNumeroAAdivinar());
                    return;
                }
                if (numeroUsuario > this.numeroAAdivinar) {
                    System.out.println("El numero a adivinar es menor" );

                }
                else {
                    System.out.println("El numero a adivinar es mayor" );
                }
                System.out.println("Vidas Restantes: "+getNumeroDeVidas());
                System.out.println("_________________________________");
            }
        }
    }
}


