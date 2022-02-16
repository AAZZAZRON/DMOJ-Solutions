//
// Created by Aaron Zhu on 2022-01-14.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 2001

ll fact[MAX];
ll inv[MAX];
int num, times, l;
unordered_map<string, int> words;
ll dp[MAX][MAX];

inline ll binpow(ll b, ll e) {
    ll ret = 1;
    while(e) {
        if (e & 1) ret = ret * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return ret;
}

inline ll choose(int n, int k) {
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
}

int main() {
    boost();
    cin >> num >> times;
    fact[0] = inv[0] = 1;
    for (int i = 1; i < MAX; i += 1) {
        fact[i] = (fact[i - 1] * i) % MOD;
        inv[i] = binpow(fact[i], MOD - 2);
    }

    for (int i = 0; i < num; i += 1) {
        string word;
        cin >> word;
        vector<int> tmp;
        for (char c : word) {
            tmp.pb((int) c);
        }
        sort(tmp.begin(), tmp.end());
        string ins = "";
        for (int c : tmp) ins += (char) c;
        if (words.find(ins) != words.end()) words[ins] += 1;
        else words[ins] = 1;
    }

    l = words.size();
    auto it = words.begin();
    dp[0][0] = 1;
    for (int i = 1; i <= l; i += 1) {
        int v = it->second;
        for (int j = 0; j <= times; j += 1) {
            dp[i][j] = (dp[i - 1][j] * (v + 1)) % MOD;
            int curr = 0;
            for (int k = 1;; k += 1) {
                curr += k;
                if (j - curr < 0 || k + 1 > v) break;
                dp[i][j] = (dp[i][j] + (dp[i - 1][j - curr] * choose(v, k + 1)) % MOD) % MOD;
            }
        }
        it++;
    }
    cout << dp[l][times] << "\n";
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
