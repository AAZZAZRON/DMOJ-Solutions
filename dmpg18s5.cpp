//
// Created by Aaron Zhu on 2021-12-04.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 200001

int n, q, len;
int blocks[450][MAX];
int arr[MAX];
int op, one, two, val;

inline void update(int v, int ind, int inc) {
    int bN = ind / len;
    for (int i = 1; i <= (int) sqrt(v); i += 1) {
        if (v % i == 0) {
            blocks[bN][v / i] += inc;
            if (v / i != i) blocks[bN][i] += inc;
        }
    }
}

inline int query(int l, int r, int d) {
    int c = 0;
    for (int i = l; i <= r; ) {
        if (i % len == 0 && i + len - 1 <= r) {
            c += blocks[i / len][d];
            i += len;
        } else {
            if (arr[i] % d == 0) c += 1;
            i += 1;
        }
    }
    return c;
}

int main() {
    scan(n); scan(q);
    len = (int) sqrt(n + .0) + 1;
    for (int i = 0; i < n; i += 1) {
        scan(arr[i]);
        update(arr[i], i, 1);
    }
    for (int i = 0; i < q; i += 1) {
        scan(op);
        if (op == 1) {
            scan(one); scan(two); scan(val);
            cout << query(one - 1, two - 1, val) << "\n";
        } else {
            scan(one); scan(val);
            one--;
            update(arr[one], one, -1);
            arr[one] = val;
            update(arr[one], one, 1);
        }
    }
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
