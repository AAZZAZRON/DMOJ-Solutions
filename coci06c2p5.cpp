//
// Created by Aaron Zhu on 2021-08-08.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <cassert>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 402
int psa[MAX][MAX];
int r, c;
int maximum = 0;
char s;
int main() {
    boost();
    cin >> r >> c;
    for (int i = 1; i <= r; i += 1) {
        for (int j = 1; j <= c; j += 1) {
            cin >> s;
            if (s == 'X') psa[i][j] = psa[i][j - 1] + 1;
            else psa[i][j] = psa[i][j - 1];
        }
    }
    for (int i = 1; i <= c; i += 1) {
        for (int j = i; j <= c; j += 1) {
            int cons = 0;
            for (int k = 1; k <= r; k += 1) {
                if (psa[k][j] - psa[k][i - 1] == 0) cons += 1;
                else {
                    if (cons) maximum = max(maximum, 2 * (j - i + 1) + 2 * cons);
                    cons = 0;
                }
            }
            if (cons) maximum = max(maximum, 2 * (j - i + 1) + 2 * cons);
        }
    }
    cout << maximum - 1 << "\n";
}
