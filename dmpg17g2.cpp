//
// Created by Aaron Zhu on 2021-07-20.
//

#include <iostream>
#include <algorithm>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 100001

struct info {ll sum, prefix, suffix, ans;} seg[4 * MAX];
ll arr[MAX];

inline info combine(info left, info right) {
    info tmp;
    tmp.sum = left.sum + right.sum;
    tmp.prefix = max(left.prefix, left.sum + right.prefix);
    tmp.suffix = max(right.suffix, right.sum + left.suffix);
    tmp.ans = max(max(left.ans, right.ans), left.suffix + right.prefix);
    return tmp;
}

inline info build(int node, int left, int right) {
    if (left == right) return seg[node] = {arr[left], arr[left], arr[left], arr[left]};
    int mid = (left + right) / 2;
    build(node * 2, left, mid);
    build(node * 2 + 1, mid + 1, right);
    return seg[node] = combine(seg[node * 2], seg[node * 2 + 1]);
}

inline info update(int node, int left, int right, int ind) {
    if (left == right) return seg[node] = {arr[left], arr[left], arr[left], arr[left]};
    int mid = (left + right) / 2;
    if (ind <= mid) update(node * 2, left, mid, ind);
    else update(node * 2 + 1, mid + 1, right, ind);
    return seg[node] = combine(seg[node * 2], seg[node * 2 + 1]);
}

inline info query(int node, int left, int right, int l, int r) {
    if (right < l || r < left) return (info) {-10000000000, -10000000000, -10000000000, -10000000000};
    if (l <= left && right <= r) return seg[node];
    int mid = (left + right) / 2;
    return combine(query(node * 2, left, mid, l, r), query(node * 2 + 1, mid + 1, right, l, r));
}

ll n, q, one, two;
char instruction;
int main() {
    boost();
    cin >> n >> q;
    for (int i = 1; i <= n; i += 1) cin >> arr[i];
    build(1, 1, n);
    for (int i = 0; i < q; i += 1) {
        cin >> instruction >> one >> two;
        if (instruction == 'S') {
            arr[one] = two;
            update(1, 1, n, one);
        } else cout << query(1, 1, n, one, two).ans << "\n";
    }
    return 0;
}
