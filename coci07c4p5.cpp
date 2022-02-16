//
// Created by Aaron Zhu on 2022-01-26.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vii vector<pii>
#define si set<int>
#define usi unordered_set<int>
#define mii map<int, int>
#define umii unordered_map<int, int>
#define pb push_back
#define mp make_pair
#define printArr(a, len) for(int orzdaniel = 0; orzdaniel < (len); orzdaniel += 1) cout << (a)[orzdaniel] << ' '; cout << '\n';
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 1000000005
#define LLINF 1000000000000000005LL
#define MOD 1000000007
#define MAX 1000001


struct coord {
    int x, y;
    bool operator <(const struct coord t) const {
        if (y != t.y) return y > t.y;
        return x < t.x;
    }
};

int n, a, b, s, curr;
vector<coord> val;
int dp[MAX];
int b4[MAX];
stack<coord> ans;
pii BIT[MAX];

inline void update(int ind, pii v) {
    for (; ind <= MAX; ind += ind & (-ind)) BIT[ind] = max(BIT[ind], v);
}

inline pii query(int ind) {
    pii t = {0, 0};
    for (; ind >= 1; ind -= ind & (-ind)) t = max(t, BIT[ind]);
    return t;
}


int main() {
    boost();
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> a >> b;
        val.pb({a, b});
    }
    sort(val.begin(), val.end());

    for (int i = 1; i <= n; i += 1) {
        pii v = query(val[i - 1].x);
        dp[i] = v.first + 1;
        b4[i] = v.second;
        update(val[i - 1].x, {dp[i], i});
        if (dp[i] > curr) {
            curr = dp[i];
            s = i;
        }
    }

//    printArr(dp, n + 1);
//    printArr(b4, n + 1);

    do {
        ans.push(val[s - 1]);
        s = b4[s];
    } while (s != 0);


    cout << curr << "\n";
    while (!ans.empty()) {
        cout << ans.top().x << " " << ans.top().y << "\n";
        ans.pop();
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