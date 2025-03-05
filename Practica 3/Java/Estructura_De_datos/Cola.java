package Estructura_De_datos;

public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int size;

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.size = 0;
    }

    public void insert(long e) {
        if (isFull()) {
            System.out.println("Cola llena");
        }
        fin = (fin + 1) % n;
        arreglo[fin] = e;
        size++;
    }

    public long remove() {
        if (isEmpty()) {
            System.out.println("Cola vacía");
        }
        long elemento = arreglo[inicio];
        inicio = (inicio + 1) % n;
        size--;
        return elemento;
    }

    public long peek() {
        if (isEmpty()) {
            System.out.println("Cola vacía");
        }
        return arreglo[inicio];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == n;
    }

    public int size() {
        return size;
    }

    public static void main(String[] args){
        Cola cola = new Cola(10);
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);
        System.out.println(cola.peek());
        System.out.println("remove() = "+cola.remove());
        System.out.println(cola.peek());
        System.out.println("remove() = "+cola.remove());
        System.out.println("remove() = "+cola.remove());
        System.out.println("remove() = "+cola.remove());
    }
}
