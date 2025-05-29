package fileB;

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
    public String promedio(Pintura other){
        StringBuilder r = new StringBuilder();
        ArrayList<Artista> todos = new ArrayList<>();
        todos.addAll(this.getArtista());
        todos.addAll(other.getArtista());
        r.append("Promedio de años de experiencia: ").append("\n");
        int prom = 0;
        for (Artista art: todos){
            prom += art.getAñosExperiencia();
        }
        prom /= todos.size();
        r.append(String.format("El promedio : %d",prom));
        return r.toString();
    }
    
    public String increment(String x,int y){
        StringBuilder r = new StringBuilder();
        for (Artista art: this.getArtista()){
            if (art.getNombre().equals(x)){
                Anuncio a = this.getAnuncio();
                int nPrecio = a.getPrecio() + y;
                a.setPrecio(nPrecio);
                r.append(String.format("Incremntado, nuevo precio: %d",nPrecio));
                return r.toString();
            }
        }
        return "No se encontro el nombre";
    }
    
    @Override
    public String toString(){
        StringBuilder r = new StringBuilder();
        r.append(super.toString()).append("\n");
        r.append(String.format("Genero: %s ",getGenero()));
        return r.toString();
    }
}