//
// Created by Aaron Zhu on 2023-02-14.
//

#include <bits/stdc++.h>

#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
#define pii pair<int, int>

ifstream IN;
ofstream OUT;
#define MAX 355
// let dp[i][j] be the largest rectangle ending at (i, j)
int dp[MAX][MAX];
bool vis[MAX][MAX];
vector<pii> queries;
int pAns[MAX * MAX];
int ans = 0;
int r, c;

inline void checkDp(int i, int j) {
    if (vis[i][j]) {
        int tmp = dp[i - 1][j - 1];
        tmp = min(tmp, min(dp[i - 1][j], dp[i][j - 1]));
        if (tmp + 1 > dp[i][j]) {
            dp[i][j] = tmp + 1;
            ans = max(ans, tmp + 1);
            if (i + 1 <= r && j + 1 <= c) checkDp(i + 1, j + 1);
            if (i + 1 <= r) checkDp(i + 1, j);
            if (j + 1 <= c) checkDp(i, j + 1);
        }
    }
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    IN.open("../in.txt");
    OUT.open("../out.txt");

    cin >> r >> c;
    for (int i = 0; i < MAX; i += 1) {
        for (int j = 0; j < MAX; j += 1) {
            vis[i][j] = 1;
        }
    }
    int m; cin >> m;
    for (int i = 0; i < m; i += 1) {
        int a, b; cin >> a >> b;
        queries.push_back({a, b});
        vis[a][b] = 0;
    }

    for (int i = 1; i <= r; i += 1) {
        for (int j = 1; j <= c; j += 1) {
            if (vis[i][j]) {
                int tmp = dp[i - 1][j - 1];
                tmp = min(tmp, min(dp[i - 1][j], dp[i][j - 1]));
                dp[i][j] = tmp + 1;
                ans = max(ans, tmp + 1);
            }
        }
    }

    for (int i = m - 1; i >= 0; i -= 1) {
        pAns[i] = ans;
        int a = queries[i].first;
        int b = queries[i].second;
        vis[a][b] = 1;
        checkDp(a, b);
//        for (int j = 1; j <= r; j += 1) {
//            printArr(dp[j], c + 1);
//        }
//        cout << '\n';
    }

    for (int i = 0; i < m; i += 1) cout << pAns[i] << '\n';


    IN.close();
    OUT.close();
    return 0;
}