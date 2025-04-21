//C.java
package Practica_8;

class C extends A implements IncrementaYZ{
    B b;

    public C(int x, int y, int z) {
        super(x,z);
        b = new B(y, z);
    }

    public void incrementaXYZ() {
        x += 1;
        b.y += 1;
        z += 1;
        b.z = z;
    }

    @Override
    public void incrementaYZ() {
        b.incrementaYZ();
        this.z = b.z;
    }

    @Override
    public void incrementaZ() {
        super.incrementaZ();
        b.z = this.z;
    }

    @Override
    public String toString() {
        return "x:" + this.x + ", y:" + b.y + ", z:" + this.z;
    }
}
