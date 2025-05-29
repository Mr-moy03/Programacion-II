package filaA;

public class Main {
    public static void main(String[] args) {
        // a)
        // artistas
        Artista a1 = new Artista("Juan",1001,2);
        Artista a2 = new Artista("luis",1002,3);
        // anuncio
        Anuncio b = new Anuncio(1,100);
        // pinturas
        Pintura pint1 = new Pintura("monalisa","oleo","abstracto");
        Pintura pint2 = new Pintura("abstracto","acuarela","drama");
        
        pint1.addArtista(a1);
        pint2.addArtista(a2);
        pint1.addAnuncio(b);
        
        // b)
        System.out.println(pint1.mayor(pint2));
        
        // c)
        Anuncio c = new Anuncio(2,200);
        pint2.addAnuncio(c);
        
        System.out.println(pint1.total(pint2));
        
        
    }
    
}