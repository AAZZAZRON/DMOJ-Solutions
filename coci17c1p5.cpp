//
// Created by Aaron Zhu on 2021-07-07.
//

#include <iostream>
#include <algorithm>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
using namespace std;
#define MAX 200001

int n, q, a, b;
int seg[4 * MAX];
char instruction;

int update(int node, int left, int right, int ind, int val) {
    if (left == right) return seg[node] = val;

    int mid = (left + right) / 2;
    if (ind <= mid) update(node * 2, left, mid, ind, val);
    else update(node * 2 + 1, mid + 1, right, ind, val);

    int one = seg[2 * node];
    int two = seg[2 * node + 1];
    if (one == -1 && two == -1) return seg[node] = -1;
    else if (one == -1) return seg[node] = two;
    else if (two == -1) return seg[node] = one;
    else return seg[node] = min(one, two);
}


int query(int node, int l, int r, int left, int right, int maximum) {
    if (l > right || r < left) return -1;
    if (seg[node] > maximum || seg[node] == -1) return -1;
    if (left <= l && r <= right) {
        while (l != r) {
            int mid = l + (r - l) / 2;
            if (seg[node * 2] <= maximum && seg[node * 2] != -1) {
                node = node * 2;
                r = mid;
            } else {
                node = node * 2 + 1;
                l = mid + 1;
            }
        }
        return l;
    }
    int mid = l + (r - l) / 2;
    int tmp = query(node * 2, l, mid, left, right, maximum);
    if (tmp != -1) return tmp;
    return query(node * 2 + 1, mid + 1, r, left, right, maximum);
}

// let seg[i] store the the smallest # stops a child from [a, b] got off at
int main() {
    boost();
    cin >> n >> q;
    for (int i = 0; i < 4 * MAX; i += 1) seg[i] = -1;

    for (int i = 1; i <= q; i += 1) {
        cin >> instruction >> a >> b;
        if (instruction == 'M') update(1, 1, n, b, a);
        else cout << query(1, 1, n, b, n, a) << "\n";
    }
    return 0;
}
