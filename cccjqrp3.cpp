//
// Created by Aaron Zhu on 2021-12-29.
//

#include <iostream>
using namespace std;

int main()
{
    unsigned long long a, b, c;
    unsigned long long MOD = 42069900169420;
    cin >> a >> b >> c;
    a %= MOD;
    b %= MOD;
    c %= MOD;
    unsigned long long ans = (((a + b) % MOD) + c) % MOD;
    cout << ans << "\n";
    return 0;
}