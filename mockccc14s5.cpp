//
// Created by Aaron Zhu on 2023-02-04.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
//ifstream IN;
//ofstream OUT;
#define MAX 300
#define OFFSET 100
int black[MAX], white[MAX];

struct Edge {
    int from, to, cap;
    int capacity = 0;
};

vector<Edge> conn[MAX];
int capacity[MAX][MAX];
int vis[MAX];
int s = 201; int e = 202;

inline int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

inline int remainingCapacity(Edge edge) {
    return edge.cap - capacity[edge.from][edge.to];
}

inline int bfs() {
    queue<int> q;
    vis[s] = 1;
    q.push(s);
    Edge prev[MAX];
    prev[s] = {s, s, s};
    int found = 0;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        if (node == e) {
            found = 1;
            break;
        }
        for (Edge edge : conn[node]) {
            int cap = remainingCapacity(edge);
            if (cap > 0 && !vis[edge.to]) {
                vis[edge.to] = 1;
                prev[edge.to] = edge;
                q.push(edge.to);
            }
        }
    }
    if (!found) return 0;
    int bottleneck = MAX;
    for (Edge edge = prev[e]; edge.to != s; edge = prev[edge.from]) {
        bottleneck = min(bottleneck, remainingCapacity(edge));
    }
    for (Edge edge = prev[e]; edge.to != s; edge = prev[edge.from]) {
        capacity[edge.from][edge.to] += bottleneck;
        capacity[edge.to][edge.from] -= bottleneck;

        //cout << edge.from << ' ' << edge.to << ' ' << edge.cap << ' ';
        //cout << capacity[edge.from][edge.to] << ' ' << capacity[edge.to][edge.from] << '\n';
    }

    return bottleneck;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    int n, m; cin >> n >> m;
    for (int i = 0; i < n; i += 1) { // black = 0-99
        cin >> black[i];
        conn[s].push_back({s, i, 1});
        conn[i].push_back({i, s, 0});
    }

    for (int i = 0; i < m; i += 1) { // white = 100-199
        cin >> white[i];
        conn[OFFSET + i].push_back({OFFSET + i, e, 1});
        conn[e].push_back({e, OFFSET + i, 0});
    }

    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < m; j += 1) {
            if (gcd(black[i], white[j]) != 1) {
                conn[i].push_back({i, OFFSET + j, 1});
                conn[OFFSET + j].push_back({OFFSET + j,i, 0});
            }
        }
    }

//    for (int i = 0; i < MAX; i += 1) {
//        for (Edge edge : conn[i]) {
//            if (edge.cap == 1) cout << edge.from << ' ' << edge.to << ' ' << edge.cap << '\n';
//        }
//    }

    int ans = 0;
    int flow;
    do {
        for (int i = 0; i < MAX; i += 1) vis[i] = 0;
        flow = bfs();
        ans += flow;
        //cout << flow << '\n';
    } while (flow != 0);

    cout << ans * 2 << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}
