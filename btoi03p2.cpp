#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
#define MAX 10001

//#define cin IN
//#define cout OUT

//ifstream IN;
//ofstream OUT;
vector<int> conn[MAX];
int dp[MAX][4];

inline int dfs(int node, int prev, int cantTake) {
    int m = MAX * 5;
    if (dp[node][cantTake] != MAX * 5) return dp[node][cantTake];
    for (int cost = 1; cost <= 3; cost += 1) {
        if (cost == cantTake) continue;
        int tmp = cost;
        for (int nex : conn[node]) if (nex != prev) tmp += dfs(nex, node, cost);
        m = min(m, tmp);
    }
    dp[node][cantTake] = m;
    return m;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");
    int n; cin >> n;
    for (int i = 0; i < n - 1; i += 1) {
        int a, b; cin >> a >> b;
        conn[a].push_back(b);
        conn[b].push_back(a);
    }

    // let dp[i][j] be the minimum cost to build
    // subtree rooted at i assuming u cant build
    // i with cost of j
    for (int i = 0; i < MAX; i += 1) {
        for (int j = 0; j < 4; j += 1) {
            dp[i][j] = MAX * 5;
        }
    }

    int ans = MAX * 5;
    for (int i = 1; i <= 3; i += 1) {
        dfs(1, -1, i);
        ans = min(ans, dp[1][i]);
    }

    cout << ans << '\n';

    //IN.close();
    //OUT.close();
    return 0;
}
