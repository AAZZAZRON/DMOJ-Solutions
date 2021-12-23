//
// Created by Aaron Zhu on 2021-07-18.
//

#include <iostream>
#include <map>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 500001
int arr[MAX];
int n, q, x, one, two, c, instruction;
map<int, int> seg[4 * MAX];

inline int fill(int node, int left, int right) {
    if (left == right) return seg[node][0] = 1;
    int mid = (left + right) / 2;
    fill(node * 2, left, mid);
    fill(node * 2 + 1, mid + 1, right);
    return seg[node][0] = seg[node * 2][0] + seg[node * 2 + 1][0];
}

inline int update(int node, int left, int right, int before, int after, int ind) {
    if (left == right) {
        seg[node].erase(before);
        return seg[node][after] = 1;
    }
    int mid = (left + right) / 2;
    if (ind <= mid) update(node * 2, left, mid, before, after, ind);
    else update(node * 2 + 1, mid + 1, right, before, after, ind);
    seg[node][before] -= 1;
    if (seg[node][before] == 0) seg[node].erase(before);
    if (seg[node].count(after)) seg[node][after] += 1;
    else seg[node][after] = 1;
    return 0;
}

inline int query(int node, int left, int right, int l, int r, int v) {
    if (right < l || r < left) return 0;
    if (l <= left && right <= r) {
        if (seg[node].count(v)) return seg[node][v];
        return 0;
    }
    int mid = (left + right) / 2;
    return query(node * 2, left, mid, l, r, v) + query(node * 2 + 1, mid + 1, right, l, r, v);
}


int main() {
    boost();
    cin >> n >> q;
    fill(1, 1, n);
    for (int i = 0; i < q; i += 1) {
        cin >> instruction;
        if (instruction == 1) {
            cin >> x;
            arr[x] += 1;
            update(1, 1, n, arr[x] - 1, arr[x], x);
        } else if (instruction == 2) {
            cin >> x;
            arr[x] -= 1;
            update(1, 1, n, arr[x] + 1, arr[x], x);
        } else {
            cin >> one >> two >> c;
            cout << query(1, 1, n, one, two, c) << "\n";
        }
    }
    return 0;
}
