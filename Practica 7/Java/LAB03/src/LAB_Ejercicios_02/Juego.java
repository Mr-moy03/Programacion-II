//Juego.java
package LAB_Ejercicios_02;
public class Juego {
    //Atributos
    private int numeroDeVidas;
    private int record;
    //Metodos
    public Juego(int numeroDeVidas, int record) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = record;
    }
    public int getNumeroDeVidas() {
        return numeroDeVidas;
    }
    public void setNumeroDeVidas(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
    }
    public int getRecord() {
        return record;
    }
    public void setRecord(int record) {
        this.record = record;
    }
    public void reiniciaPartida(){
        setNumeroDeVidas(this.numeroDeVidas);
        setRecord(0);
    }
    public void actualizaRecord(){
        setRecord(getRecord() + 10);
    }
    public boolean quitaVida(){
        if (getNumeroDeVidas() > 1){
            setNumeroDeVidas(getNumeroDeVidas() - 1);
            return true;
        }
        else {
            return false;}
    }
}

