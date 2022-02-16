//
// Created by Aaron Zhu on 2022-01-28.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vii vector<pii>
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
#define MAX 100001

int n, t[MAX], cycle[MAX], mT[MAX];
vi conn[MAX];
bitset<MAX> bs;

inline int solve(int node, bitset<MAX> vis) {
    if (mT[node]) return mT[node];
    else if (cycle[node] || vis[node]) {
        cycle[node] = 1;
        mT[node] = INF;
        return INF;
    }
    int ct = 0;
    vis[node] = 1;
    for (int nex : conn[node]) ct = max(ct, solve(nex, vis));
    if (ct == INF) {
        mT[node] = INF;
        cycle[node] = 1;
        return INF;
    }
    return mT[node] = ct + t[node];
}

int main() {
    boost();
    cin >> n;
    for (int i = 1; i <= n; i += 1) {
        int q; cin >> q; t[i] = q;
        cin >> q;
        for (int j = 0; j < q; j += 1) {
            int w; cin >> w; conn[i].pb(w);
        }
    }
    int m = 0;
    for (int i = 1; i <= n; i += 1) {
        if (!mT[i] && !cycle[i]) {
            int x = solve(i, bs);
            if (x != INF) m = max(m, x);
        }
    }
    cout << m << '\n';
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