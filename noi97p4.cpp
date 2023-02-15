//
// Created by Aaron Zhu on 2022-09-16.
//

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
#define MAX 20001
// #define cin IN
//#define cout OUT

int arr[MAX];
ifstream IN;
ofstream OUT;

signed main() {
    cin.tie(); cin.sync_with_stdio(0);

    IN.open("../in.txt");
    OUT.open("../out.txt");

    int n, m; cin >> m >> n; n -= 1;
    for (int i = 0; i < MAX; i += 1) arr[i] = -200;

    for (int i = 0; i < m; i += 1) {
        for (int j = 0; j < n; j += 1) {
            int t; cin >> t; arr[j] = max(arr[j], t);
        }
    }
    int gMax = -200;
    int lMax = 0;
    for (int i = 0; i < n; i += 1) {
        lMax = max(arr[i], lMax + arr[i]);
        gMax = max(gMax, lMax);
    }

//    for (int i = 0; i < n; i += 1) cout << arr[i] << ' ';
//    cout << '\n';

    cout << gMax << '\n';

    IN.close();
    OUT.close();

    return 0;
}