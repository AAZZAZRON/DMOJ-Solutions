//
// Created by Aaron Zhu on 2021-11-10.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff

ll p, y, t;
bool canDo(ll match) {
    ll coins = 0;
    for (int i = 0; i < y; i += 1) {
        coins += match;
        coins += (ll) (coins * p / 100);
        if (coins >= t) return 1;
    }
    return 0;
}

ll low = 0, high = 1e16;
int main() {
    scan(p); scan(y); scan(t);
    while (high - low > 1) {
        ll mid = (low + high) / 2;
        if (canDo(mid)) high = mid;
        else low = mid;
    }
    cout << high << "\n";
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
