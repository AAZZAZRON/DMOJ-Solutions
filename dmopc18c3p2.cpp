//
// Created by Aaron Zhu on 2023-04-10.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
//ifstream IN;
//ofstream OUT;

#define MAX 100005
int dp[MAX][4]; // 00, 01, 10, 11
int yes[MAX];
int no[MAX];

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    int n; cin >> n;
    for (int i = 1; i <= n; i += 1) cin >> yes[i];
    for (int i = 1; i <= n; i += 1) cin >> no[i];

    for (int i = 1; i <= n; i += 1) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2]) + no[i];
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + yes[i];
        dp[i][2] = max(dp[i - 1][1], dp[i - 1][3]) + no[i];
        dp[i][3] = dp[i - 1][1] + yes[i];
    }

    int m = dp[n][0];
    for (int i = 0; i < 4; i += 1) m = max(m, dp[n][i]);
    cout << m << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}