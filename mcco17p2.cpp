//
// Created by Aaron Zhu on 2021-12-28.
//

#include "../../bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 200001
struct node {
    ll lazy, max;
} seg[4 * MAX];
int n, k, q, cmd, one, two;

inline void checkLazy(int node, int left, int right) {
    if (seg[node].lazy != 0) {
        assert(seg[node].lazy >= 0);
        seg[node].max += seg[node].lazy;
        if (left != right) {
            seg[2 * node].lazy += seg[node].lazy;
            seg[2 * node + 1].lazy += seg[node].lazy;
        }
        seg[node].lazy = 0;
    }
}

inline ll update(int node, int l, int r, int left, int right, int v) {
    if (l <= left && right <= r) {
        seg[node].lazy += v;
        checkLazy(node, left, right);
        return seg[node].max;
    }
    checkLazy(node, left, right);
    if (right < l || r < left) return seg[node].max;
    int mid = (left + right) / 2;
    return seg[node].max = max(update(node * 2, l, r, left, mid, v), update(node * 2 + 1, l, r, mid + 1, right, v));
}

inline ll query(int node, int l, int r, int left, int right) {
    checkLazy(node, left, right);
    if (right < l || r < left) return 0;
    if (l <= left && right <= r) return seg[node].max;
    int mid = (left + right) / 2;
    return max(query(node * 2, l, r, left, mid), query(node * 2 + 1, l, r, mid + 1, right));
}

inline ll print(int node, int left, int right) {
    checkLazy(node, left, right);
    if (left == right) {
        cout << left << " " << seg[node].max << "\n";
        return seg[node].max;
    }
    int mid = (left + right) / 2;
    seg[node].max = max(print(node * 2, left, mid), print(node * 2 + 1, mid + 1, right));
    cout << left << " " << right << " " << seg[node].max << " " << seg[node].lazy << "\n";
    return seg[node].max;
}

int main() {
    boost();
    cin >> n >> k >> q;
    for (int i = 0; i < q; i += 1) {
        cin >> cmd >> one >> two;
        if (cmd == 0) {
            one += 1;
            update(1, max(1, one - k + 1), one, 1, n, two);
        } else {
            one += 1;
            two += 1;
            cout << query(1, one, two, 1, n) << "\n";
        }
        //print(1, 1, n);
    }
    // print(1, 1, n);
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
