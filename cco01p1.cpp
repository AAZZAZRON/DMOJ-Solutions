//
// Created by Aaron Zhu on 2022-08-01.
//

#include "bits/stdc++.h"
using namespace std;
#define MAX 105
int arr[MAX];
int vis[MAX];

inline int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

inline int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    int n; cin >> n;
    while (n != 0) {
        for (int i = 0; i < n; i += 1) {
            int a, b; cin >> a >> b;
            arr[a] = b;
        }
        memset(vis, 0, MAX);
        int ans = 1;
        int ct = 0;
        for (int i = 1; i <= n; i += 1) {
            if (!vis[i]) {
                ct = 0;
                int node = i;
                while (!vis[node]) {
                    vis[node] = 1;
                    node = arr[node];
                    ct += 1;
                }
                ans = lcm(ans, ct);
            }
        }
        cout << ans << '\n';
        cin >> n;
    }
    return 0;
}
