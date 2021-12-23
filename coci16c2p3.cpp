//
// Created by Aaron Zhu on 2021-10-06.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 1000001

int n, t;
int l, r, c;
ll lC, rC;
int arr[MAX];
int main() {
    scan(n);
    for (int i = 0; i < n; i += 1) {
        scan(t);
        arr[i] = t;
    }
    l = 0; r = n - 1;
    while (l < r) {
        if (arr[l] + lC == arr[r] + rC) {
            lC = rC = 0;
            l++; r--;
        } else if (arr[l] + lC < arr[r] + rC) {
            lC += arr[l++];
            c += 1;
        } else {
            rC += arr[r--];
            c += 1;
        }
    }
    cout << c << "\n";
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
