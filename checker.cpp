//
// Created by Aaron Zhu on 2021-11-13.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 3002

ll odd[MAX][MAX];
ll even[MAX][MAX];
ll current[MAX][MAX];
int r, c;
int x, y, v;
int q, r1, c1, r2, c2;

inline void update(bool isE, ll inc) {
    for (int i = x; i <= r; i += (i & -i)) {
        for (int j = y; j <= c; j += (j & -j)) {
            if (isE) even[i][j] += inc;
            else odd[i][j] += inc;
        }
    }
}

inline ll query(ll arr[MAX][MAX], int n, int m) {
    ll total = 0;
    for (int i = n; i >= 1; i -= (i & -i)) for (int j = m; j >= 1; j -= (j & -j)) total += arr[i][j];
    return total;
}

inline ll psa(ll arr[MAX][MAX]) {
    return query(arr, r2, c2) - query(arr, r1 - 1, c2) - query(arr, r2, c1 - 1) + query(arr, r1 - 1, c1 - 1);
}

int main() {
    scan(r); scan(c);
    while (1) {
        scan(q);
        if (q == 0) break;
        else if (q == 1) {
            scan(x); scan(y); scan(v);
            if ((x + y) % 2 == 0) update(1, v - current[x][y]);
            else update(0, v - current[x][y]);
            current[x][y] = v;
        } else {
            scan(r1); scan(c1); scan(r2); scan(c2);
            if ((r1 + c1) % 2 == 0) cout << psa(even) - psa(odd) << "\n";
            else cout << psa(odd) - psa(even) << "\n";
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
