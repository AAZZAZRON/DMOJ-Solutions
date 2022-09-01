//
// Created by Aaron Zhu on 2022-03-12.
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
#define MAX 200001
#define int ll

struct el {
    int e, o;
};

int n, a, b, c;
int tot, m = LLINF;
vii conn[MAX];
el p[MAX];

inline void dfs(int node, int prev) {
    for (pii tmp : conn[node]) {
        if (tmp.first != prev) {
            dfs(tmp.first, node);
            if (tmp.second == 0) {
                p[node].e += p[tmp.first].e;
                p[node].o += p[tmp.first].o;
                p[node].e += 1;
            } else {
                p[node].e += p[tmp.first].o;
                p[node].o += p[tmp.first].e;
                p[node].o += 1;
            }
        }
    }
}

inline void pathify(int even, int odd) {
    a = even * odd + odd;
    b = tot - a;
    m = min(m, abs(b - a));
}

inline void calc(int node, int prev, int dep) {
    for (pii tmp : conn[node]) {
        if (tmp.first != prev) {
            int even, odd;
            if ((tmp.second + dep) % 2 == 0) {
                even = p[1].e - p[tmp.first].e + p[tmp.first].o;
                odd = p[1].o - p[tmp.first].o + p[tmp.first].e;
                even -= 1; odd += 1;
            } else {
                even = p[1].e - p[tmp.first].o + p[tmp.first].e;
                odd = p[1].o - p[tmp.first].e + p[tmp.first].o;
                even += 1; odd -= 1;
            }
            pathify(even, odd);
            calc(tmp.first, node, (dep + tmp.second) % 2);
        }
    }
}

signed main() {
    boost();
    cin >> n;
    tot = (n * (n - 1)) / 2;
    for (int i = 0; i < n - 1; i += 1) {
        cin >> a >> b >> c;
        conn[a].pb({b, c % 2});
        conn[b].pb({a, c % 2});
    }

    dfs(1, 0);

    pathify(p[1].e, p[1].o);
    calc(1, 0, 0);
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