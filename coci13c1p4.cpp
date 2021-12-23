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
#define MAX 1000001
using namespace std;

vector<int> jewels[MAX];
priority_queue<int> best, bags;
int n, k, m, v;
int stopped = 0;
ll bag;
ll total = 0;
int main()
{
    boost();
    cin >> n >> k;
    for (int i = 0; i < n; i += 1) {
        cin >> m >> v;
        jewels[m].push_back(v);
    }
    for (int i = 0; i < k; i += 1) {
        cin >> bag;
        if (bag >= MAX) {
            bag = MAX - 1;
        }
        bags.push(-bag);
    }
    for (int i = 0; i < k; i += 1) {
        bag = -bags.top(); bags.pop();
        for (; stopped <= bag; stopped += 1) {
            for (int j : jewels[stopped]) best.push(j);
        }
        if (!best.empty()) {
            total += best.top();
            best.pop();
        }
    }
    cout << total << endl;
    
    return 0;
}
