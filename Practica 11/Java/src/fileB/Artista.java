package fileB;


public class Artista {
    private String nombre;
    private int ci;
    private int añosExperiencia;
    public Artista(String nombre,int ci,int añosExperiencia){
        this.nombre = nombre;
        this.ci = ci;
        this.añosExperiencia = añosExperiencia;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    
    public int getCi(){
        return this.ci;
    }
    
    public int getAñosExperiencia(){
        return this.añosExperiencia;
    }
    
    public void setNombre(String n){
        this.nombre = n;
    }
    
    public void setCi(int c){
        this.ci = c;
    }
    
    public void setAñosExperiencia(int a){
        this.añosExperiencia = a;
    }
    
    @Override
    public String toString(){
        return String.format("Nombre: %s,Ci: %d,Años de experiencia: %d",getNombre(),getCi(),getAñosExperiencia());
    }
}