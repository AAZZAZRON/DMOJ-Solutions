//
// Created by Aaron Zhu on 2022-09-02.
//

#include "bits/stdc++.h"
using namespace std;

inline int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    int n; cin >> n;
    int ans = 0;
    for (int i = 0; i < n; i += 1) {
        int tmp; cin >> tmp; tmp = abs(tmp);
        if (tmp != 0) {
            if (ans == 0) ans = tmp;
            else ans = gcd(ans, tmp);
        }
    }
    cout << ans << '\n';

    return 0;
}
