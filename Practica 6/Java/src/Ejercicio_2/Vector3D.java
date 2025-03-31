package Ejercicio_2;

public class Vector3D {
    private double x;
    private double y;
    private double z;

    // Constructores
    public Vector3D() {
        this(0.0, 0.0, 0.0);
    }
    public Vector3D(double x, double y) {
        this(x, y, 0.0);
    }
    public Vector3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    // Operaciones básicas
    public Vector3D suma(Vector3D otro) {
        return new Vector3D(
                this.x + otro.x,
                this.y + otro.y,
                this.z + otro.z
        );
    }
    public Vector3D multiplicar(double escalar) {
        return new Vector3D(
                this.x * escalar,
                this.y * escalar,
                this.z * escalar
        );
    }
    public Vector3D resta(Vector3D otro) {
        return new Vector3D(
                this.x - otro.x,
                this.y - otro.y,
                this.z - otro.z
        );
    }
    public Vector3D dividir(double escalar) {
        return new Vector3D(this.x / escalar,this.y / escalar,this.z / escalar);
    }
    // Propiedades del vector
    public double longitud() {
        return Math.sqrt(x*x + y*y + z*z);
    }
    public Vector3D normalizar() {
        double longitud = this.longitud();
        if (longitud == 0) {
            return new Vector3D();
        }
        return this.dividir(longitud);
    }
    // Productos
    public double productoEscalar(Vector3D otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }
    public Vector3D productoVectorial(Vector3D otro) {
        return new Vector3D(this.y * otro.z - this.z * otro.y,this.z * otro.x - this.x * otro.z,this.x * otro.y - this.y * otro.x);
    }
    // Relaciones entre vectores
    public boolean esPerpendicular(Vector3D otro) {
        return esPerpendicular(otro, 1e-10);
    }
    public boolean esPerpendicular(Vector3D otro, double tolerancia) {
        return Math.abs(this.productoEscalar(otro)) < tolerancia;
    }
    // Proyección
    public Vector3D proyeccion(Vector3D otro) {
        double productoEscalar = this.productoEscalar(otro);
        double longitudCuadrado = otro.longitud() * otro.longitud();
        if (longitudCuadrado == 0) {
            return new Vector3D();
        }
        return otro.multiplicar(productoEscalar / longitudCuadrado);
    }
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }
    // Main
    public static void main(String[] args) {
        Vector3D a = new Vector3D(1, 2, 3);
        Vector3D b = new Vector3D(4, 5, 6);

        System.out.println("Operaciones básicas:");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("a + b = " + a.suma(b));
        System.out.println("a * 2 = " + a.multiplicar(2));
        System.out.println("a / 2 = " + a.dividir(2));

        System.out.println("\nPropiedades del vector:");
        System.out.println("Longitud de a: " + a.longitud());
        System.out.println("Vector normalizado de a: " + a.normalizar());

        System.out.println("\nProductos:");
        System.out.println("Producto escalar a·b: " + a.productoEscalar(b));
        System.out.println("Producto vectorial a×b: " + a.productoVectorial(b));

        System.out.println("\nRelaciones:");
        System.out.println("¿a y b son perpendiculares? " + a.esPerpendicular(b));

        System.out.println("\nProyección:");
        System.out.println("Proyección de a sobre b: " + a.proyeccion(b));
    }
}