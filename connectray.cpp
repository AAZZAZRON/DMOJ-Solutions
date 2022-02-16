//
// Created by Aaron Zhu on 2022-01-20.
//

#include "bits/stdc++.h"
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
#define MAX 400001

int n, m, q, a, b;
char ins;
bool vis[MAX];
vi conn[MAX];
queue<int> qu;
int main() {
    boost();
    cin >> n >> m >> q;
    for (int i = 0; i < m; i += 1) {
        cin >> a >> b;
        conn[a].pb(b);
    }
    vis[1] = 1;
    qu.push(1);
    while (!qu.empty()) {
        int node = qu.front(); qu.pop();
        for (int nex : conn[node]) {
            if (!vis[nex]) {
                vis[nex] = 1;
                qu.push(nex);
            }
        }
        conn[node] = {};
    }
    for (int i = 0; i < q; i += 1) {
        cin >> ins;
        if (ins == '?') {
            cin >> a;
            cout << (vis[a] ? "YES" : "NO") << "\n";
        } else {
            cin >> a >> b;
            if (!vis[a] || (vis[a] && !vis[b])) conn[a].pb(b);
            if (vis[a] && !vis[b]) {
                qu.push(a);
                while (!qu.empty()) {
                    int node = qu.front(); qu.pop();
                    for (int nex : conn[node]) {
                        if (!vis[nex]) {
                            vis[nex] = 1;
                            qu.push(nex);
                        }
                    }
                    conn[node] = {};
                }
            }
        }
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