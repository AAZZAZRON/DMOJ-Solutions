//
// Created by Aaron Zhu on 2022-08-04.
//

#include "bits/stdc++.h"
using namespace std;
#define MAX 200001
struct query {
    int x, y;
};
int parent[MAX];
vector<query> q;
unordered_map<int, int> m;


inline int dsuFind(int a) {
    if (a == parent[a]) return a;
    return parent[a] = dsuFind(parent[a]);
}

inline void dsuUnion(int a, int b) {
    int x = dsuFind(a);
    int y = dsuFind(b);
    if (x != y) parent[x] = y;
}


signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    int t; cin >> t;
    for (int _ = 0; _ < t; _ += 1) {
        for (int i = 0; i < MAX; i += 1) parent[i] = i;
        q.clear();
        m.clear();
        int ct = 1;

        int n; cin >> n;
        for (int i = 0; i < n; i += 1) {
            int a, b, c; cin >> a >> b >> c;
            if (m.find(a) == m.end()) m[a] = ct++;
            if (m.find(b) == m.end()) m[b] = ct++;
            if (c == 1) dsuUnion(m[a], m[b]);
            else q.push_back({m[a], m[b]});
        }

        bool success = 1;
        for (query tmp : q) {
            if (dsuFind(tmp.x) == dsuFind(tmp.y)) {
                success = 0;
                break;
            }
        }
        cout << (success ? "YES" : "NO") << '\n';

    }
    return 0;
}
