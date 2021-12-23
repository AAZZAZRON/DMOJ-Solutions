//
// Created by Aaron Zhu on 2021-07-12.
//

#include <iostream>
#include <algorithm>
#define ll long long
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 503
#define MOD 1000000007

int c, r, q, x, y, w, h, n, one, two;
ll diff[MAX][MAX], maxLength[MAX][MAX], maxSum[MAX][MAX];
int moves[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

inline void longestPath(int a, int b) {
    ll val = 0;
    ll path = 0;
    for (int i = 0, fX, fY; i < 4; i += 1) {
        fX = moves[i][0] + a;
        fY = moves[i][1] + b;
        if (1 <= fX && fX <= r && 1 <= fY && fY <= c && diff[fX][fY] > diff[a][b]) {
            if (maxLength[fX][fY] == 0) longestPath(fX, fY);
            if (path < maxLength[fX][fY]) {
                path = maxLength[fX][fY];
                val = maxSum[fX][fY];
            } else if (maxLength[fX][fY] == path) val = max(val, maxSum[fX][fY]);
        }
    }
    maxLength[a][b] = path + 1;
    maxSum[a][b] = val + diff[a][b];
}

inline void diffify(const int c1, const int r1, const int c2, const int r2, const int v) {
    diff[c1][r1] += v;
    diff[c1][r2] -= v;
    diff[c2][r1] -= v;
    diff[c2][r2] += v;
}

inline void PSAify() {
    for (int i = 1; i <= r; i += 1)
        for (int j = 1; j <= c; j += 1)
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
}

int main() {
    scan(c); scan(r); scan(q);
    for (int i = 0; i < q; i += 1) {
        scan(y); scan(x); scan(h); scan(w); scan(n);
        diffify(x, y, x + w, y + h, n);
        diffify(x + w, y, x + w + 1, y + h, -n * w);
        diffify(x, y + h, x + w, y + h + 1, -n * h);
        diffify(x + w, y + h, x + w + 1, y + h + 1, n * h * w);
    }
    PSAify(); PSAify();
    scan(two); scan(one);
    longestPath(one, two);
    cout << maxSum[one][two] % MOD << "\n";
    return 0;
}
