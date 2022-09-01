//
// Created by Aaron Zhu on 2022-08-01.
//

#include "bits/stdc++.h"
using namespace std;
#define MAX 100001
#define int long long
int arr[MAX];
unordered_map<int, int> mods;
signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    int n, m; cin >> n >> m;
    for (int i = 0; i < n; i += 1) cin >> arr[i];
    int ct = 0;
    int ans = 0;
    for (int i = 0; i < n; i += 1) {
        ct = (ct + arr[i]) % m;
        if (ct == 0) ans += 1;
        if (mods.find(ct) != mods.end()) ans += mods[ct];

        if (mods.find(ct) != mods.end()) mods[ct] += 1;
        else mods[ct] = 1;
    }
    cout << ans << '\n';
    return 0;
}
