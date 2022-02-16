//
// Created by Aaron Zhu on 2022-01-09.
//

#include "../../bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 2001

int r, c;
bool vis[MAX][MAX];
char grid[MAX][MAX];
int moves[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
queue<pii> q;
vector<int> areas;
string line;

inline int bfs(int one, int two) {
    q.push(make_pair(one, two));
    vis[one][two] = 1;
    int ct = 0;
    while (!q.empty()) {
        int a = q.front().first;
        int b = q.front().second;
        q.pop();
        if (a % 2 == 1 && b % 2 == 1) {
            ct += 1;
        }
        for (int i = 0; i < 4; i += 1) {
            int x = moves[i][0] + a;
            int y = moves[i][1] + b;
            if (0 <= x && x < r && 0 <= y && y < c && !vis[x][y] && grid[x][y] == '.') {
                vis[x][y] = 1;
                q.push(make_pair(x, y));
            }
        }
    }
    return ct;
}

int main() {
    boost();
    cin >> r >> c;
    r = 2 * r + 1;
    c = 2 * c + 1;
    for (int i = 0; i < r; i += 1) {
        cin >> line;
        for (int j = 0; j < c; j += 1) {
            grid[i][j] = line.at(j);
        }
    }
    for (int i = 0; i < r; i += 1) {
        for (int j = 0; j < c; j += 1) {
            if (!vis[i][j] && grid[i][j] == '.') {
                areas.push_back(bfs(i, j));
            }
        }
    }
    sort(areas.begin(), areas.end());
    cout << areas[3] << " " << areas[2] << " " << areas[1] << " " << areas[0] << "\n";

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
