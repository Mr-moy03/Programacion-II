package PracticaN1;

public class Punto {
    public float x;
    public float y;

    // Constructor que recibe coordenadas x e y como float
    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    // Método que retorna un array con coordenadas cartesianas
    public float[] coord_cartesianas() {
        return new float[]{x, y};
    }

    // Método que retorna un array con coordenadas polares
    public double[] coord_polares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan2(y, x); // Ángulo en radianes
        return new double[]{r, Math.toDegrees(theta)};
    }

    // Método toString para mostrar las coordenadas de forma legible
    public String toString() {
        return "Punto: (" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        // Creación de un punto
        Punto p = new Punto(3.0f, 4.0f);

        // Obtener y mostrar coordenadas cartesianas
        float[] cartesianas = p.coord_cartesianas();
        System.out.println("Coordenadas cartesianas: (" + cartesianas[0] + ", " + cartesianas[1] + ")");

        // Obtener y mostrar coordenadas polares
        double[] polares = p.coord_polares();
        System.out.println("Coordenadas polares: (r: " + polares[0] + ", θ: " + polares[1] + "°)");
    }
}
