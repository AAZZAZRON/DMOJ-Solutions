//
// Created by Aaron Zhu on 2022-01-21.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define si set<int>
#define usi unordered_set<int>
#define mii map<int, int>
#define umii unordered_map<int, int>
#define pb push_back
#define mp make_pair
#define printArr(a, len) for(int orzdaniel = 0; orzdaniel < (len); orzdaniel += 1) cout << (a)[orzdaniel] << ' '; cout << '\n';
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 1000000005
#define LLINF 1000000000000000005LL
#define MOD 1000000007
#define MAX 200001

ll n, v, m;
ll dp[MAX];
ll height[MAX];
ll cost[MAX];
ll BIT[MAX];

inline void update(ll ind, ll val) {
    for (;ind <= n; ind += ind & (-ind)) {
        BIT[ind] = max(BIT[ind], val);
    }
}

inline ll query(ll ind) {
    ll s = 0;
    for (;ind > 0; ind -= ind & (-ind)) s = max(BIT[ind], s);
    return s;
}


int main() {
    boost();
    cin >> n;
    for (int i = 1; i <= n; i += 1) cin >> height[i];
    for (int i = 1; i <= n; i += 1) cin >> cost[i];
    for (int i = 1; i <= n; i += 1) {
        v = query(height[i] - 1);
        dp[i] = v + cost[i];
        m = max(m, dp[i]);
        update(height[i], dp[i]);
    }
    cout << m << "\n";
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