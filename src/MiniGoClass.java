/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  io
 */
public class MiniGoClass {
    public static void main(String[] args) {
        String[][] a = new String[][]{{null}, {"food"}};
        a[0][0] = "no";
        io.putString((String)a[0][0].concat(" ").concat(a[1][0]).concat(" I feel hungry"));
    }
}
