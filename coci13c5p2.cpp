//
// Created by Aaron Zhu on 2021-10-11.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff

vector<int> arr[12];
int n, tmp;

inline void traverse(int curr, int depth) {
    if (curr == depth) {
        scan(tmp);
        arr[curr].push_back(tmp);
        return;
    }
    traverse(curr + 1, depth);
    scan(tmp);
    arr[curr].push_back(tmp);
    traverse(curr + 1, depth);
    return;
}

int main() {
    scan(n);
    traverse(1, n);
    for (int i = 1; i <= n; i += 1) {
        for (auto el : arr[i]) cout << el << " ";
        cout << "\n";
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
