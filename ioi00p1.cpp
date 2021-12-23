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
int length;
int dp[5001], previous[5001];
string word, backwards;
int main()
{
    cin >> length;
    cin >> word;
    backwards = word;
    reverse(backwards.begin(), backwards.end());
    for (int i = 0; i <= length; i += 1) {
        previous[i] = 0;
    }
    for (int i = 1; i <= length; i += 1) {
        for (int j = 1; j <= length; j += 1) {
            if (word[i - 1] == backwards[j - 1]) {
                dp[j] = previous[j - 1] + 1;
            } else {
                dp[j] = max(previous[j], dp[j - 1]);
            }
        }
        swap(dp, previous);
    }
    cout << length - previous[length] << endl;
    
    return 0;
}
