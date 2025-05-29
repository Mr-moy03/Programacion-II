package fileB;

import java.util.ArrayList;

public class Obra {
    private String titulo;
    private String material;
    private ArrayList<Artista> artista;
    private Anuncio anuncio;
    public Obra(String titulo,String material){
        this.titulo = titulo;
        this.material = material;
        this.artista = new ArrayList<>();
        this.anuncio = null;
    }
    
    public String getTitulo(){
        return this.titulo;
    }
    public String getMaterial(){
        return this.material;
    }
    
    public ArrayList<Artista> getArtista(){
        return this.artista;
    }
    
    public Anuncio getAnuncio(){
        return this.anuncio;
    }
    public void setAnuncio(Anuncio a){
        this.anuncio = a;
    }
    
    public void addArtista(Artista a){
        this.artista.add(a);
    }
    
    public void addAnuncio(Anuncio a){
        this.anuncio = a;
    }
    
    @Override
    public String toString(){
        StringBuilder r = new StringBuilder();
        r.append(String.format("Titulo: %s, Material: %s\n",getTitulo(),getMaterial()));
        for (Artista list: getArtista()){
            r.append(String.format("Artista: ")).append(list).append("\n");
        }
        r.append("Anuncio: ").append(getAnuncio());
        return r.toString();
    }
}