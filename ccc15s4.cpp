//
// Created by Aaron Zhu on 2021-08-06.
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
#define MAX 2001
#define INF 0x7fffffff
struct info {
    int node, damage;
};
struct connect {
    int node, distance, damage;
};
int damage, n, e;
int one, two, cost, dmg;
int beginning, ending;
vector<connect> connections[MAX];
int d[MAX][201];
bool visited[MAX][201];
queue<info> q;
int main() {
    scan(damage); scan(n); scan(e);
    for (int i = 0; i < e; i += 1) {
        scan(one); scan(two); scan(cost); scan(dmg);
        connections[one].push_back((connect) {two, cost, dmg});
        connections[two].push_back((connect) {one, cost, dmg});
    }
    scan(beginning); scan(ending);
    visited[beginning][0] = 1;
    q.push((info) {beginning, 0});
    while (!q.empty()) {
        info node = q.front(); q.pop();
        for (connect el : connections[node.node]) {
            int total = node.damage + el.damage;
            if (total > damage) continue;
            if (!visited[el.node][total]) {
                visited[el.node][total] = 1;
                d[el.node][total] = d[node.node][node.damage] + el.distance;
                q.push((info) {el.node, total});
            } else if (d[node.node][node.damage] + el.distance < d[el.node][total]) {
                d[el.node][total] = d[node.node][node.damage] + el.distance;
                q.push((info) {el.node, total});
            }
        }
    }
    int ans = INF;
    for (int i = 0; i < damage; i += 1) {
        if (d[ending][i]) ans = min(ans, d[ending][i]);
    }
    if (ans == INF) cout << "-1\n";
    else cout << ans << "\n";
    return 0;
}
