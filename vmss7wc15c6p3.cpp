//
// Created by Aaron Zhu on 2023-02-01.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
#define MAX 400001

vector<int> conn[MAX];
int val[MAX];
int maxV = -999999999;

//#define cin IN
//#define cout OUT

//ifstream IN;
//ofstream OUT;

inline int dfs(int node, int prev) {
    int s = val[node];
    for (int nex : conn[node]) {
        if (nex != prev) s += dfs(nex, node);
    }
    maxV = max(maxV, s);
    return s;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    int n; cin >> n;
    for (int i = 0; i < n - 1; i += 1) {
        int a, b; cin >> a >> b;
        conn[a].push_back(b);
        conn[b].push_back(a);
    }

    for (int i = 1; i <= n; i += 1) cin >> val[i];
    dfs(1, -1);
    cout << maxV << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}