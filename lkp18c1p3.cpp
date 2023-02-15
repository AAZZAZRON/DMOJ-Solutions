//
// Created by Aaron Zhu on 2023-01-31.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
#define int long long
using namespace std;

//#define cin IN
//#define cout OUT

//ifstream IN;
//ofstream OUT;

int arr[10], test[10];

inline bool synthDiv(int n, int zero) {
    zero *= -1;
    int v = arr[0];
    test[0] = v;
    for (int i = 1; i <= n; i += 1) {
        v = arr[i] - v * zero;
        test[i] = v;
    }
    if (v == 0) {
        for (int i = 0; i < 10; i += 1) arr[i] = test[i];
        return 1;
    }
    return 0;
}

inline void solve(int n) {
    int ct = n;
    for (int zero = -150; zero <= 150; zero += 1) {
        if (ct == 0) continue;
        if (zero == 0) {
            while (arr[ct] == 0) {
                ct -= 1;
                cout << "0 ";
            }
            continue;
        }
        while (synthDiv(n, zero)) {
            ct -= 1;
            cout << zero << ' ';
        }
    }
    cout << '\n';
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    int t; cin >> t;
    while (t--) {
        int deg; cin >> deg;
        for (int i = 0; i <= deg; i += 1) {
            int tmp; cin >> tmp;
            arr[i] = tmp;
        }
        //cout << deg << '\n';
        //printArr(arr, deg + 1);
        solve(deg);
    }

    //IN.close();
    //OUT.close();
    return 0;
}
