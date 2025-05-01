/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  io
 */
public class MiniGoClass {
    public static void main(String[] args) {
        int[][] arr = new int[][]{{1, 2}, {3, 4}};
        int i = 0;
        while ((i < 2 ? 1 : 0) > 0) {
            int j = 0;
            while ((j < 2 ? 1 : 0) > 0) {
                io.putIntLn((int)arr[i][j]);
                ++j;
            }
            ++i;
        }
    }
}
