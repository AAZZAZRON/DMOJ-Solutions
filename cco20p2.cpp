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
#define MAX 200001
using namespace std;

vector<int> values[MAX];
priority_queue<int> pq;
int BIT[MAX];
int original[MAX];
int d, val;

void update(int ind) {
    for (; ind < MAX; ind += ind & (-ind)) {
        BIT[ind] += 1;
    }
}

int getMax(int ind) {
    int total = 0;
    for (; ind > 0; ind -= ind & (-ind)) {
        total += BIT[ind];
    }
    return total;
}


int main()
{
    boost();
    cin >> d;
    for (int i = 1; i <= d; i += 1) {
        cin >> val;
        original[i] = val;
        values[val].push_back(i);
    }
    ll ans = 0;
    for (int i = d; i > 0; i -= 1) {
        for (int j = 0; j < values[i].size(); j += 1) {
            pq.push(values[i][j]);
        }
        if (pq.empty()) {
            cout << -1 << endl;
            return 0;
        }
        val = pq.top();
        pq.pop();
        int before = getMax(val);
        int totalRemoved = d - i;
        int after = totalRemoved - before;
        int between = d - val - after;
        ans += between;
        update(val);
    }
    cout << ans << endl;
    return 0;
}
