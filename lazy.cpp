//
// Created by Aaron Zhu on 2021-07-18.
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
#define MAX 100001
struct info {
    ll min, inc;
    bool reset = 0;
};
info seg[4 * MAX];
int arr[MAX];

inline ll build(int node, int left, int right) {
    if (left == right) return seg[node].min = arr[left];
    int mid = (left + right) / 2;
    return seg[node].min = min(build(node * 2, left, mid), build(node * 2 + 1, mid + 1, right));
}

inline void checkLazy(int node, int left, int right) {
    if (seg[node].inc != 0) {
        if (seg[node].reset) seg[node].min = seg[node].inc;
        else seg[node].min += seg[node].inc;
        if (left != right) {
            if (seg[node].reset) {
                seg[2 * node].reset = 1;
                seg[2 * node].inc = seg[node].inc;
                seg[2 * node + 1].reset = 1;
                seg[2 * node + 1].inc = seg[node].inc;
            } else {
                seg[2 * node].inc += seg[node].inc;
                seg[2 * node + 1].inc += seg[node].inc;
            }
        }
        seg[node].reset = 0;
        seg[node].inc = 0;
    }
}

inline ll incrementUpdate(int node, int left, int right, int l, int r, int v) {
    if (l <= left && right <= r) {
        seg[node].inc += v;
        checkLazy(node, left, right);
        return seg[node].min;
    }
    checkLazy(node, left, right);
    if (right < l || r < left) return seg[node].min;
    int mid = (left + right) / 2;
    return seg[node].min = min(incrementUpdate(node * 2, left, mid, l, r, v), incrementUpdate(node * 2 + 1, mid + 1, right, l, r, v));
}

inline ll setUpdate(int node, int left, int right, int l, int r, int v) {
    if (l <= left && right <= r) {
        seg[node].inc = v;
        seg[node].reset = 1;
        checkLazy(node, left, right);
        return seg[node].min;
    }
    checkLazy(node, left, right);
    if (right < l || r < left) return seg[node].min;
    int mid = (left + right) / 2;
    return seg[node].min = min(setUpdate(node * 2, left, mid, l, r, v), setUpdate(node * 2 + 1, mid + 1, right, l, r, v));
}

inline ll query(int node, int left, int right, int l, int r) {
    checkLazy(node, left, right);
    if (right < l || r < left) return 99999999999999;
    if (l <= left && right <= r) return seg[node].min;
    int mid = (left + right) / 2;
    return min(query(node * 2, left, mid, l, r), query(node * 2 + 1, mid + 1, right, l, r));
}

int n, q, instruction, one, two, val;
int main() {
    scan(n); scan(q);
    for (int i = 1; i <= n; i += 1) scan(arr[i]);
    build(1, 1, n);
    for (int i = 0; i < q; i += 1) {
        scan(instruction);
        if (instruction == 1) {
            scan(one); scan(two); scan(val);
            incrementUpdate(1, 1, n, one, two, val);
        } else if (instruction == 2) {
            scan(one); scan(two); scan(val);
            setUpdate(1, 1, n, one, two, val);
        } else {
            scan(one); scan(two);
            cout << query(1,1, n, one, two) << "\n";
        }
    }
    return 0;
}
