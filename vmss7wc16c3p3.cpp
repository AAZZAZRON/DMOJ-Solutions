//
// Created by Aaron Zhu on 2022-01-20.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
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
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 2001

int n, m, st, q, a, b, c, t;
vector<pii> conn[MAX];
int minD[MAX];
bool vis[MAX];
priority_queue<pii> pq;
int main() {
    boost();
    cin >> n >> m >> st >> q;
    for (int i = 0; i < m; i += 1) {
        cin >> a >> b >> c;
        conn[a].pb(mp(b, c));
        conn[b].pb(mp(a, c));
    }
    pq.push(mp(0, st));
    for (int i = 0; i <= n; i += 1) minD[i] = INF;
    minD[st] = 0;
    while (!pq.empty()) {
        int node = pq.top().second;
        int cost = -pq.top().first;
        pq.pop();
        if (minD[node] != cost) continue;
        for (pii tmp : conn[node]) {
            if (!vis[tmp.first] && cost + tmp.second < minD[tmp.first]) {
                minD[tmp.first] = cost + tmp.second;
                pq.push(mp(-minD[tmp.first], tmp.first));
            }
        }
        vis[node] = 1;
    }
    for (int i = 0; i < q; i += 1) {
        cin >> t;
        cout << (minD[t] != INF ? minD[t] : -1) << "\n";
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
