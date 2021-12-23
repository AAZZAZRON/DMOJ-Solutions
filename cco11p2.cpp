//
// Created by Aaron Zhu on 2021-07-29.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <cassert>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 1601
#define INF 0x7fffffff
struct info {
    int v, time, n;
};
struct connect {
    int n, c, s;
};
int expose, n, e;
int one, two, cost, above;
vector<connect> connections[MAX];
int d[MAX][3601];
bool visited[MAX][3601];
queue<info> q;
int main() {
    scan(expose); scan(n); scan(e);
    for (int i = 0; i < e; i += 1) {
        scan(one); scan(two); scan(cost); scan(above);
        connections[one].push_back((connect) {two, cost, above});
        connections[two].push_back((connect) {one, cost, above});
    }
    visited[0][0] = 1;
    q.push((info) {0, 0});
    while (!q.empty()) {
        info node = q.front(); q.pop();
        for (connect el : connections[node.v]) {
            int sun = node.time + el.c * el.s;
            if (sun > expose) continue;
            if (!visited[el.n][sun]) {
                visited[el.n][sun] = 1;
                d[el.n][sun] = d[node.v][node.time] + el.c;
                q.push((info) {el.n, sun});
            } else if (d[node.v][node.time] + el.c < d[el.n][sun]) {
                d[el.n][sun] = d[node.v][node.time] + el.c;
                q.push((info) {el.n, sun});
            }
        }
    }
    int ans = INF;
    for (int i = 0; i <= expose; i += 1) {
        if (d[n - 1][i]) ans = min(ans, d[n - 1][i]);
    }
    if (ans == INF) cout << "-1\n";
    else cout << ans << "\n";
    return 0;
}
