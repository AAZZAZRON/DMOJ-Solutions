//
// Created by Aaron Zhu on 2021-12-23.
//

#include "bits/stdc++.h"

#define ll long long
#define pll pair<ll, ll>
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 100001

struct node {
    ll cost, x, y, P;

    bool operator() (const node& one, const node& two) {
        if (one.cost != two.cost) return one.cost < two.cost;
        return one.P < two.P;
    }
} node;

ll n, m, D, a, b, c;
vector<struct node> paths;
int parent[MAX];
ll cost = 0;
ll minD = INF;

inline int dsuFind(int one) {
    int root = one;
    while (parent[root] != root) root = parent[root];

    // path compression
    while (parent[one] != root) {
        parent[one] = root;
        one = parent[one];
    }
    return root;
}

inline bool dsuUnion(int one, int two) {
    int p1 = dsuFind(one);
    int p2 = dsuFind(two);
    if (p1 == p2) return 0;
    parent[p1] = p2;
    return 1;
}

int main() {
    boost();
    cin >> n >> m >> D;
    for (int i = 0; i < n - 1; i += 1) {
        cin >> a >> b >> c;
        paths.push_back((struct node) {c, a, b, 0});
    }
    for (int i = n - 1; i < m; i += 1) {
        cin >> a >> b >> c;
        paths.push_back((struct node) {c, a, b, 1});
    }

    sort(paths.begin(), paths.end(), node);
    ll days = 0;
    ll used = 0;
    ll ct = 0;
    ll mE;
    for (int i = 0; i < MAX; i += 1) parent[i] = i;

    for (struct node p : paths) {
        if (dsuUnion(p.x, p.y)) {
            used += 1;
            if (p.P) days += 1;
            mE = p.cost;
        }
        if (used == n - 1) break;
        ct += 1;
    }

    if (paths[ct].P) { // if the node is not in original
        for (int i = 0; i < MAX; i += 1) parent[i] = i;

        for (struct node p: paths) {
            if (dsuFind(p.x) != dsuFind(p.y)) {
                if (p.cost < mE || (p.cost == mE && !p.P)) dsuUnion(p.x, p.y);
                else if (p.cost <= D && !p.P) {
                    days--;
                    break;
                }
            }
        }
    }
    cout << days << "\n";

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
