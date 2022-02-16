//
// Created by Aaron Zhu on 2022-01-24.
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
#define MAX 100001

int n, m, s, a, b, st;
vi conn[MAX];
bool pho[MAX];
queue<int> q;
bool vis[MAX];
int d = 0;

inline int diameter(int node, int prev) {
    vector<int> vals = {0, 0};
    for (int nex : conn[node]) {
        if (nex != prev) vals.pb(diameter(nex, node));
    }
    sort(vals.begin(), vals.end());
    d = max(d, vals[vals.size() - 1] + vals[vals.size() - 2]);
    return 1 + max(vals[vals.size() - 1], vals[vals.size() - 2]);
}

int main() {
    boost();
    cin >> n >> m;
    s = n - 1;
    while (m--) {
        cin >> a;
        pho[a] = 1;
        st = a;
    }
    for (int i = 0; i < n - 1; i += 1) {
        cin >> a >> b;
        conn[a].pb(b);
        conn[b].pb(a);
    }
    for (int i = 0; i < n; i += 1) {
        if (conn[i].size() == 1) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int node = q.front(); q.pop();
        if (vis[node]) continue;
        for (int nex : conn[node]) {
            if (vis[nex]) {
                conn[node].erase(remove(conn[node].begin(), conn[node].end(), nex), conn[node].end());
            }
        }
        if (conn[node].size() == 1 && !pho[node]) {
            s -= 1;
            vis[node] = 1;
            q.push(conn[node][0]);
            conn[node].erase(remove(conn[node].begin(), conn[node].end(), conn[node][0]), conn[node].end());
        }
    }
    diameter(st, -1);
    cout << s * 2 - d << "\n";

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