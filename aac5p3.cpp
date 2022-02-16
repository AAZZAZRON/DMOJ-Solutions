//
// Created by Aaron Zhu on 2022-01-30.
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
#define MAX 200001

int n, k, a, b, d;
vii conn[MAX];
int skills[MAX];
int ans[MAX];

inline void dfs(int node, int one, int two) {
    if (one >= two) return;
    ans[node] += two - one;
    if (conn[node].size() == 0) return;
    sort(conn[node].begin(), conn[node].end());
    int tmp = one;
    for (int i = 1; i < conn[node].size() && tmp != two; i += 1) {
        int nex = conn[node][i - 1].second;
        int diff = (conn[node][i - 1].first + conn[node][i].first) / 2;
        int l = tmp;
        int r = two;

        while (r - l > 1) {
            int mid = (l + r) / 2;
            if (skills[mid] <= diff) l = mid;
            else r = mid;
        }
        if (skills[l] <= diff) {
            dfs(nex, tmp, l + 1);
            tmp = l + 1;
        }
    }
    dfs(conn[node][conn[node].size() - 1].second, tmp, two);
}

int main() {
    boost();
    cin >> n >> k;
    for (int i = 0; i < n - 1; i += 1) {
        cin >> a >> b >> d;
        conn[a].pb({d, b});
    }
    for (int i = 0; i < k; i += 1) cin >> skills[i];
    sort(skills, skills + k);
    dfs(1, 0, k);
    //for (int i = 0; i < k; i += 1) dfs(1, i, i + 1);
    for (int i = 1; i <= n; i += 1) cout << ans[i] << " \n"[i == n];
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