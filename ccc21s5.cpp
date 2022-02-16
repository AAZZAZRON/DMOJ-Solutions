//
// Created by Aaron Zhu on 2021-12-28.
// sqrt decomp checking
//

#include "../../bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 200001

struct node {
    int l, r, v;
};

int n, q, one, two, val;
int diff[17][MAX];
int arr[MAX];
vector<node> queries;
int len;
int blocks[500];

inline int gcd(int x, int y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}

inline int query(int l, int r) {
    int g = arr[l];
    for (int i = l; i <= r;) {
        if (i % len == 0 && i + len - 1 <= r) {
            g = gcd(g, blocks[i / len]);
            i += len;
        } else {
            g = gcd(g, arr[i]);
            i += 1;
        }
    }
    return g;
}

int main() {
    boost();
    cin >> n >> q;
    len = (int) n / 500 + 1;

    for (int i = 0; i < MAX; i += 1) arr[i] = 1;
    for (int i = 0; i < 500; i += 1) blocks[i] = 1;

    for (int i = 0; i < q; i += 1) {
        cin >> one >> two >> val;
        queries.push_back((node) {one, two, val});
        diff[val][one] += 1;
        diff[val][two + 1] -= 1;
    }

    for (int i = 1; i <= 16; i += 1) {
        for (int j = 1; j <= n; j += 1) {
            diff[i][j] += diff[i][j - 1];
            if (diff[i][j]) arr[j] = arr[j] * i / gcd(arr[j], i);
        }
    }

    for (int i = 1; i <= n; i += 1) {
        int v = arr[i];
        int bN = i / len;
        if (i % len == 0) blocks[bN] = v;
        else blocks[bN] = gcd(blocks[bN], v);
    }

    for (node tmp : queries) {
        if (tmp.v != query(tmp.l, tmp.r)) {
            cout << "Impossible\n";
            return 0;
        }
    }
    for (int i = 1; i <= n; i += 1) cout << arr[i] << " ";
    cout << "\n";

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
