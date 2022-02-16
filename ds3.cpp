//
// Created by Aaron Zhu on 2022-02-15.
//

#include "bits/stdc++.h"
#define MAX 100001
#define INF 2e9 + 5

using namespace std;

struct item {
    int min, gcd, freq;
};
int n, m, x, y;
char ins;
int arr[MAX];
item seg[4 * MAX];

inline int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

inline void build(int node, int left, int right) {
    if (left == right) {
        seg[node].min = seg[node].gcd = arr[left];
        seg[node].freq = 1;
        return;
    }

    int mid = (left + right) / 2;
    build(node * 2, left, mid);
    build(node * 2 + 1, mid + 1, right);
    seg[node].min = min(seg[node * 2].min, seg[node * 2 + 1].min);
    seg[node].gcd = gcd(seg[node * 2].gcd, seg[node * 2 + 1].gcd);
    seg[node].freq = 0;
    if (seg[node * 2].gcd == seg[node].gcd) seg[node].freq += seg[node * 2].freq;
    if (seg[node * 2 + 1].gcd == seg[node].gcd) seg[node].freq += seg[node * 2 + 1].freq;
    return;
}

inline void update(int node, int left, int right, int ind) {
    if (left == right) {
        seg[node].min = seg[node].gcd = arr[ind];
        seg[node].freq = 1;
        return;
    }
    int mid = (left + right) / 2;
    if (ind <= mid) update(node * 2, left, mid, ind);
    else update(node * 2 + 1, mid + 1, right, ind);

    seg[node].min = min(seg[node * 2].min, seg[node * 2 + 1].min);
    seg[node].gcd = gcd(seg[node * 2].gcd, seg[node * 2 + 1].gcd);
    seg[node].freq = 0;
    if (seg[node * 2].gcd == seg[node].gcd) seg[node].freq += seg[node * 2].freq;
    if (seg[node * 2 + 1].gcd == seg[node].gcd) seg[node].freq += seg[node * 2 + 1].freq;
    return;
}

inline int minQ(int node, int left, int right, int l, int r) {
    if (right < l || r < left) return INF;
    if (l <= left && right <= r) return seg[node].min;
    int mid = (left + right) / 2;
    return min(minQ(node * 2, left, mid, l, r), minQ(node * 2 + 1, mid + 1, right, l, r));
}

inline int gcdQ(int node, int left, int right, int l, int r) {
    if (right < l || r < left) return -1;
    if (l <= left && right <= r) return seg[node].gcd;
    int mid = (left + right) / 2;
    int one = gcdQ(node * 2, left, mid, l, r);
    int two = gcdQ(node * 2 + 1, mid + 1, right, l, r);
    if (one == -1 && two == -1) return -1;
    if (one == -1) return two;
    if (two == -1) return one;
    return gcd(one, two);
}

inline int freqQ(int node, int left, int right, int l, int r, int G) {
    if (right < l || r < left) return 0;
    if (l <= left && right <= r) {
        if (seg[node].gcd == G) return seg[node].freq;
        return 0;
    }
    int mid = (left + right) / 2;
    return freqQ(node * 2, left, mid, l, r, G) + freqQ(node * 2 + 1, mid + 1, right, l, r, G);
}

inline void print(int node, int left, int right) {
    cout << node << " " << left << " " << right << ": " << seg[node].min << " " << seg[node].gcd << " " << seg[node].freq << '\n';
    if (left == right) return;
    int mid = (left + right) / 2;
    print(node * 2, left, mid);
    print(node * 2 + 1, mid + 1, right);
    return;
}

int main() {
    cin.tie(0); cin.sync_with_stdio(0);

    cin >> n >> m;
    for (int i = 1; i <= n; i += 1) cin >> arr[i];
    build(1, 1, n);
    for (int i = 0; i < m; i += 1) {
        cin >> ins >> x >> y;
        if (ins == 'C') {
            arr[x] = y;
            update(1, 1, n, x);
        } else if (ins == 'M') {
            cout << minQ(1, 1, n, x, y) << '\n';
        } else if (ins == 'G') {
            cout << gcdQ(1, 1, n, x, y) << '\n';
        } else if (ins == 'Q') {
            cout << freqQ(1, 1, n, x, y, gcdQ(1, 1, n, x, y)) << '\n';
        } else assert(false);
    }

    return 0;
}
