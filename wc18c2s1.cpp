//
// Created by Aaron Zhu on 2022-09-16.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <fstream>
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
// #define cin IN
//#define cout OUT
#define MAX 1000001

ifstream IN;
ofstream OUT;

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    IN.open("../in.txt");
    OUT.open("../out.txt");

    int x, y; cin >> x >> y;
    int n, m, c; cin >> n >> m >> c;
    int x1 = 0, x2 = MAX, y1 = 0, y2 = MAX;

    for (int i = 0; i < n; i += 1) {
        int t; cin >> t;
        if (t < x) x1 = max(x1, t);
        else x2 = min(x2, t);
    }

    for (int i = 0; i < m; i += 1) {
        int t; cin >> t;
        if (t < y) y1 = max(y1, t);
        else y2 = min(y2, t);
    }

    for (int i = 0; i < c; i += 1) {
        int a, b; cin >> a >> b;
        if (x1 < a && a < x2 && y1 < b && b < y2) cout << "Y\n";
        else cout << "N\n";
    }

    IN.close();
    OUT.close();
    return 0;
}