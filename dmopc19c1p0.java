package Completed;

import java.io.*;
import java.util.*;

public class dmopc19c1p0 {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        long minimum = 1000000000;
        long maximum = -1000000000;
        for (int i = 0; i < n; i += 1) {
            int t = scan.nextInt();
            maximum = Math.max(maximum, t);
            minimum = Math.min(minimum, t);
        }
        System.out.println(maximum - minimum);
    }
}
