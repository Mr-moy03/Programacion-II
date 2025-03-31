package Ejercicio_1;

public class AlgebraVectorial {
    private double x;
    private double y;
    private double z;

    public AlgebraVectorial() {
        this(0, 0, 0);
    }
    public AlgebraVectorial(double x, double y) {
        this(x, y, 0);
    }
    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public AlgebraVectorial suma(AlgebraVectorial otro) {
        return new AlgebraVectorial(this.x + otro.x, this.y + otro.y, this.z + otro.z);
    }
    public AlgebraVectorial resta(AlgebraVectorial otro) {
        return new AlgebraVectorial(this.x - otro.x,this.y - otro.y,this.z - otro.z
        );
    }
    public double productoPunto(AlgebraVectorial otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }
    public AlgebraVectorial productoCruz(AlgebraVectorial otro) {
        double nuevoX = this.y * otro.z - this.z * otro.y;
        double nuevoY = this.z * otro.x - this.x * otro.z;
        double nuevoZ = this.x * otro.y - this.y * otro.x;
        return new AlgebraVectorial(nuevoX, nuevoY, nuevoZ);
    }
    public double norma() {
        return Math.sqrt(x*x + y*y + z*z);
    }

    public boolean perpendicular(AlgebraVectorial otro) {
        return Math.abs(this.productoPunto(otro)) < 1e-10;
    }
    public boolean perpendicular(AlgebraVectorial otro, int metodo) {
        switch(metodo) {
            case 1: // |a + b| = |a - b|
                AlgebraVectorial suma = this.suma(otro);
                AlgebraVectorial resta = this.resta(otro);
                return Math.abs(suma.norma() - resta.norma()) < 1e-10;
            case 2: // |a - b| = |b - a|
                AlgebraVectorial resta1 = this.resta(otro);
                AlgebraVectorial resta2 = otro.resta(this);
                return Math.abs(resta1.norma() - resta2.norma()) < 1e-10;
            case 3: // a · b = 0
                return Math.abs(this.productoPunto(otro)) < 1e-10;
            case 4: // |a + b|² = |a|² + |b|²
                AlgebraVectorial suma4 = this.suma(otro);
                return Math.abs(suma4.norma() * suma4.norma() - (this.norma() * this.norma() + otro.norma()*otro.norma())) < 1e-10;
            default:
                throw new IllegalArgumentException("Método no válido para perpendicularidad");
        }
    }
    public boolean paralelo(AlgebraVectorial otro) {
        return this.productoCruz(otro).norma() < 1e-10;
    }
    public boolean paralelo(AlgebraVectorial otro, int metodo) {
        switch(metodo) {
            case 1: // a = r*b
                if (otro.x == 0 || otro.y == 0 || otro.z == 0) {
                    return false;
                }
                double r = this.x / otro.x;
                return (Math.abs(this.y / otro.y - r) < 1e-10 && Math.abs(this.z / otro.z - r) < 1e-10);
            case 2: // a × b = 0
                return this.productoCruz(otro).norma() < 1e-10;
            default:
                return false;
        }
    }
    public AlgebraVectorial proyeccion(AlgebraVectorial otro) {
        double productoPunto = this.productoPunto(otro);
        double normaBCuadrado = otro.norma() * otro.norma();
        if (normaBCuadrado == 0) {
            return new AlgebraVectorial();
        }
        double factor = productoPunto / normaBCuadrado;
        return new AlgebraVectorial(otro.x * factor,otro.y * factor,otro.z * factor);
    }
    public double componente(AlgebraVectorial otro) {
        double productoPunto = this.productoPunto(otro);
        double normaB = otro.norma();
        if (normaB == 0) {
            return 0;
        }
        return productoPunto / normaB;
    }
    @Override
    public String toString() {
        return String.format("Vector(%.2f, %.2f, %.2f)", x, y, z);
    }
    // Main
    public static void main(String[] args) {
        AlgebraVectorial v1 = new AlgebraVectorial(1, 0, 0);
        AlgebraVectorial v2 = new AlgebraVectorial(0, 1, 0);
        AlgebraVectorial v3 = new AlgebraVectorial(2, 0, 0);

        System.out.println("Vectores:");
        System.out.println("v1 = " + v1);
        System.out.println("v2 = " + v2);
        System.out.println("v3 = " + v3);

        System.out.println("\nPruebas de perpendicularidad:");
        System.out.println("v1 perpendicular a v2 (Default): " + v1.perpendicular(v2));
        System.out.println("v1 perpendicular a v2 (método 1): " + v1.perpendicular(v2, 1));
        System.out.println("v1 perpendicular a v2 (método 2): " + v1.perpendicular(v2, 2));
        System.out.println("v1 perpendicular a v2 (método 3): " + v1.perpendicular(v2, 3));
        System.out.println("v1 perpendicular a v2 (método 4): " + v1.perpendicular(v2, 4));

        System.out.println("\nPruebas de paralelismo:");
        System.out.println("v1 paralelo a v3 (método por defecto): " + v1.paralelo(v3));
        System.out.println("v1 paralelo a v3 (método 1): " + v1.paralelo(v3, 1));
        System.out.println("v1 paralelo a v3 (método 2): " + v1.paralelo(v3, 2));

        System.out.println("\nProyección de v1 sobre v2:");
        System.out.println(v1.proyeccion(v2));

        System.out.println("\nComponente de v1 en v2:");
        System.out.println(v1.componente(v2));
    }
}
