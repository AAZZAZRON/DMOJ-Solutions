//
// Created by Aaron Zhu on 2022-01-11.
//

#include "../../bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 101

int n, p, b, one, two, t;
int popcorn[MAX][MAX][MAX];
bool boulder[MAX][MAX][MAX];
int dp[MAX][MAX][MAX];
int moves[5][2] = {{0, 0}, {1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int main() {
    boost();
    cin >> n >> p >> b;
    cin >> one >> two;
    for (int i = 0; i < MAX; i += 1) {
        for (int j = 0; j < MAX; j += 1) {
            for (int k = 0; k < MAX; k += 1) {
                dp[i][j][k] = -1;
            }
        }
    }
    dp[0][one][two] = 0;
    for (int i = 0; i < p; i += 1) {
        cin >> one >> two >> t;
        popcorn[t][one][two] += 1;
    }
    for (int i = 0; i < b; i += 1) {
        cin >> one >> two >> t;
        boulder[t][one][two] = 1;
    }
    for (int q = 1; q < MAX; q += 1) {
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < n; j += 1) {
                if (dp[q - 1][i][j] != -1) {
                    for (auto move: moves) {
                        int x = move[0] + i;
                        int y = move[1] + j;
                        if (0 <= x && x < n && 0 <= y && y < n) {
                            if (!boulder[q][x][y]) {
                                dp[q][x][y] = max(dp[q][x][y], dp[q - 1][i][j] + popcorn[q][x][y]);
                            } else {
                                dp[q][x][y] = max(dp[q][x][y], dp[q - 1][i][j] / 2);
                            }
                        }
                    }
                }
            }
        }
    }
    int m = -1;
    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < n; j += 1) {
            m = max(m, dp[100][i][j]);
        }
    }
    cout << m << "\n";
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
