//
// Created by Aaron Zhu on 2021-12-20.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 5000001

int arr[MAX];
int n, t, ct;

int main() {
    scan(n);
    for (int i = 0; i < n; i += 1) {
        scan(t);
        arr[t] = t;
    }

    for (int i = 1; i < MAX; i += 1) {
        if (arr[i]) {
            int j = i;
            int v = arr[i];
            while (true) {
                if (j + v >= MAX) {
                    ct += 1;
                    break;
                }
                if (arr[j + v] != j + v) j += v;
                else {
                    arr[j + v] = v;
                    break;
                }
            }
        }
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