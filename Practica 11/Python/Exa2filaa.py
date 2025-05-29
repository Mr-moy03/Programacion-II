class Anuncio:
    def __init__(self,numero,precio):
        self.__numero = numero 
        self.__precio = precio 
    def getNumero(self): 
        return self.__numero 
    def getPrecio(self): 
        return self.__precio 
    
    def setNumero(self,n): 
        self.__numero = n 
    
    def setPrecio(self,p): 
        self.__precio = p 
        
    def __str__(self):
        return f"Numero: {self.getNumero()},Precio {self.getPrecio()}"
        
        
class Artista:
    def __init__(self,nombre,ci,aniosExperiencia):
        self.__nombre = nombre 
        self.__ci = ci 
        self.__aniosExperiencia = aniosExperiencia 
    def getNombre(self): 
        return self.__nombre 
    
    def getCi(self): 
        return self.__ci 
    
    def getAniosExperiencia(self):
        return self.__aniosExperiencia 
    
    def setNombre(self,n): 
        self.__nombre = n 
    
    def setCi(self,c): 
        self.__ci = c 
    
    def setAniosExperiencia(self,a): 
        self.__aniosExperiencia = a 
        
    def __str__(self): 
        return f"Nombre: {self.getNombre()},Ci: {self.getCi()},Años de experiencia: {self.getAniosExperiencia()}"
    
class Obra: 
    def __init__(self,titulo,material): 
        self.__titulo = titulo 
        self.__material = material 
        self.__artista = [] 
        self.__anuncio = None 
    def getTitulo(self): 
        return self.__titulo
    
    def getMaterial(self): 
        return self.__material 
        
    def getArtista(self): 
        return self.__artista 
    
    def getAnuncio(self): 
        return self.__anuncio
        
    def setTitulo(self,t): 
        self.__titulo = t      
    
    def setMaterial(self,m): 
        self.__material = m 
    
    def addArtista(self,a): 
        self.__artista.append(a) 
    
    def addAnuncio(self,a): 
        self.__anuncio = a  
    
class Pintura(Obra):
    def __init__(self,titulo,material,genero): 
        super().__init__(titulo,material)
        self.__genero = genero  
    def getGenero(self): 
        return self.__genero 
    
    def setGenero(self,g): 
        self.__genero = g 
        
    def mayor(self,other): 
        r = "Artista con mayor experiencia: \n"
        todos = self.getArtista() + other.getArtista()
        mayor = 0 
        for art in todos:
            if art.getAniosExperiencia() > mayor: 
                mayor = art.getAniosExperiencia()
        
        for art in todos:
            if art.getAniosExperiencia() == mayor: 
                r += f"{art}\n"
        return r 
    
    def total(self,other): 
        t = self.getAnuncio().getPrecio() + other.getAnuncio().getPrecio()
        return f"total de precio: {t}" 
        
    
    
        
    
        
        
# Main 
#a 
#artistas 
a1 = Artista("Juan",1001,2)
a2 = Artista("luis",1002,3)
#anuncio
b = Anuncio(1,100)
#pinturas
pint1 = Pintura("monalisa","oleo","abstracto")

pint2 = Pintura("abstracto","acuarela","drama") 
#metodos
pint1.addArtista(a1)
pint2.addArtista(a2)
pint1.addAnuncio(b) 

#b
print(pint1.mayor(pint2))

#c 
c = Anuncio(2,200)
pint2.addAnuncio(c)
print(pint1.total(pint2))





