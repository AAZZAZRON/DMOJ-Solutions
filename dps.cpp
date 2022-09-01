//
// Created by Aaron Zhu on 2022-03-24.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vii vector<pii>
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
#define MAX 10001

int memo[MAX][101];
string n;
int d, len;

inline int memoize(int ind, int mod, bool isBegin, bool takeAll, int ans=0) {
    if (takeAll && memo[ind][mod] != -1) return memo[ind][mod];
    else if (ind == len) {
        // cout << ans << " " << mod << '\n';
        return mod == 0;
    }

    int ct = 0;
    if (isBegin) ct = (ct + memoize(ind + 1, mod, true, true)) % MOD;
    for (int i = 0; i < 10; i += 1) {
        if (i == 0 && isBegin) continue;
        else if (!takeAll && i > n[ind] - '0') break;
        else if (!takeAll && i == n[ind] - '0') ct = (ct + memoize(ind + 1, (mod + i) % d, false, false, ans * 10 + i)) % MOD;
        else ct = (ct + memoize(ind + 1, (mod + i) % d, false, true, ans * 10 + i)) % MOD;
    }
    if (!isBegin) return memo[ind][mod] = ct;
    return ct;
}

signed main() {
    memset(memo, -1, sizeof(memo));
    boost();
    cin >> n;
    cin >> d;
    len = n.length();
    cout << memoize(0, 0, true, false) - 1 << '\n';
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