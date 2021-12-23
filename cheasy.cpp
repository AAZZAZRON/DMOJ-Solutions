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
int r, c;
int x, y, v;
int r1, c1, r2, c2;

inline ll psa(ll arr[MAX][MAX]) {
    return arr[r2][c2] - arr[r2][c1 - 1] - arr[r1 - 1][c2] + arr[r1 - 1][c1 - 1];
}

int main() {
    scan(r); scan(c);
    while (true) {
        scan(x); scan(y); scan(v);
        if (x == y && y == v && v == 0) break;
        if ((x + y) % 2 == 0) even[x][y] = v;
        else odd[x][y] = v;
    }
    for (int i = 1; i <= r; i += 1) {
        int eT = 0, oT = 0;
        for (int j = 1; j <= c; j += 1) {
            eT += even[i][j];
            even[i][j] = even[i - 1][j] + eT;

            oT += odd[i][j];
            odd[i][j] = odd[i - 1][j] + oT;
        }
    }

    while (true) {
        scan(r1); scan(c1); scan(r2); scan(c2);
        if (r1 == c1 && c1 == r2 && r2 == c2 && c2 == 0) break;
        if ((r1 + c1) % 2 == 0) cout << psa(even) - psa(odd) << "\n";
        else cout << psa(odd) - psa(even) << "\n";
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
