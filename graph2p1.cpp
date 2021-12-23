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
#define MAX 1001
int num;
int used[MAX];
int grid[MAX][MAX];
int val;
vector<int> n;
queue<int> q;

int main()
{
    boost();
    cin >> num;
    for (int i = 1; i <= num; i += 1) {
        for (int j = 1; j <= num; j += 1) {
            cin >> grid[i][j];
        }
    }

    for (int i = 1; i <= num; i += 1) {
        if (used[i]) continue;
        n.clear();
        n.push_back(i);
        q.push(i);
        used[i] = 1;
        while (!q.empty()) {
            val = q.front(); q.pop();
            for (int j = 1; j <= num; j += 1) {
                if (grid[val][j] and !used[j]) {
                    used[j] = 1;
                    q.push(j);
                    n.push_back(j);
                }
            }
        }
        sort(n.begin(), n.end());
        for (int j : n) {
            cout << j << " ";
        }
        cout << endl;
    }
    
    return 0;
}
