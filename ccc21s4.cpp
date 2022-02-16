//
// Created by Aaron Zhu on 2022-01-08.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 1000000
#define MOD 1000000007
#define MAX 200001

int n, w, d, one, two;
vector<int> conn[MAX];
int minDist[MAX];
int train[MAX];
priority_queue<pii> q;
priority_queue<pii> values;
bool vis[MAX];

inline void dijkstra() {
    for (int i = 0; i < MAX; i += 1) minDist[i] = INF;
    minDist[n] = 0;
    q.push(make_pair(0, n));
    while (!q.empty()) {
        int cost = -q.top().first;
        int node = q.top().second; q.pop();
        if (minDist[node] != cost) continue;
        for (int nex : conn[node]) {
            if (!vis[nex] && cost + 1 < minDist[nex]) {
                minDist[nex] = cost + 1;
                q.push(make_pair(-minDist[nex], nex));
            }
        }
        vis[node] = 1;
    }
}


int main() {
    boost();
    cin >> n >> w >> d;
    for (int i = 0; i < w; i += 1) {
        cin >> one >> two;
        conn[two].push_back(one);
    }
    dijkstra();
    for (int i = 0; i < n; i += 1) {
        cin >> one;
        train[i] = one;
        values.push(make_pair(-i - minDist[one], one));
    }
    for (int i = 0; i < d; i += 1) {
        cin >> one >> two;
        one--; two--;
        swap(train[one], train[two]);
        values.push(make_pair(-one - minDist[train[one]], train[one]));
        values.push(make_pair(-two - minDist[train[two]], train[two]));
        while (true) {
            int v = -values.top().first;
            int ind = values.top().second;
            if (train[v - minDist[ind]] == ind) {
                cout << v << "\n";
                break;
            }
            values.pop();
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
