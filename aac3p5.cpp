//
// Created by Aaron Zhu on 2021-07-31.
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
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 2001
char grid[MAX][MAX];
struct coord {
    int x, y;
};
queue<coord> q;
int moves[4][3] = {{1, 0, 0}, {0, 1, 1}, {0, -1, 2}, {-1, 0, 3}};
int boat[MAX][MAX];
int r, c, a, b, x, y, ind;

int main() {
    boost();
    cin >> r >> c;
    for (int i = 0; i < r; i += 1)
        for (int j = 0; j < c; j += 1)
            cin >> grid[i][j];
    for (int j = 0; j < c; j += 1) {
        if (grid[0][j] == '#') {
            boat[0][j] = MAX;
            q.push((coord) {0, j});
        }
    }
    while (!q.empty()) {
        coord tmp = q.front(); q.pop();
        a = tmp.x;
        b = tmp.y;
        for (int i = 0; i < 4; i += 1) {
            x = moves[i][0] + a;
            y = moves[i][1] + b;
            ind = moves[i][2];
            if (0 <= x && x < r && 0 <= y && y < c) {
                if (grid[x][y] == '#') {
                    if (boat[x][y] >= boat[a][b]) continue;
                    boat[x][y] = boat[a][b];
                    q.push((coord) {x, y});
                } else {
                    int count = 0;
                    while (0 <= x && x < r && 0 <= y && y < c && grid[x][y] == '.') {
                        count += 1;
                        x += moves[ind][0];
                        y += moves[ind][1];
                    }
                    if (0 <= x && x < r && 0 <= y && y < c && boat[x][y] < fmin(count, boat[a][b])) {
                        q.push((coord) {x, y});
                        boat[x][y] = fmin(count, boat[a][b]);
                    }
                }
            }
        }
    }
    for (int j = 0; j < c; j += 1) {
        int i = boat[r - 1][j];
        if (i == 0) cout << "-1";
        else if (i == MAX) cout << "0";
        else cout << i;
        if (j != c - 1) cout << " ";
    }
    cout << "\n";
    return 0;
}
