#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <climits>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
ll items, trucks;
ll dp[5002];
ll amount, space, value;
ll capacity, refuel;
ll answer = INT_MIN;
int main()
{
    boost();
    for (ll i = 0; i <= 5000; i += 1) {
        dp[i] = 0;
    }
    cin >> items >> trucks;
    for (ll i = 0; i < items; i += 1) {
        cin >> amount >> space >> value;
        for (ll j = 5000; j >= 0; j -= 1) {
            for (ll ind = 0; ind * space <= j && ind <= amount; ind += 1) {
                dp[j] = max(dp[j], dp[j - (ind * space)] + value * ind);
            }
        }
    }
    for (ll i = 0; i < trucks; i += 1) {
        cin >> capacity >> refuel;
        answer = max(answer, dp[capacity] - refuel);
    }
    cout << answer << endl;
    return 0;
}
