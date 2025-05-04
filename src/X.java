/*
 * Decompiled with CFR 0.152.
 */
public class X {
    float x1;
    float x2;
    boolean isInit;

    public X(float f, float f2, boolean bl) {
        this.x1 = f;
        this.x2 = f2;
        this.isInit = bl;
    }

    public float getX1() {
        return this.x1;
    }

    public void setInit(boolean b) {
        this.isInit = true & b;
    }
}
