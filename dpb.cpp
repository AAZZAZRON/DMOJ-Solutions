#include <iostream>
#include <vector>
#include <set>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
int num, jump;
int dp[200001], costs[200001];
int main()
{
    cin >> num >> jump;
    for (int i = 1; i < num + 1; i += 1) {
        cin >> costs[i];
        dp[i] = 999999999;
    }

    dp[1] = 0;
    
    for (int i = 1; i <= num; i += 1) {
        for (int j = 1; j < jump + 1; j += 1) {
            if (i + j <= num) {
                dp[i + j] = min(dp[i + j], dp[i] + abs(costs[i + j] - costs[i]));
            }
        }
    }
    cout << dp[num] << endl;
    return 0;
}
