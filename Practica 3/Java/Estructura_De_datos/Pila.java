package Estructura_De_datos;

public class Pila {
    // atributos
    private long[] arreglo;
    private int top;
    private int n;

    // metodos
    public Pila(int n){
        this.arreglo = new long[n];
        this.top = -1;
        this.n = n;
    }
    public void push(int e){
        if (isFull()){
            System.out.println("Pila llena");
        }
        else{
            top++;
            arreglo[top] = e;
        }
    }
    public long pop(){
        if (isEmpty()){
            System.out.println("Pila vacia");
            return -1;
        }
        else{
            long e = arreglo[top];
            top--;
            return (int) e;
        }
    }
    public long peek(){
        if (isEmpty()){
            System.out.println("Pila vacia");
        }
        return (int)arreglo[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args){
        Pila pila = new Pila(10);
        pila.push(10);
        pila.push(20);
        pila.push(30);
        System.out.println(pila.peek());
        System.out.println("pop() = "+pila.pop());
        System.out.println(+pila.peek());
        System.out.println("pop() = "+pila.pop());
        System.out.println("pop() = "+pila.pop());
    }
}
