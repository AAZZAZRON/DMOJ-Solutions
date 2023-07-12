//
// Created by Aaron Zhu on 2023-02-17.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
//ifstream IN;
//ofstream OUT;
#define MAX 2005
#define MAXV 10001
int cap[MAX][MAX];
vector<int> conn[MAX];
int vis[MAX];
int pre[MAX];
int rate[MAX];
int source = 0; int sink;

inline int bfs() {
    memset(vis, 0, sizeof vis);
    vis[source] = 1;
    queue<int> q;
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
        for (int to = sink; pre[to] != -1; to = pre[to]) {
            int from = pre[to];
            bottleneck = min(bottleneck, cap[from][to]);
        }

        for (int to = sink; pre[to] != -1; to = pre[to]) {
            int from = pre[to];
            cap[from][to] -= bottleneck;
            cap[to][from] += bottleneck;
        }
        maxFlow += bottleneck;
    }
    return maxFlow;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    int m, n; cin >> m >> n;
    for (int i = 1; i <= m; i += 1) {
        cin >> rate[i];
        if (rate[i] == 0) sink = i;
        else {
            conn[i].push_back(1000 + i);
            conn[1000 + i].push_back(i);
            cap[i][1000 + i] = cap[1000 + i][i] = rate[i];
        }
    }

    conn[source].push_back(1);
    conn[1].push_back(source);
    cap[source][1] = INT32_MAX;

    // in = i
    // out = 1000 + ia
    for (int i = 0; i < n; i += 1) {
        int a, b; cin >> a >> b;
        conn[1000 + a].push_back(b);
        conn[b].push_back(1000 + a);
        cap[1000 + a][b] = b != sink ? rate[b] : INT32_MAX;
    }

//    for (int i = 0; i < MAX; i += 1) {
//        for (int j : conn[i]) {
//            if (cap[i][j]) cout << i << ' ' << j << ' ' << cap[i][j] << '\n';
//        }
//    }

    int ans = flow();
    //assert(ans <= 10000);
    cout << ans << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}
