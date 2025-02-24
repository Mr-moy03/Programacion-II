package Linea_Circulo;


import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class Main extends JPanel {
    // Configuración de pantalla
    public static final int WIDTH = 800;
    public static final int HEIGHT = 600;

    // Colores
    public static final Color WHITE = new Color(255, 255, 255);
    public static final Color BLACK = new Color(0, 0, 0);
    public static final Color RED = new Color(255, 0, 0);
    public static final Color BLUE = new Color(0, 0, 255);
    public static final Color COLOR1 = new Color(255, 255, 255);
    public static final Color COLOR2 = new Color(18, 161, 164);

    // Puntos y figuras
    public Punto p1, p2;
    public Linea linea;
    public Circulo circulo;

    // Texto
    public String texto1, texto2, texto3;

    public Main() {
        // Crear puntos aleatorios
        Random random = new Random();
        p1 = new Punto(random.nextInt(201) - 100, random.nextInt(201) - 100);
        p2 = new Punto(random.nextInt(201) - 100, random.nextInt(201) - 100);

        // Crear línea y círculo
        linea = new Linea(p1, p2);
        circulo = new Circulo(p1, p1.coordPolares()[0]);

        // Generar texto
        texto1 = String.format("p1 = %s", p1);
        texto2 = String.format("p2 = %s", p2);
        texto3 = String.format("radio: %.2f, angulo: %.2f", p1.coordPolares()[0], p1.coordPolares()[1]);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        // Fondo negro
        setBackground(BLACK);

        // Dibujar línea
        linea.dibujaLinea(g2d);

        // Dibujar círculo
        circulo.dibujaCirculo(g2d);

        // Dibujar texto
        g2d.setColor(WHITE);
        g2d.drawString(texto1, 10, 20);
        g2d.drawString(texto2, 10, 40);
        g2d.drawString(texto3, 10, 60);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Practica 2");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(WIDTH, HEIGHT);
        frame.add(new Main());
        frame.setVisible(true);
    }
}

// Clase Punto
class Punto {
    public double x, y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double[] coordCartesianas() {
        return new double[]{x, y};
    }

    public double[] coordPolares() {
        double radio = Math.sqrt(x * x + y * y);
        double angulo = Math.toDegrees(Math.atan2(y, x));
        return new double[]{radio, angulo};
    }

    public int[] transformar() {
        // Transformar coordenadas cartesianas a las de la pantalla (invertir Y)
        int xTransformado = (int) (x + Main.WIDTH / 2);
        int yTransformado = (int) (Main.HEIGHT / 2 - y);
        return new int[]{xTransformado, yTransformado};
    }

    @Override
    public String toString() {
        return String.format("(%.2f, %.2f)", x, y);
    }
}

// Clase Linea
class Linea {
    public Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public void dibujaLinea(Graphics2D g2d) {
        int[] punto1 = p1.transformar();
        int[] punto2 = p2.transformar();
        g2d.setColor(Main.COLOR2);
        g2d.setStroke(new BasicStroke(2));
        g2d.drawLine(punto1[0], punto1[1], punto2[0], punto2[1]);
    }
}

// Clase Circulo
class Circulo {
    public Punto centro;
    public double radio;

    public Circulo(Punto centro, double radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public void dibujaCirculo(Graphics2D g2d) {
        int[] centroTransformado = centro.transformar();
        g2d.setColor(Main.COLOR1);
        g2d.setStroke(new BasicStroke(2));
        g2d.drawOval(centroTransformado[0] - (int) radio, centroTransformado[1] - (int) radio,
                (int) (2 * radio), (int) (2 * radio));
    }
}

