//
// Created by Aaron Zhu on 2023-02-05.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
//ifstream IN;
//ofstream OUT;
#define MAX 210
#define OFFSET 100

struct Edge {
    int from, to, cap;
};

vector<Edge> conn[MAX];
int capacity[MAX][MAX];
int vis[MAX];
int source = 205; int sink = 206;
int girls[MAX];
Edge pre[MAX];
int cnt = 0;

inline int bfs() {
    memset(vis, 0, sizeof vis);
    queue<int> q;
    vis[source] = 1;
    q.push(source);
    pre[source] = {-1, -1, -1};
    while (!q.empty()) {
        int node = q.front(); q.pop();
        if (node == sink) return 1;
        for (Edge edge : conn[node]) {
            int cap = edge.cap - capacity[edge.from][edge.to];
            if (cap > 0 && !vis[edge.to]) {
                vis[edge.to] = 1;
                pre[edge.to] = edge;
                q.push(edge.to);
            }
        }
    }
    return 0;
}

inline int flow() {
    int maxFlow = 0;
    while (bfs()) {
        int bottleneck = INT32_MAX;
        for (Edge edge = pre[sink]; edge.to != -1; edge = pre[edge.from]) {
            bottleneck = min(bottleneck, edge.cap - capacity[edge.from][edge.to]);
        }
        for (Edge edge = pre[sink]; edge.to != -1; edge = pre[edge.from]) {
            capacity[edge.from][edge.to] += bottleneck;
            capacity[edge.to][edge.from] -= bottleneck;
        }
        maxFlow += bottleneck;
    }
    return maxFlow;
}


signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");
    int n, m; cin >> n >> m;
    for (int i = 1; i <= n; i += 1) {
        conn[source].push_back({source, i, 1});
        conn[i].push_back({i, source, 0});
        int ct; cin >> ct;
        for (int j = 0; j < ct; j += 1) {
            int g; cin >> g;
            if (i == 1) {
                cnt += 1;
                girls[g] = 1;
                conn[OFFSET + g].push_back({OFFSET + g, sink, 1});
                conn[sink].push_back({sink, OFFSET + g, 0});
                continue;
            }
            if (girls[g]) {
                conn[i].push_back({i, OFFSET + g, 1});
                conn[OFFSET + g].push_back({OFFSET + g, i, 0});
            }
        }
    }

    cout << cnt - flow() << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}