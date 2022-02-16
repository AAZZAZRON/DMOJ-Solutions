#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vii vector<pii>
#define si set<int>
#define usi unordered_set<int>
#define mii map<int, int>
#define umii unordered_map<int, int>
#define pb push_back
#define mp make_pair
#define printArr(a, len) for(int orzdaniel = 0; orzdaniel < (len); orzdaniel += 1) cout << (a)[orzdaniel] << ' '; cout << '\n';
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 1000000005
#define LLINF 1000000000000000005LL
#define MOD 1000000007
#define MAX 1501

int n, m, k;
int arr[MAX][MAX];
int vis[MAX][MAX];
int moves[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int main() {
    boost();
    cin >> n >> m >> k;
    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < m; j += 1) {
            cin >> arr[i][j];
            if (arr[i][j]) vis[i][j] = 1;
        }
    }

    for (int q = 1; q <= k; q += 1) {
        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < m; j += 1) {
                if (vis[i][j] == q) {
                    for (int w = 0; w < 4; w += 1) {
                        int x = moves[w][0] + i;
                        int y = moves[w][1] + j;
                        if (0 <= x && x < n && 0 <= y && y < m) {
                            if (!vis[x][y] || (vis[x][y] == q + 1 && arr[x][y] > arr[i][j])) {
                                vis[x][y] = q + 1;
                                arr[x][y] = arr[i][j];
                            }
                        }
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < m; j += 1) {
            cout << arr[i][j] << " \n"[j == m - 1];
        }
    }

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