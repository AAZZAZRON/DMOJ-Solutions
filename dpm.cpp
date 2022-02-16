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
#define MAXN 101
#define MAXV 100001
#define MOD 1000000007

ll n, k;
// let dp[i][j] be the number of ways
// to split j candies amongst the first i kids
ll dp[MAXN][MAXV];
ll need[MAXN];



int main() {
    boost();
    cin >> n >> k;
    for (int i = 1; i <= n; i += 1) cin >> need[i];

    // base case
    for (int i = 0; i < MAXN; i += 1) dp[i][0] = 1;

    for (int i = 1; i <= n; i += 1) {
        ll window = 1;
        for (int j = 1; j <= min(k, need[i]); j += 1) {
            window = (window + dp[i - 1][j]) % MOD;
            dp[i][j] = window;
        }
        for (int j = min(k, need[i]) + 1; j <= k; j += 1) {
            window = (window - dp[i - 1][j - need[i] - 1] + dp[i - 1][j] + MOD) % MOD;
            dp[i][j] = window;
        }
    }
    cout << dp[n][k] << "\n";
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
