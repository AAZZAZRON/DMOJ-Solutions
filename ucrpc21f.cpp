//
// Created by Aaron Zhu on 2022-01-10.
//

#include "bits/stdc++.h"
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
#define MAX 1001
struct node {
    int v, x, y;
    bool operator<(const node one) const {
        return v > one.v;
    };
};
int n, t;
priority_queue<node> q;
bool vis[MAX][MAX];
int minD[MAX][MAX];
bool grid[MAX][MAX];
int moves[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int main() {
    boost();
    cin >> n >> t;
    for (int i = 0; i < n; i += 1) {
        string line;
        cin >> line;
        for (int j = 0; j < n; j += 1) {
            minD[i][j] = INF;
            if (line.at(j) == 'b') grid[i][j] = 1;
        }
    }
    minD[0][0] = 0;
    q.push((node) {0, 0, 0});
    while (!q.empty()) {
        int v = q.top().v;
        int a = q.top().x;
        int b = q.top().y;
        q.pop();
        if (minD[a][b] != v) continue;
        for (int i = 0; i < 4; i += 1) {
            int x = moves[i][0] + a;
            int y = moves[i][1] + b;
            if (0 <= x && x < n && 0 <= y && y < n && !vis[x][y]) {
                int cost = v + grid[x][y] * t + 1;
                if (cost < minD[x][y]) {
                    minD[x][y] = cost;
                    q.push((node) {cost, x, y});
                }
            }
        }
        vis[a][b] = 1;
    }
//    for (int i = 0; i < n; i += 1) {
//        for (int j = 0; j < n; j += 1) {
//            cout << minD[i][j] << "\t";
//        }
//        cout << '\n';
//    }
    cout << minD[n - 1][n - 1] << "\n";
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
