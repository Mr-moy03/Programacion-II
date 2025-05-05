from multimethod import multimethod
class Ministerio:
    def __init__(self, nombre, direccion, nroEmpleados):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nroEmpleados = nroEmpleados
        self.__empleados = []
        self.__edades = []
        self.__sueldos = []

    def setNombre(self,nombre):
        self.__nombre = nombre
    def setDireccion(self,dire):
        self.__direccion = dire
    def setNroEmpleados(self,nroEmpleados):
        self.__nroEmpleados = nroEmpleados
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getNroEmpleados(self):
        return self.__nroEmpleados

    @classmethod
    def desde_otro(cls,nroEmpleados):
        return cls(nombre = "Morado",direccion = "Estacion el faro murillo",nroEmpleados = nroEmpleados)

    def addEmpleados(self,a):
        self.__empleados.append(a)
    def addEdad(self,a):
        self.__edades.append(a)
    def addSueldo(self,a):
        self.__sueldos.append(a)
    def delEmpleado(self,x):
        i = 0
        for edad in self.__edades:
            if x == edad:
                self.__edades.remove(edad)
                del self.__empleados[i]
                del self.__sueldos[i]
            i += 1

    def __add__(self, other):
        name, destino = other;i = 0
        for emp in self.__empleados:
            if emp['Nombre'] == name:
                destino.addEmpleados(emp);destino.addEdad(self.__edades[i]);destino.addSueldo(self.__sueldos[i])
                del self.__empleados[i];del self.__edades[i];del self.__sueldos[i]
                break
            i += 1
        return destino

    def __str__(self):
        r = "Datos: \n";i = 0
        r += f"{self.getNombre()},{self.getDireccion()},{self.getNroEmpleados()} \n"
        for emp in self.__empleados:
            r += f"{emp},sueldo: {self.__sueldos[i]} Bs,edad: {self.__edades[i]} años\n";i += 1
        return r

    @multimethod
    def mostrar(self, x: str):
        if x.lower() == "edad":
            min_edad = min(self.__edades)
            print("Empleado con la menor edad:")
            i = 0
            for edad in self.__edades:
                if edad == min_edad:
                    print(f"{self.__empleados[i]} - {edad} años")
                i += 1

    @multimethod
    def mostrar(self):
        min_sueldo = min(self.__sueldos)
        print("Empleado con el menor sueldo:")
        i = 0
        for sueldo in self.__sueldos:
            if sueldo == min_sueldo:
                print(f"{self.__empleados[i]} - {sueldo} Bs")
            i += 1






# main
obj1 = Ministerio("Rojo","Estación Central, Estación Cementerio, Estación 16 de Julio",4)
obj2 = Ministerio.desde_otro(7)

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


obj2.addEmpleados(empleado1)
obj2.addEmpleados(empleado2)
obj2.addEmpleados(empleado3)
obj2.addEmpleados(empleado4)

obj2.addEdad(edad1)
obj2.addEdad(edad2)
obj2.addEdad(edad3)
obj2.addEdad(edad4)

obj2.addSueldo(sueldo1)
obj2.addSueldo(sueldo2)
obj2.addSueldo(sueldo3)
obj2.addSueldo(sueldo4)

obj2.delEmpleado("Rojas")

print(obj2)

print(obj2 + ("Saul",obj1))

obj2.mostrar("edad")
obj2.mostrar()
