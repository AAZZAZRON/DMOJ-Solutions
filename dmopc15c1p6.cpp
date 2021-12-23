//
// Created by Aaron Zhu on 2021-07-21.
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
#define MAX 200001
struct info {
    ll val, lazy;
};
info seg[4 * MAX];
ll arr[MAX];

inline ll build(int node, int left, int right) {
    if (left == right) return seg[node].val = arr[left];
    int mid = (left + right) / 2;
    return seg[node].val = build(node * 2, left, mid) + build(node * 2 + 1, mid + 1, right);
}

inline void checkLazy(int node, int left, int right) {
    if (seg[node].lazy != 0) {
        seg[node].val += seg[node].lazy * (right - left + 1);
        if (left != right) {
            seg[node * 2].lazy += seg[node].lazy;
            seg[node * 2 + 1].lazy += seg[node].lazy;
        }
        seg[node].lazy = 0;
    }
}

inline int update(int node, int left, int right, int l, int r, int v) {
    if (l <= left && right <= r) {
        seg[node].lazy += v;
        checkLazy(node, left, right);
        return 0;
    }
    checkLazy(node, left, right);
    if (right < l || r < left) return 0;
    int mid = (left + right) / 2;
    update(node * 2, left, mid, l, r, v);
    update(node * 2 + 1, mid + 1, right, l, r, v);
    seg[node].val = seg[node * 2].val + seg[node * 2 + 1].val;
    return 0;
}

inline ll query(int node, int left, int right, int l, int r) {
    checkLazy(node, left, right);
    if (right < l || r < left) return 0;
    if (l <= left && right <= r) return seg[node].val;
    int mid = (left + right) / 2;
    return query(node * 2, left, mid, l, r) + query(node * 2 + 1, mid + 1, right, l, r);
}

int mod, n, q, instruction, one, two, val;
int main() {
    scan(mod); scan(n); scan(q);
    for (int i = 1; i <= n; i += 1) scan(arr[i]);
    build(1, 1, n);
    for (int i = 0; i < q; i += 1) {
        scan(instruction); scan(one); scan(two);
        if (instruction == 1) {
            scan(val);
            update(1, 1, n, one, two, val);
        }
        else cout << query(1, 1, n, one, two) % mod << "\n";
    }
    return 0;
}
