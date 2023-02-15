//
// Created by Aaron Zhu on 2022-09-02.
//

#include "bits/stdc++.h"
using namespace std;
#define MOD 1000000007
#define int long long

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);

    int n; cin >> n;
    int ct = 0;
    for (int i = 0; i < n; i += 1) {
        int tmp; cin >> tmp; ct = (ct + tmp) % MOD;
    }

    int p = 1;
    for (int i = 0; i < n - 1; i += 1) p = (p * 2) % MOD;

    cout << (ct * p) % MOD << '\n';

    return 0;
}
