/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  io
 */
public class MiniGoClass {
    public static void main(String[] args) {
        Y y = new Y(12.0f, null, false, new X(1.2f, 4, true));
        y.setS("oke");
        float f = y.x.getX1();
        io.putFloat((float)y.x.getX1());
        io.putFloat((float)y.x.x1);
        io.putString((String)y.s);
    }
}
