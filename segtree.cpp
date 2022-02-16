//
// Created by Aaron Zhu on 2022-02-15.
//

#include "bits/stdc++.h"
using namespace std;

#define MAX 100001
#define INF 1e7

int n, m, x, y;
char ins;
int arr[MAX];
int seg[4 * MAX];

inline int build(int node, int left, int right) {
    if (left == right) return seg[node] = arr[left];
    int mid = (left + right) / 2;
    return seg[node] = min(build(node * 2, left, mid), build(node * 2 + 1, mid + 1, right));
}

inline int update(int node, int left, int right, int ind) {
    if (left == right) return seg[node] = arr[ind];
    int mid = (left + right) / 2;
    if (ind <= mid) update(node * 2, left, mid, ind);
    else update(node * 2 + 1, mid + 1, right, ind);
    return seg[node] = min(seg[node * 2], seg[node * 2 + 1]);
}

inline int query(int node, int left, int right, int l, int r) {
    if (right < l || r < left) return INF;
    if (l <= left && right <= r) return seg[node];
    int mid = (left + right) / 2;
    return min(query(node * 2, left, mid, l, r), query(node * 2 + 1, mid + 1, right, l, r));
}

int main() {
    cin.tie(0); cin.sync_with_stdio(0);

    cin >> n >> m;
    for (int i = 1; i <= n; i += 1) cin >> arr[i];
    build(1, 1, n);
    for (int i = 0; i < m; i += 1) {
        cin >> ins >> x >> y;
        if (ins == 'M') {
            arr[x + 1] = y;
            update(1, 1, n, x + 1);
        } else if (ins == 'Q') {
            cout << query(1, 1, n, x + 1, y + 1) << '\n';
        }
    }

}