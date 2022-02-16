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
#define MAX 22
#define MOD 1000000007

int n;
int grid[MAX][MAX];
int dp[5000000];
bitset<21> tmp;

inline int solve(int curr, bitset<21> vis) {
    if (curr == n) return 1;
    int v = (int)(vis.to_ulong());
    if (dp[v]) return dp[v] != -1 ? dp[v] : 0;
    int ct = 0;
    for (int i = 0; i < n; i += 1) {
        if (grid[curr][i] && !vis[i]) {
            vis.flip(i);
            ct = (ct + solve(curr + 1, vis)) % MOD;
            vis.flip(i);
        }
    }
    if (ct == 0) dp[v] = -1;
    else dp[v] = ct;
    return dp[v] != -1 ? dp[v] : 0;
}


int main() {
    boost();
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < n; j += 1) {
            cin >> grid[i][j];
        }
    }

    cout << solve(0, tmp) << "\n";


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
