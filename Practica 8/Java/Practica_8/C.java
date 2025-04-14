//C.java
package Practica_8;

class C {
    A aParte;
    B bParte;

    public C(int x, int y, int z) {
        aParte = new A(x, z);
        bParte = new B(y, z);
    }

    public void incrementaXYZ() {
        aParte.x += 1;
        bParte.y += 1;
        aParte.z += 1;
        bParte.z = aParte.z; // sincronizamos z
    }

    public void incrementaZ() {
        aParte.incrementaZ();
        bParte.z = aParte.z;
    }

    public void incrementaXZ() {
        aParte.incrementaXZ();
        bParte.z = aParte.z;
    }

    public void incrementaYZ() {
        bParte.incrementaYZ();
        aParte.z = bParte.z;
    }

    @Override
    public String toString() {
        return "x:" + aParte.x + ", y:" + bParte.y + ", z:" + aParte.z;
    }
}