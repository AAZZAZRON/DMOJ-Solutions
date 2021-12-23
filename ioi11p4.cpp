//
// Created by Aaron Zhu on 2021-08-31.
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
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
struct conn {
    ll v, cost;
    bool operator<(const conn &o) const {
        return cost > o.cost;
    }
};
#define INF 0x7fffffff
#define MAX 100001
vector<conn> c[MAX];
ll dist[MAX][2];
bool visited[MAX];
int n, m, k;
int one, two, cost;
ll total = 0;
int travel_plan(int N, int M, int R[][2], int W[], int K, int E[]) {
    for (int i = 0; i < M; i += 1) {
        one = R[i][0], two = R[i][1];
        cost = W[i];
        c[one].push_back((conn) {two, cost});
        c[two].push_back((conn) {one, cost});
    }
    priority_queue<conn> pq;
    for (int i = 0; i < MAX; i += 1) {
        dist[i][0] = dist[i][1] = INF;
    }
    for (int i = 0; i < K; i += 1) {
        one = E[i];
        dist[one][0] = dist[one][1] = 0;
        pq.push((conn) {one, 0});
    }
    while (!pq.empty()) {
        conn tmp = pq.top();
        pq.pop();
        if (visited[tmp.v] || tmp.cost > dist[tmp.v][1]) continue;
        visited[tmp.v] = 1;
        for (auto it : c[tmp.v]) {
            int next = it.v;
            ll w = tmp.cost + it.cost;
            bool found = 0;
            if (w <= dist[next][0]) { // get top 2
                dist[next][1] = dist[next][0];
                dist[next][0] = w;
                found = 1;
            } else if (w < dist[next][1]) {
                dist[next][1] = w;
                found = 1;
            }
            if (found) {
                pq.push((conn) {next, dist[next][1]});
            }
        }
    }
    // for (int i = 0; i < n; i += 1) cout << dist[i][0] << " " << dist[i][1] << "\n";
    if (dist[0][1] == INF) return dist[0][0];
    else return dist[0][1];
}
