//
// Created by Aaron Zhu on 2022-08-28.
//

#include "bits/stdc++.h"
using namespace std;

#define MAX 31
double ans[MAX];
signed main() {
    cin.tie(0); cin.sync_with_stdio(0);

    int n, m; cin >> n >> m;
    double tot = 1;
    for (int i = 0; i < m; i += 1) {
        int a, p; cin >> a >> p;
        double tmp = p * tot / 100.0;
        ans[a] += tmp;
        tot -= tmp;
    }
    for (int i = 1; i <= n; i += 1) cout << ans[i] << '\n';

    return 0;
}
