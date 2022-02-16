//
// Created by Aaron Zhu on 2022-01-03.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff

double dp[301][301][301];
double n;
int t;
int ct[3];

inline double memoize(int a, int b, int c) {
    if (!(a || b || c)) return 0.0;
    if (dp[a][b][c]) return dp[a][b][c];
    double v = 1.0;
    if (a) v += a * memoize(a - 1, b, c) / n;
    if (b) v += b * memoize(a + 1, b - 1, c) / n;
    if (c) v += c * memoize(a, b + 1, c - 1) / n;
    v /= 1.0 - (n - a - b - c) / n;
    dp[a][b][c] = v;
    return dp[a][b][c];
}

int main() {
    boost();
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> t;
        ct[t - 1] += 1;
    }
    cout << setprecision(15) << memoize(ct[0], ct[1], ct[2]) << "\n";
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
