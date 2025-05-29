package fileB;

public class Main {
    
    public static void main(String[] args) {
        // Main
        // a)
        // artistas
        Artista a1 = new Artista("Juan",1001,2);
        Artista a2 = new Artista("luis",1002,3);
        // anuncio
        Anuncio b1 = new Anuncio(1,100);
        Anuncio b2 = new Anuncio(2,250);
        // pinturas
        Pintura pint1 = new Pintura("monalisa","oleo","abstracto");
        Pintura pint2 = new Pintura("abstracto","acuarela","drama");
        
        pint1.addArtista(a1);
        pint1.addAnuncio(b1);
        
        pint2.addArtista(a2);
        pint2.addAnuncio(b2);
        
        // b)
        System.out.println(pint1.promedio(pint2));
        
        // c)
        System.out.println(pint1.increment("Juan",230));
        
    }
    
}