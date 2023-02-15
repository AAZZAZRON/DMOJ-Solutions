#include "bits/stdc++.h"
using namespace std;
#define MAX 1000000
#define MOD 1000000007
#define int long long

int fact[MAX];

int gcdExtended(int a, int b, int* x, int* y) {
    if (a == 0) {
        *x = 0, *y = 1;
        return b;
    }
    int x1, y1;
    int gcd = gcdExtended(b % a, a, &x1, &y1) % MOD;
    x1 %= MOD;
    y1 %= MOD;
    *x = ((y1 % MOD) - ((b / a) * x1) % MOD + MOD) % MOD;
    *y = x1 % MOD;
    return gcd;
}

inline int modInverse(int a) {
    int x, y;
    int g = gcdExtended(a, MOD, &x, &y);
    int res = (x % MOD + MOD) % MOD;
    return res;
}

inline int cr(int n, int i) {
    int x, y;
    int num = fact[n] % MOD;
    int inv = modInverse((fact[n - i] * fact[i]) % MOD) % MOD;
    int ans = (num * inv) % MOD;
    return ans;
}

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    int n; cin >> n;
    int ct = 0;
    fact[0] = 1;
    for (int i = 1; i < MAX; i += 1) fact[i] = (fact[i - 1] * i) % MOD;
    for (int i = 1; n > 0; i += 1, n -= 3) ct = (ct + cr(n + i - 1, i)) % MOD;
    cout << ct << '\n';
    return 0;
}