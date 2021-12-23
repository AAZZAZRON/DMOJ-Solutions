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

inline ll ascii(char c) {
    return int(c) - 'A' + 1;
}
ll a, b;
string one, two;
int depth = 0;
ll power = 1;

int main() {
    boost();
    cin >> one >> two;
    int lenOne = one.length();
    int length = fmin(lenOne, two.length());
    a += ascii(one[lenOne - 1]);
    b += ascii(two[0]);
    if (a == b) depth = 1;
    for (int i = 1; i < length; i += 1) {
        power = (power * EXP) % MOD;
        a = (a + ascii(one[lenOne - 1 - i]) * power) % MOD;
        b = (b * EXP + ascii(two[i])) % MOD;
        if (a == b) depth = i + 1;
    }
    cout << one.substr(0, lenOne - depth) << two << "\n";
    return 0;
}
