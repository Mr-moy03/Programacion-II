package fileB;

public class Anuncio {
    private int numero;
    private int precio;
    public Anuncio(int numero,int precio){
        this.numero = numero; 
        this.precio = precio;
    }
    
    public int getNumero(){
        return this.numero;
    }
    
    public int getPrecio(){
        return this.precio;
    }
    
    public void setNunero(int n){
        this.numero = n;
    }
    
    public void setPrecio(int p){
        this.precio = p;
    }
    
    @Override
    public String toString(){
        return String.format("Numero %d, Precio: %d",getNumero(),getPrecio());
    }
    
    
}