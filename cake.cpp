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
#define MAX 5002
using namespace std;
int n, m, k, q, i, j, xOne, xTwo, yOne, yTwo, num;
ll answer = 0;
ll before;
ll cake[MAX][MAX];
int main()
{
    boost();
    cin >> n >> m >> k;
    // update
    for (q = 0; q < k; q += 1) {
        cin >> xOne >> yOne >> xTwo >> yTwo;
        cake[xOne][yOne] += 1;
        cake[xOne][yTwo + 1] -= 1;
        cake[xTwo + 1][yOne] -= 1;
        cake[xTwo + 1][yTwo + 1] += 1;
    }

    // create array
    for (i = 1; i <= n; i += 1) {
        for (j = 1; j <= m; j += 1) {
            cake[i][j] += cake[i - 1][j] + cake[i][j - 1] - cake[i - 1][j - 1];
        }
    }
    // initialize psa
    for (i = 1; i <= n; i += 1) {
        before = 0;
        for (j = 1; j <= m; j += 1) {
            before += cake[i][j];
            cake[i][j] = before + cake[i - 1][j];
        }
    }

    cin >> num;
    for (q = 0; q < num; q += 1) {
        cin >> xOne >> yOne >> xTwo >> yTwo;
        cout << cake[xTwo][yTwo] - cake[xTwo][yOne - 1] - cake[xOne - 1][yTwo] + cake[xOne - 1][yOne - 1] << endl;
    }
    return 0;
}
