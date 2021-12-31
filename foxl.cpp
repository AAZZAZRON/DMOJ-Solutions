//
// Created by Aaron Zhu on 2021-12-30.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff


map<int, int> friends;
int n, m, one, two;

inline int dsuFind(int a) {
    return friends[a] == a ? a : friends[a] = dsuFind(friends[a]);
}

inline void dsuUnion(int x, int y) {
    if (friends.find(x) == friends.end()) friends[x] = x;
    if (friends.find(y) == friends.end()) friends[y] = y;
    int f1 = dsuFind(x);
    int f2 = dsuFind(y);
    if (f1 == f2) return;
    friends[f1] = f2;
    n -= 1;
}

int main() {
    scan(n); scan(m);
    for (int i = 0; i < m; i += 1) {
        scan(one); scan(two);
        dsuUnion(one, two);
    }
    cout << n << "\n";
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
