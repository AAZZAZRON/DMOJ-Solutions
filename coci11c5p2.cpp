//
// Created by Aaron Zhu on 2022-04-21.
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
#define int ll

int arr[MAX];
int n, m;
signed main() {
    scan(n); scan(m);
    for (int i = 0; i < n; i++) scan(arr[i]);

    int l = 0; int r = 2e9;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            cnt += fmax(arr[i] - mid, 0);
        }
        //cout << l << ' ' << r << ' ' << mid << ' ' << cnt << '\n';
        if (cnt < m) r = mid;
        else l = mid;
    }
    cout << l << '\n';
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