//
// Created by Aaron Zhu on 2022-01-09.
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

vector<pii> sweep;
int ct = 0;
int t, n, m, a, b, c, v;
int one, three;
int main() {
    boost();
    cin >> t >> n >> m;
    for (int i = 0; i < n + m; i += 1) {
        cin >> a >> b >> c;
        if (c == 0) {
            sweep.pb(mp(a, 1));
            sweep.pb(mp(b + 1, -1));
        } else {
            sweep.pb(mp(a, 3));
            sweep.pb(mp(b + 1, -3));
        }
    }
    sort(sweep.begin(), sweep.end());
    for (int i = 0; i < 2 * (n + m); i += 1) {
        a = sweep[i].first;
        v = sweep[i].second;
        if (v == 1 || v == -1) one += v;
        else three += v;
        if (three) ct += 3 * (sweep[i + 1].first - a);
        else if (one) ct += sweep[i + 1].first - a;
    }
    cout << ct << "\n";
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
