//
// Created by Aaron Zhu on 2022-01-25.
//

#include "../../bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define si set<int>
#define usi unordered_set<int>
#define mii map<int, int>
#define umii unordered_map<int, int>
#define pb push_back
#define mp make_pair
#define printArr(a, len) for(int orzdaniel = 0; orzdaniel < (len); orzdaniel += 1) cout << (a)[orzdaniel] << ' '; cout << '\n';
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 1000000005
#define LLINF 1000000000000000005LL
#define MOD 1000000007
#define MAX 500001

int n, a, b;
vi conn[MAX];
pii fM[MAX], sM[MAX];
bool vis[MAX];
int down[MAX], up[MAX];

inline int dfsDown(int node) {
    vis[node] = 1;
    for (int nex : conn[node]) {
        if (!vis[nex]) {
            int t = dfsDown(nex);
            if (t > fM[node].first) {
                sM[node] = fM[node];
                fM[node] = {t, nex};
            } else if (t > sM[node].first) {
                sM[node] = {t, nex};
            }
            down[node] = max(down[node], t);
        }
    }
    return down[node] += 1;
}

inline int dfsUp(int node, int par, int par2) {
    vis[node] = 1;
    up[node] = up[par];
    if (fM[par].second != node) {
        up[node] = max(up[node], fM[par].first + 1);
    } else {
        up[node] = max(up[node], sM[par].first + 1);
    }
    up[node] += 1;
    for (int nex : conn[node]) {
        if (!vis[nex]) {
            dfsUp(nex, node, par);
        }
    }
    return up[node];
}

int main() {
    boost();
    cin >> n;
    for (int i = 0; i < n - 1; i += 1) {
        cin >> a >> b;
        conn[a].pb(b);
        conn[b].pb(a);
    }

    memset(vis, 0, n + 1);
    dfsDown(1);
    memset(vis, 0, n + 1);
    vis[1] = 1;
    up[1] = 1;
    for (int i : conn[1]) dfsUp(i, 1, 1);
//    printArr(down, n + 1);
//    printArr(up, n + 1);
    for (int i = 1; i <= n; i += 1) {
        cout << max(down[i], up[i]) << "\n";
    }
    return 0;
}

/*
 * Stuck?
 * Did you try:
 * Integer overflow?
 * Edge cases? (n = 1)
 * Printing output?
 * Organizing your code?
 * Another approach?
 *
 * Still Stuck? Ask Daniel!
 */