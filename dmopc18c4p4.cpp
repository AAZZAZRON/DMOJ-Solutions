//
// Created by Aaron Zhu on 2021-09-13.
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
#define INF 0x7fffffff
#define MAX 200001

ll BIT[MAX];

inline void insert(ll ind, ll v) {
    for (; ind < MAX; ind += ind & (-ind)) {
        BIT[ind] += v;
    }
}

inline ll query(ll ind) {
    ll total = 0;
    for (; ind >= 1; ind -= ind & (-ind)) total += BIT[ind];
    return total;
}
struct qN {
    ll l, r, k;
};


ll psa[MAX];
vector<pii> s;
vector<qN> queries;
ll ans[MAX];
ll n, q, t, l, r, k;
int main() {
    scan(n); scan(q);
    for (int i = 0; i < n; i += 1) {
        scan(t);
        psa[i + 1] = psa[i] + t;
        s.push_back(make_pair(t, -i));
    }
    for (int i = 1; i <= q; i += 1) {
        scan(l); scan(r); scan(k);
        queries.push_back((qN) {l, r, k});
        s.push_back(make_pair(k - 1, i));
    }
    sort(s.begin(), s.end());
    for (auto el : s) {
        ll v = el.first, i = el.second;
        if (i <= 0) insert(-i + 1, v);
        else {
            qN tmp = queries[i - 1];
            ans[i - 1] = (psa[tmp.r] - psa[tmp.l - 1]) - 2 * (query(tmp.r) - query(tmp.l - 1));
        }
    }
    for (int i = 0; i < q; i += 1) cout << ans[i] << "\n";
    return 0;
}
