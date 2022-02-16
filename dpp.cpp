//
// Created by Aaron Zhu on 2022-01-03.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 100001
#define MOD 1000000007

int n, one, two;
vector<int> conn[MAX];
ll dp[MAX][2];

// let dp[i][0] be # ways to complete the child branch if i is white
// let dp[i][1] be # ways to complete the child branch if i is black or white

inline int solve(int node, int last, bool canBeBlack) {
    if (canBeBlack && dp[node][1]) return dp[node][1];
    if (!canBeBlack && dp[node][0]) return dp[node][0];

    ll b = 1, w = 1;
    for (int nex : conn[node]) {
        if (nex != last) {
            w = (w * solve(nex, node, 1)) % MOD;
            if (canBeBlack) b = (b * solve(nex, node, 0)) % MOD;
        }
    }

    dp[node][0] = w;
    dp[node][1] = (b + w) % MOD;
    return (w + b) % MOD;
}

int main() {
    boost();
    cin >> n;
    for (int i = 0; i < n - 1; i += 1) {
        cin >> one >> two;
        conn[one].pb(two);
        conn[two].pb(one);
    }

    cout << solve(1, -1, 1) << "\n";
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
