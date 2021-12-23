#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
int grid[300][300];
vector<int> top5[301][301];
int n, x, y, i, j, k;
vector<int> tmp;
int val;
int cost;
int main() {
    boost();
    cin >> n;
    for (i = 0; i < n; i += 1) {
        for (j = 0; j < n; j += 1) {
            cin >> grid[i][j];
        }
    }
    top5[n - 1][0].push_back(0);
    for (i = n - 1; i >= 0; i -= 1) {
        for (j = 1; j <= n; j += 1) {
            tmp.clear();
            val = grid[i][j - 1];
            for (int value : top5[i][j - 1]) tmp.push_back(value + val);
            for (int value : top5[i + 1][j]) tmp.push_back(value + val);
            sort(tmp.begin(), tmp.end(), greater<int>());
            for (k = 0; k < fmin(tmp.size(), 5); k += 1) {
                top5[i][j].push_back(tmp[k]);
            }
        }
    }
    cout << top5[0][n][0] << endl;
    cout << top5[0][n][1] << endl;
    cout << top5[0][n][2] << endl;
    cout << top5[0][n][3] << endl;
    cout << top5[0][n][4] << endl;

    return 0;
}
