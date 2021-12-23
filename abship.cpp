//
// Created by Aaron Zhu on 2021-08-03.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
struct coord{int x, y;};
#define MAX 501
char grid[MAX][MAX];
int ships[MAX][MAX];
int counter[MAX * MAX / 2];
int original[MAX * MAX / 2];
int r, c, s;
int oC, cC;
int n = 1;
double total;
queue<coord> q;
int moves[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int main() {
    boost();
    cin >> r >> c >> s;
    for (int i = 0; i < r; i += 1) for (int j = 0; j < c; j += 1) cin >> grid[i][j];
    for (int i = 0; i < r; i += 1)
        for (int j = 0; j < c; j += 1) {
            if (grid[i][j] == 'X' && !ships[i][j]) {
                q.push((coord) {i, j});
                ships[i][j] = n;
                while (!q.empty()) {
                    coord tmp = q.front(); q.pop();
                    int a = tmp.x;
                    int b = tmp.y;
                    for (int k = 0; k < 4; k += 1) {
                        int x = moves[k][0] + a;
                        int y = moves[k][1] + b;
                        if (0 <= x && x < r && 0 <= y && y < c && grid[x][y] == 'X' && !ships[x][y]) {
                            ships[x][y] = n;
                            q.push((coord) {x, y});
                        }
                    }
                }
                n += 1;
            }
        }
    // create original window
    for (int a = 0; a < s; a += 1) {
        for (int b = 0; b < s; b += 1) {
            if (ships[a][b] != 0) {
                original[ships[a][b]] += 1;
                if (original[ships[a][b]] == 1) oC += 1;
            }
        }
    }

    for (int i = s - 1; i < r; i += 1) {
        copy(begin(original), end(original), begin(counter));
        cC = oC;
        total += cC;
        for (int j = s; j < c; j += 1) {
            for (int k = i - s + 1; k <= i; k += 1) {
                if (ships[k][j - s] != 0) {
                    counter[ships[k][j - s]] -= 1; // remove
                    if (counter[ships[k][j - s]] == 0) cC -= 1;
                }
                if (ships[k][j] != 0) {
                    counter[ships[k][j]] += 1; // add
                    if (counter[ships[k][j]] == 1) cC += 1;
                }
            }
            total += cC;
        }
        for (int j = 0; j < s; j += 1) {
            if (ships[i - s + 1][j] != 0) {
                original[ships[i - s + 1][j]] -= 1;
                if (original[ships[i - s + 1][j]] == 0) oC -= 1;
            }
            if (ships[i + 1][j] != 0) {
                original[ships[i + 1][j]] += 1;
                if (original[ships[i + 1][j]] == 1) oC += 1;
            }
        }
    }
    cout << setprecision(8) << total / (double) ((r - s + 1) * (c - s + 1)) << "\n";
    return 0;
}
