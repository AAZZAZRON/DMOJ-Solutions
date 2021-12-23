#include <iostream>
#include <vector>
#include <set>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;

bool itch[2000001];
long long dp[2000001];
set<long long> drops;
long long reach, jump, num, start, ending, number;
long long minimum = 3000000;


int main()
{
    boost();

    scan(reach);
    scan(jump);
    scan(num);
    for (int i = 0; i < num; i += 1) {
        scan(start);
        scan(ending);
        for (int j = start; j < ending + 1; j += 1) {
            itch[j] = true;
        }
    }
    dp[0] = 0;
    drops.insert(0);
    for (int i = 1; i < 2000001; i += 1) {
        if (0 <= i - jump && !itch[i] && !itch[i - jump]) {
            dp[i] = min(dp[i - jump] + 1, dp[*drops.begin() % (1 << 25)] + 2);
        } else {
            dp[i] = 2000001;
        }
        drops.insert((dp[i] << 25) + i);
        if (drops.size() > jump) {
            drops.erase((dp[i - jump] << 25) + i - jump);
        }
        if (i >= reach) {
            minimum = min(minimum, dp[i]);
        }
    }
    if (minimum < 1000000) {
        cout << minimum << endl;
    } else {
        cout << -1 << endl;
    }
    
    return 0;
}
