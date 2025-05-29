package filaA;
import java.util.ArrayList;

public class Pintura extends Obra{ 
    private String genero;
    public Pintura(String titulo,String material,String genero){
        super(titulo,material);
        this.genero = genero;
    }
    public String getGenero(){
        return this.genero;
    }
    public void setGenero(String g){
        this.genero = g; 
    }
    public String mayor(Pintura other){
        StringBuilder r = new StringBuilder();
        ArrayList<Artista> todos = new ArrayList<>();
        todos.addAll(this.getArtista());
        todos.addAll(other.getArtista());
        r.append("Artista con mayor experiencia: ").append("\n");
        int mayor = 0;
        for (Artista art: todos){
            if (art.getAñosExperiencia() > mayor){
                mayor = art.getAñosExperiencia();
            }
        }
        for (Artista art: todos){
            if (art.getAñosExperiencia() == mayor){
                r.append(art).append("\n");
            }
        }
        return r.toString();
    }
    
    public String total(Pintura other){
        int total = this.getAnuncio().getPrecio() + other.getAnuncio().getPrecio();
        
                
        return String.format("Total de precio: %d",total);
    }
    
    @Override
    public String toString(){
        StringBuilder r = new StringBuilder();
        r.append(super.toString()).append("\n");
        r.append(String.format("Genero: %s ",getGenero()));
        return r.toString();
    }
}