from multimethod import multimethod
class LineaTeléferico:
    def __init__(self, color, tramo, nroCabinas, nroEmpleados):
        self.__color = color
        self.__tramo = tramo
        self.__nroCabinas = nroCabinas
        self.__nroEmpleados = nroEmpleados
        self.__empleados = []
        self.__edades = []
        self.__sueldos = []

    def setColor(self,color):
        self.__color = color
    def setTramo(self,tramo):
        self.__tramo = tramo
    def setNroCabinas(self,nroCabinas):
        self.__nroCabinas = nroCabinas
    def setNroEmpleados(self,nroEmpleados):
        self.__nroEmpleados = nroEmpleados
    def getColor(self):
        return self.__color
    def getTramo(self):
        return self.__tramo
    def getNroCabinas(self):
        return self.__nroCabinas
    def getNroEmpleados(self):
        return self.__nroEmpleados

    @classmethod
    def desde_otro(cls,nroCabinas,nroEmpleados):
        return cls(color = "Morado",tramo = "Estacion el faro murillo",nroCabinas = nroCabinas,nroEmpleados = nroEmpleados)

    def addEmpleados(self,a):
        self.__empleados.append(a)
    def addEdad(self,a):
        self.__edades.append(a)
    def addSueldo(self,a):
        self.__sueldos.append(a)

    def delEmpleado(self,x):
        i = 0
        for emp in self.__empleados:
            if x == emp['ApPaterno'] or x == emp['ApMaterno']:
                self.__empleados.remove(emp);del self.__edades[i];del self.__sueldos[i]
            i += 1

    def __add__(self, other):
        name, destino = other
        i = 0
        for emp in self.__empleados:
            if emp['Nombre'] == name:
                destino.addEmpleados(emp);destino.addEdad(self.__edades[i]);destino.addSueldo(self.__sueldos[i])
                del self.__empleados[i];del self.__edades[i];del self.__sueldos[i]
                break
            i += 1
        return destino

    def __str__(self):
        r = "lista: \n";i = 0
        r += f"{self.getColor()},{self.getTramo()},{self.getNroCabinas()},{self.getNroEmpleados()} \n"
        for emp in self.__empleados:
            r += f"{emp},sueldo: {self.__sueldos[i]} Bs,edad: {self.__edades[i]} años\n"
            i += 1
        return r

    @multimethod
    def mostrar(self, x: str):
        if x.lower() == "edad":
            max_edad = max(self.__edades)
            print("Empleado con la mayor edad:")
            i = 0
            for edad in self.__edades:
                if edad == max_edad:
                    print(f"{self.__empleados[i]} - {edad} años")
                i += 1

    @multimethod
    def mostrar(self):
        max_sueldo = max(self.__sueldos)
        print("Empleado con el mayor sueldo:")
        i = 0
        for sueldo in self.__sueldos:
            if sueldo == max_sueldo:
                print(f"{self.__empleados[i]} - {sueldo} Bs")
            i += 1






# main
obj1 = LineaTeléferico("Rojo","Estación Central, Estación Cementerio, Estación 16 de Julio",20,4)
obj2 = LineaTeléferico.desde_otro(50,1)

empleado1 = {
    "Nombre":"pedro",
    "ApPaterno":"Rojas",
    "ApMaterno":"Luna"
}
empleado2 = {
    "Nombre":"Lucy",
    "ApPaterno":"Sosa",
    "ApMaterno":"Rios"
}
empleado3 = {
    "Nombre":"Ana",
    "ApPaterno":"Perez",
    "ApMaterno":"Rojas"
}
empleado4 = {
    "Nombre":"Saul",
    "ApPaterno":"Arce",
    "ApMaterno":"Calle"
}
edad1 = 35
edad2 = 43
edad3 = 26
edad4 = 29

sueldo1 = 2500
sueldo2 = 3250
sueldo3 = 2700
sueldo4 = 2500


obj1.addEmpleados(empleado1)
obj1.addEmpleados(empleado2)
obj1.addEmpleados(empleado3)
obj1.addEmpleados(empleado4)

obj1.addEdad(edad1)
obj1.addEdad(edad2)
obj1.addEdad(edad3)
obj1.addEdad(edad4)

obj1.addSueldo(sueldo1)
obj1.addSueldo(sueldo2)
obj1.addSueldo(sueldo3)
obj1.addSueldo(sueldo4)

obj1.delEmpleado("Rojas")

print(obj1)

print(obj1 + ("Saul",obj2))

obj1.mostrar("edad")
obj1.mostrar()
