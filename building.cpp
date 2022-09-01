//
// Created by Aaron Zhu on 2022-08-28.
//

#include "bits/stdc++.h"
using namespace std;

#define MAX 1000001
#define int long long

struct node {
    int ind, val;
};

struct qn {
    int ind, cost;
    bool operator<(const qn tmp) const {
        return cost > tmp.cost;
    }
};

inline bool cp(node one, node two, int d) {
    // one is current ind, two is top of stack
    if (two.ind - one.ind > d) return false;
    return two.val >= one.val;
}

int h[MAX];
int tall[MAX];
stack<node> s;
priority_queue<qn> pq;
int vis[MAX];
int n, d, x, y;

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    cin >> n >> d >> x >> y;
    for (int i = 0; i < n; i += 1) cin >> h[i];

    memset(tall, -1, sizeof tall);
    memset(vis, MAX, sizeof vis);
    for (int i = n - 1; i >= 0; i -= 1) {
        while (!s.empty() && !cp({i, h[i]}, s.top(), d)) {
            s.pop();
        }

        if (!s.empty()) tall[i] = s.top().ind;
        s.push({i, h[i]});
    }

//    for (int i = 0; i < n; i += 1) cout << tall[i] << ' ';
//    cout << '\n';

    pq.push({0, 0});
    vis[0] = 0;
    while (!pq.empty()) {
        qn t = pq.top(); pq.pop();
        if (t.cost != vis[t.ind]) continue;
        int ind = t.ind, cost = t.cost;
        if (ind + 1 < n && vis[ind + 1] > cost + y) {
            vis[ind + 1] = cost + y;
            pq.push({ind + 1, cost + y});
        }
        if (ind + 2 < n && vis[ind + 2] > cost + y) {
            vis[ind + 2] = cost + y;
            pq.push({ind + 2, cost + y});
        }
        if (tall[ind] != -1 && vis[tall[ind]] > cost + x) {
            vis[tall[ind]] = cost + x;
            pq.push({tall[ind], cost + x});
        }
    }

//    for (int i = 0; i < n; i += 1) cout << vis[i] << ' ';
//    cout << '\n';

    cout << vis[n - 1] << '\n';

    return 0;
}
