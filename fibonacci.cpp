#include <bits/stdc++.h>
using namespace std;
#define int unsigned long long
using Matrix = array<array<int, 2>, 2>;
#define MOD 1000000007

Matrix multiply(Matrix a, Matrix b) {
    Matrix ans = {{{0, 0}, {0, 0}}};
    for (int i = 0; i < 2; i += 1) {
        for (int j = 0; j < 2; j += 1) {
            for (int k = 0; k < 2; k += 1) {
                ans[i][j] = (ans[i][j] + (a[i][k] * b[k][j]) % MOD) % MOD;
            }
        }
    }
    return ans;
}

signed main() {
    int n; cin >> n;
    n -= 1;
    Matrix M = {{{1, 1}, {1, 0}}};
    Matrix res = {{{1, 1}, {1, 0}}};
    while (n > 0) {
        if (n % 2 == 1) {
            res = multiply(res, M);
        }
        M = multiply(M, M);
        n /= 2;
    }

    cout << res[0][1] << '\n';

    return 0;
}