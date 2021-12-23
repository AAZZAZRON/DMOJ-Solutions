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
#define MAX 100001
int buns[MAX], hotdogs[MAX];
int n, val;
int answer = 269;
int main()
{
    boost();
    for (int i = 0; i < MAX; i += 1) {
        buns[i] = 101;
        hotdogs[i] = 101;
    }
    buns[0] = 0;
    hotdogs[0] = 0;
    // hotdogs
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> val;
        for (int j = MAX - 1; j >= val; j -= 1) {
            if (hotdogs[j - val] != 101) hotdogs[j] = min(hotdogs[j], hotdogs[j - val] + 1);
        }
    }

    // buns
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> val;
        for (int j = MAX - 1; j >= val; j -= 1) {
            if (buns[j - val] != 101) buns[j] = min(buns[j], buns[j - val] + 1);
        }
    }
    for (int i = 1; i < MAX; i += 1) {
        if (buns[i] != 101 && hotdogs[i] != 101) {
            answer = min(answer, buns[i] + hotdogs[i]);
        }
    }
    if (answer == 269) cout << "impossible" << endl;
    else cout << answer << endl;
    return 0;
}
