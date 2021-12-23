//
// Created by Aaron Zhu on 2021-08-09.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <cassert>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define EXP 31
#define MOD 126458753
ll h, window;
string one, two;

inline ll ascii(char c) {
    return int(c) - 96;
}

int main() {
    boost();
    cin >> one >> two;
    int lenOne = one.length();
    int lenTwo = two.length();
    ll powers[lenTwo + 1];
    powers[0] = 1;
    for (int i = 1; i < lenTwo; i += 1) powers[i] = (powers[i - 1] * EXP) % MOD;
    for (int i = 0; i < lenTwo; i += 1) {
        h = (h + ascii(two[i]) * powers[lenTwo - i - 1]) % MOD;
        window = (window + ascii(one[i]) * powers[lenTwo - i - 1]) % MOD;
    }
    if (window == h) {
        cout << "0\n";
        return 0;
    }
    for (int i = lenTwo; i < lenOne; i += 1) {
        window = (window - ascii(one[i - lenTwo]) * powers[lenTwo - 1]) % MOD;
        window = (window % MOD + MOD) % MOD;
        window = (window * EXP + ascii(one[i])) % MOD;
        assert(window > 0);
        if (window == h) {
            cout << i - lenTwo + 1 << "\n";
            return 0;
        }
    }
    cout << "-1\n";
    return 0;
}
