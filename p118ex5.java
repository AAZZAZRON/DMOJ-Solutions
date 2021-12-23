package Completed;

import java.util.*;
import java.io.*;

public class p118ex5 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
        int n = Integer.parseInt(br.readLine());
        float[] arr = new float[n];
        float maximum = Integer.MIN_VALUE;
        for (int i = 0; i < n; i += 1) {
            float t = Float.parseFloat(br.readLine());
            maximum = Math.max(maximum, t);
            arr[i] = t;
        }
        for (int i = 0; i < n; i += 1) {
            if (arr[i] != maximum) System.out.printf("%.2f", arr[i]);
        }
        System.out.printf("%.2f", maximum);

    }
}
