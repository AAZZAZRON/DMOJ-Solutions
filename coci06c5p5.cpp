#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <map>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 101
int n;
int numbers[MAX];
int counter = 0;
map<pii, int> memo;

int dp(int start, int ending) {
    int x = start % n;
    int y = ending % n;
    if (x < 0) x += n;
    if (y < 0) y += n;
    if (x == y) return numbers[x] % 2 == 1;
    map<pii, int>::iterator iter = memo.find(make_pair(x, y));
    if (iter != memo.end()) return iter->second;
    return memo[make_pair(x, y)] = max(dp(x, x) - dp(x + 1, y), dp(y, y) - dp(x, y - 1));
}


int main()
{
    boost();
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> numbers[i];
    }
    for (int i = 0; i < n; i += 1) {
        if (dp(i - 1, i - 1) - dp(i, i + n - 2) > 0) counter += 1;
    }
    cout << counter << endl;
    for (map<pii, int>::const_iterator iter = memo.cbegin(); iter != memo.cend(); ++iter) {
        //cout << "(" << iter->first.first << ", " << iter->first.second << ") = " << iter->second << endl;
    }
    return 0;
}
