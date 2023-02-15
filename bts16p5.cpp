//
// Created by Aaron Zhu on 2023-02-04.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
//ifstream IN;
//ofstream OUT;
#define pii pair<int, int>

struct el {
    int nex, w;
};

#define MAX 10001
int cherry[MAX];
vector<el> conn[MAX];
int n, C, K;
int ans = 0;

inline pii dfs(int node, int prev, int cut) {
    int cherries = cherry[node];
    int weight = cut;
    for (el nex : conn[node]) {
        if (nex.nex != prev) {
            pii tmp = dfs(nex.nex, node, nex.w);
            cherries += tmp.first;
            weight += tmp.second;
        }
    }
    if (node != 1 && cherries >= C && weight <= K) ans += 1;

    return {cherries, weight};
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");
    cin >> n >> C >> K;
    for (int i = 1; i <= n; i += 1) cin >> cherry[i];
    for (int i = 0; i < n - 1; i += 1) {
        int a, b, c; cin >> a >> b >> c;
        conn[a].push_back({b, c});
        conn[b].push_back({a, c});
    }

    dfs(1, -1, 0);
    cout << ans << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}