//
// Created by Aaron Zhu on 2021-12-22.
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

int memo[3001][101][101][2];
int pies[3001];
int bag[101];
int n, m;

inline int recurse(int ind, int l, int r, int took) {
    if (memo[ind][l][r][took]) return memo[ind][l][r][took];

    int maximum = 0;
    if (ind == n) {
        int take;
        if (took) take = (int) ((r - l + 1) / 2.0);
        else take = (int) ((r - l) / 2.0);

        int s = 0;
        for (int i = l + take; i < r; i += 1) s += bag[i];
        memo[ind][l][r][took] = s;
        return s;
    }
    if (!took) maximum = max(maximum, pies[ind] + recurse(ind + 1, l, r, 1));
    maximum = max(maximum, recurse(ind + 1, l, r, 0));
    if (l < r) {
        maximum = max(maximum, pies[ind] + recurse(ind + 1, l + 1, r, 1));
        if (!took) maximum = max(maximum, bag[r - 1] + recurse(ind, l, r - 1, 1));
    }
    memo[ind][l][r][took] = maximum;
    return memo[ind][l][r][took];
}

int main() {
    boost();
    cin >> n;
    for (int i = 0; i < n; i += 1) cin >> pies[i];
    cin >> m;
    for (int i = 0; i < m; i += 1) cin >> bag[i];
    sort(bag, bag + m);
    cout << recurse(0, 0, m, 0) << "\n";
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
