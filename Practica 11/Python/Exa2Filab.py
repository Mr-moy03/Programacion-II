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
        
    def promedio(self,other): 
        r = "Promedio de años de experiencia: \n"
        todos = self.getArtista() + other.getArtista()
        prom = 0 
        for art in todos:
            prom += art.getAniosExperiencia()
        
        prom /= len(todos)
        r += f"el promedio es {prom}"
        return r 
    
    def increment(self,x,y): 
        r = "" 
        for art in self.getArtista():
            if art.getNombre() == x:
                a = self.getAnuncio()
                nPrecio = a.getPrecio()+y
                a.setPrecio(nPrecio)
                r += f"Incremntado, nuevo precio {nPrecio}"
                return r
            
        return "No se encontro el nombre"
        
    
        
    
    
        
    
        
        
# Main 
#a 
#artistas 
a1 = Artista("Juan",1001,2)
a2 = Artista("luis",1002,3)
#anuncio
b1 = Anuncio(1,100)
b2= Anuncio(2,250)
#pinturas
pint1 = Pintura("monalisa","oleo","abstracto")

pint2 = Pintura("abstracto","acuarela","drama") 
#metodos
pint1.addArtista(a1)
pint1.addAnuncio(b1)

pint2.addArtista(a2)
pint2.addAnuncio(b2)

#b
print(pint1.promedio(pint2))

#c 
print(pint1.increment("Juan",230))







