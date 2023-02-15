#include "bits/stdc++.h"
using namespace std;
#define MAX 1000001
#define int long long
int cost[MAX];

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    int n, m, k; cin >> n >> m >> k;
    k *= n;
    int ct = 0;
    for (int i = 0; i < n; i += 1) {
        int x, y; cin >> x >> y;
        ct += x;
        cost[y] += m - x;
    }

    int ans = 0;
    for (int i = 0; i < MAX && k >= ct; i += 1) {
        int freq = cost[i];
        ans += i * min(freq, k - ct);
        ct += freq;
    }

    cout << ans << '\n';


    return 0;
}
