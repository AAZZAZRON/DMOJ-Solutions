//
// Created by Aaron Zhu on 2021-06-15.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
int n;
#define MAX 2003002
pair<int, pii> connections[MAX];
pii values[2002];
int dp[2002], best[2002], pdp[2002];
int x, y, tmp, dist;
int one, two;
int counter = -1;
int main()
{
    boost();
    cin >> n;
    values[0] = make_pair(0, 0);
    for (int i = 1; i <= n; i += 1) {
        cin >> x >> y;
        values[i] = make_pair(x, y);
    }

    for (int i = 0; i < n; i += 1) {
        for (int j = i + 1; j <= n; j += 1) {
            counter += 1;
            int dX = (values[i].first - values[j].first);
            int dY = (values[i].second - values[j].second);
            connections[counter] = make_pair(dX * dX + dY * dY, make_pair(i, j));
        }
    }
    sort(connections, connections + MAX);

    for (int i = MAX - counter - 1; i < MAX; i += 1) {
        dist = connections[i].first;
        one = connections[i].second.first;
        two = connections[i].second.second;
        if (best[one] != dist) pdp[one] = dp[one];
        if (best[two] != dist) pdp[two] = dp[two];
        if (one != 0) {
            dp[one] = max(dp[one], pdp[two] + 1);
            dp[two] = max(dp[two], pdp[one] + 1);
        } else dp[one] = max(dp[one], pdp[two]);
        best[one] = dist;
        best[two] = dist;
    }
    cout << dp[0] + 1 << endl;
    return 0;
    for (int i = 0; i <= n; i += 1) {
        cout << dp[i] << " ";
    }
    return 0;
}
