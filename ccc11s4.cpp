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
#define int long long
#define MAX 30
#define MAXV 10000001
int cap[MAX][MAX];
vector<int> conn[MAX];
int source = 1;
int sink = 18;
int vis[MAX];
int pre[MAX];


inline int bfs() {
    memset(vis, 0, sizeof vis);
    queue<int> q;
    vis[source] = 1;
    q.push(source);
    pre[source] = -1;

    while (!q.empty()) {
        int from = q.front(); q.pop();
        if (from == sink) return 1;
        for (int to : conn[from]) {
            if (cap[from][to] > 0 && !vis[to]) {
                vis[to] = 1;
                pre[to] = from;
                q.push(to);
            }
        }
    }
    return 0;
}

inline int flow() {
    int maxFlow = 0;
    while (bfs()) {
        int bottleneck = INT32_MAX;
        for (int to = sink; to != source; to = pre[to]) {
            int from = pre[to];
            bottleneck = min(bottleneck, cap[from][to]);
        }
        for (int to = sink; to != source; to = pre[to]) {
            int from = pre[to];
            cap[from][to] -= bottleneck;
            cap[to][from] += bottleneck;
        }
        maxFlow += bottleneck;
    }
    return maxFlow;
}

inline void addConn(int a, int b, int c) {
    conn[a].push_back(b);
    conn[b].push_back(a);
    cap[a][b] = c;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    for (int i = 2; i < 2 + 8; i += 1) {
        int v; cin >> v;
        addConn(source, i, v);
    }

    for (int i = 10; i < 10 + 8; i += 1) {
        int v; cin >> v;
        addConn(i, sink, v);
    }

    // O-
    addConn(2, 10, MAXV);

    // O+
    addConn(2, 11, MAXV);
    addConn(3, 11, MAXV);

    // A-
    addConn(2, 12, MAXV);
    addConn(4, 12, MAXV);

    // A+
    addConn(2, 13, MAXV);
    addConn(3, 13, MAXV);
    addConn(4, 13, MAXV);
    addConn(5, 13, MAXV);

    // B-
    addConn(2, 14, MAXV);
    addConn(6, 14, MAXV);

    // B+
    addConn(2, 15, MAXV);
    addConn(3, 15, MAXV);
    addConn(6, 15, MAXV);
    addConn(7, 15, MAXV);

    // AB-
    for (int i = 2; i <= 8; i += 2) addConn(i, 16, MAXV);

    // AB+
    for (int i = 2; i <= 9; i += 1) addConn(i, 17, MAXV);

    cout << flow() << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}
// O- O+ A- A+ B- B+ AB- AB+
// 2  3  4  5  6  7  8   9
// 10 11 12 13 14 15 16  17

/*
 * O- | O-
 * O+ | O- O+
 * A- | A- O-
 * A+ | A- O- A+ O+
 * B- | B- O-
 * B+ | B- O- B+ O+
 * AB-| A- B- O-
 * AB+| A- B- O- A+ B+ O+
 */
