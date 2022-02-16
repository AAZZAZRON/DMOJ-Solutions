//
// Created by Aaron Zhu on 2022-01-19.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define vi vector<int>
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
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 500001
int n;
char arr[MAX];
int l, m, s;
int mS, lS, sM, lM, sL, mL;

int main() {
    n = 1;
    while (true) {
        char c = getchar();
        if (c == '\n') break;
        arr[n] = c;
        n += 1;
        if (c == 'L') l += 1;
        else if (c == 'M') m += 1;
        else s += 1;
    }
    n -= 1;
    for (int i = 1; i <= l; i += 1) {
        if (arr[i] == 'S') sL += 1;
        else if (arr[i] == 'M') mL += 1;
    }
    for (int i = l + 1; i <= l + m; i += 1) {
        if (arr[i] == 'S') sM += 1;
        else if (arr[i] == 'L') lM += 1;
    }
    for (int i = l + m + 1; i <= n; i += 1) {
        if (arr[i] == 'M') mS += 1;
        else if (arr[i] == 'L') lS += 1;
    }
    //cout << mS << " " << lS << " " << sM << " " << lM << " " << sL << " " << mL << "\n";
    //printArr(arr, n + 1);
    int ct = 0, t;
    t = min(mS, sM);ct += t;mS -= t;sM -= t;
    t = min(lS, sL);ct += t;lS -= t;sL -= t;
    t = min(mL, lM);ct += t;mL -= t;lM -= t;
    //cout << ct << " " << mS << " " << lS << " " << sM << " " << lM << " " << sL << " " << mL << "\n";
    int q[6] = {mS, lS, sM, lM, sL, mL};
    sort(q, q + 6);
    ct += 2 * q[5];
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
