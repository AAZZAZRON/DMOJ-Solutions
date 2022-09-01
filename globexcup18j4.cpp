//
// Created by Aaron Zhu on 2022-08-04.
//

#include "bits/stdc++.h"
using namespace std;
#define MOD 1000000007
#define int long long
int a, b, c, d, e, N;

inline int f(int n) {
    if (n == 0) return e;
    int one = (a * f(n / b)) % MOD;
    int two = (c * f(n / d)) % MOD;
    return (one + two) % MOD;
}

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    cin >> a >> b >> c >> d >> e >> N;
    cout << f(N) % MOD << '\n';

    return 0;
}
