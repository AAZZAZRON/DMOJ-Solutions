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
#define MAX 1000001
struct info {
    int val;
    int lazy;
};

info seg[MAX * 4];
int n, q, instruction, one, two, a;

void update(int node, int left, int right, int l, int r, int v) {
    if (right < l || r < left) return;
    if (l <= left && right <= r) {
        seg[node].lazy = seg[node].lazy + v;
        return;
    }
    int mid = (left + right) / 2;
    update(node * 2, left, mid, l, r, v);
    update(node * 2 + 1, mid + 1, right, l, r, v);
    return;
}

int query(int node, int left, int right, int l, int r) {
    if (seg[node].lazy != 0) {
        seg[node].val += seg[node].lazy;
        if (left != right) {
            seg[2 * node].lazy += seg[node].lazy;
            seg[2 * node + 1].lazy += seg[node].lazy;
        }
        seg[node].lazy = 0;
    }
    if (right < l || r < left) return 0;
    if (l <= left && right <= r) return seg[node].val;
    int mid = (left + right) / 2;
    return query(node * 2, left, mid, l, r) + query(node * 2 + 1, mid + 1, right, l, r);
}


int main()
{
    for (int i = 0; i < 4 * MAX; i += 1) {
        seg[i].val = 0;
        seg[i].lazy = 0;
    }
    scan(n); scan(q);
    for (int i = 0; i < q; i += 1) {
        scan(instruction);
        if (instruction == 1) {
            scan(one); scan(two); scan(a);
            update(1, 0, n, one, two, a);
        } else {
            scan(one); scan(two);
            cout << query(1, 0, n, one, two) << "\n";
        }
    }

    return 0;
}
