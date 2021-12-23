//
// Created by Aaron Zhu on 2021-07-28.
//

#include <iostream>
#include <algorithm>
#include <functional>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 2000001
#define INF 0x7fffffff
struct info {
    int top = 0, bottom = INF;
    bool lazy;
};
info seg[4 * MAX];
int arr[MAX];

inline void checkLazy(int node, int left, int right) {
    if (seg[node].lazy) {
        if (left == right) {
            arr[left] = min(max(seg[node].top, arr[left]), seg[node].bottom);
        } else {
            seg[node * 2].lazy = seg[node * 2 + 1].lazy = 1;

            seg[node * 2].top = min(max(seg[node].top, seg[node * 2].top), seg[node].bottom);
            seg[node * 2].bottom = max(min(seg[node].bottom, seg[node * 2].bottom), seg[node].top);

            seg[node * 2 + 1].top = min(max(seg[node].top, seg[node * 2 + 1].top), seg[node].bottom);
            seg[node * 2 + 1].bottom = max(min(seg[node].bottom, seg[node * 2 + 1].bottom), seg[node].top);
        }
        seg[node].lazy = 0;
        seg[node].top = 0;
        seg[node].bottom = INF;
    }
}

inline int update(int node, int left, int right, int l, int r, int h, int op) {
    checkLazy(node, left, right);
    if (right < l || r < left) return 1;
    if (l <= left && right <= r) {
        if (op == 1) { // add
            seg[node].top = max(h, seg[node].top);
            seg[node].bottom = max(h, seg[node].bottom);
        } else {
            seg[node].top = min(h, seg[node].top);
            seg[node].bottom = min(h, seg[node].bottom);
        }
        seg[node].lazy = 1;
        checkLazy(node, left, right);
        return 1;
    }
    int mid = (left + right) / 2;
    return update(node * 2, left, mid, l, r, h, op) + update(node * 2 + 1, mid + 1, right, l, r, h, op);
}


inline void print(int node, int left, int right) {
    cout << left << ", " << right << ": " << seg[node].lazy << " " << seg[node].top << " " << seg[node].bottom << "\n";
    if (left == right) return;
    int mid = (left + right) / 2;
    print(node * 2, left, mid);
    print(node * 2 + 1, mid + 1, right);
    return;
}

inline int query(int node, int left, int right, int ind) {
    checkLazy(node, left, right);
    if (left == right) return arr[left];
    int mid = (left + right) / 2;
    if (ind <= mid) return query(node * 2, left, mid, ind);
    return query(node * 2 + 1, mid + 1, right, ind);
}

int n, q, instruction, one, two, val;
int main() {
    scan(n); scan(q);
    for (int i = 0; i < q; i += 1) {
        scan(instruction); scan(one); scan(two); scan(val);
        if (instruction == 1) update(1, 1, n, one + 1, two + 1, val, 1);
        else update(1, 1, n, one + 1, two + 1, val, 0);
        //print(1, 1, n);
        //for (int j = 1; j <= n; j += 1) cout << arr[j] << " ";
        //cout << "\n\n";
    }
    for (int i = 1; i <= n; i += 1) cout << query(1, 1, n, i) << "\n";
    //print(1, 1, n);
    //for (int i = 1; i <= n; i += 1) cout << arr[i] << " ";
    return 0;
}