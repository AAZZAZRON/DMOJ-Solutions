//
// Created by Aaron Zhu on 2022-03-23.
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
#define MAX 1050
#define int ll

int n, t, len, valid;
string s;
int memo[MAX][MAX];

inline int memoize(int ind, int used, bool isBegin, bool takeAll, int ans=0) {
    if (takeAll && memo[ind][used] != -1) return memo[ind][used];
    else if (ind == len) {
        return (used & valid) == valid;
    }
    int ct = 0;
    if (isBegin) ct = (ct + memoize(ind + 1, used, true, true)) % MOD;

    for (int el = 0; el < 10; el++) {
        if (isBegin && el == 0) continue;
        else if (!takeAll && el > s[ind] - '0') break;
        else if (!takeAll && el == s[ind] - '0') ct = (ct + memoize(ind + 1, used | 1 << el, false, false, ans * 10 + el)) % MOD;
        else ct = (ct + memoize(ind + 1, used | 1 << el, false, true, ans * 10 + el)) % MOD;
    }
    if (takeAll) memo[ind][used] = ct;
    return ct;
}

signed main() {
    memset(memo, -1, sizeof(memo));
    boost();
    cin >> n;
    int base = 0;
    for (int i = 0; i < n; i += 1) {
        cin >> t;
        if (t == 0 && n == 1) base = 1;
        valid |= 1 << t;
    }
    cin >> s;
    len = s.length();
    cout << base + memoize(0, 0, true, false) << '\n';
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