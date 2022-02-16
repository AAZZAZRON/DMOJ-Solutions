//
// Created by Aaron Zhu on 2022-01-17.
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
#define MAX 100001
int sieve[MAX];
vector<int> primes;
int t, n, w;
int dp[MAX];
int main() {
    boost();
    sieve[0] = sieve[1] = 1;
    for (int i = 2; i < MAX; i += 1) {
        if (!sieve[i]) {
            primes.pb(i);
            for (int j = i; j < MAX; j += i) sieve[j] = 1;
        }
    }
    for (int i = 0; i < MAX; i += 1) {
        for (int j : primes) {
            if (i - j <= 0) break;
            if (!dp[i - j]) {
                dp[i] = 1;
                w = i;
                break;
            }
        }
    }
    cin >> t;
    for (int q = 0; q < t; q += 1) {
        cin >> n;
        w = -1;
        for (int j = n; j > 0; j -= 1) {
            if (dp[j]) {
                w = j;
                break;
            }
        }
        if (w == -1) {
            cout << "-1\n";
            continue;
        }
        for (int i = 1; i <= n; i += 1) {
            if (i < w) cout << i;
            else if (i == w) cout << n;
            else cout << i - 1;
            if (i == n) cout << "\n";
            else cout << " ";
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
