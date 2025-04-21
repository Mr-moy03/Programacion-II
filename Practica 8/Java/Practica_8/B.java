//B.java
package Practica_8;
class B implements IncrementaYZ {
    int y;
    int z;

    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y += 1;
        z += 1;
    }

    public void incrementaZ() {
        z += 1;
    }
}
