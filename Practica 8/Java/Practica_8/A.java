//A.java
package Practica_8;
class A {
    public int x;
    public int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        x += 1;
        z += 1;
    }

    public void incrementaZ() {
        z += 1;
    }
}