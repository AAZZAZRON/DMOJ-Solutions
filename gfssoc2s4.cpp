//
// Created by Aaron Zhu on 2021-10-17.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 500001

struct val {
    int n, c, gf;
    bool operator<(const val &one) const {
        return c > one.c;
    }
};

int n, m, a, b, c;
int minD[MAX][2];
bool vis[MAX][2];
vector<pii> reg[MAX], gf[MAX];
priority_queue<val> pq;

int main() {
    boost();
    cin >> n >> m;
    for (int i = 0; i < m; i += 1) {
        cin >> a >> b >> c;
        reg[a].pb(mp(b, c));
    }
    cin >> m;
    for (int i = 0; i < m; i += 1) {
        cin >> a >> b >> c;
        gf[a].pb(mp(b, c));
    }
    for (int i = 0; i < MAX; i += 1) minD[i][0] = minD[i][1] = INF;
    pq.push((val) {1, 0, 0});
    minD[1][0] = minD[1][1] = 0;

    while (!pq.empty()) {
        int node = pq.top().n;
        int cost = pq.top().c;
        int hasGf = pq.top().gf;
        pq.pop();
        if (minD[node][hasGf] != cost) continue;
        for (pii tmp : reg[node]) {
            if (!vis[tmp.first][hasGf] && minD[node][hasGf] + tmp.second < minD[tmp.first][hasGf]) {
                minD[tmp.first][hasGf] = minD[node][hasGf] + tmp.second;
                pq.push((val) {tmp.first, minD[tmp.first][hasGf], hasGf});
            }
        }
        if (!hasGf) {
            for (pii tmp : gf[node]) {
                if (!vis[tmp.first][1] && minD[node][0] + tmp.second < minD[tmp.first][1]) {
                    minD[tmp.first][1] = minD[node][0] + tmp.second;
                    pq.push((val) {tmp.first, minD[tmp.first][1], 1});
                }
            }
        }
        vis[node][hasGf] = 1;
    }

    int ans = min(minD[n][0], minD[n][1]);
    if (ans == INF) cout << "-1\n";
    else cout << ans << "\n";

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
