//
// Created by Aaron Zhu on 2021-07-12.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
struct info {
    ll val;
    int count;
};
ll n, num;
stack<info> s;
ll tS = 0;
ll c = 0;
int main()
{
    boost();
    cin >> num;
    for (int i = 0; i < num; i += 1) {
        cin >> n;
        int popped = 0;
        while (!s.empty() && s.top().val < n) {
            popped += s.top().count;
            s.pop();
        }
        c += popped;
        if (!s.empty()) c += 1;
        if (!s.empty() && s.top().val == n) {
            c += s.top().count - 1;
            s.top().count++;
            info tmp = s.top(); s.pop();
            if (!s.empty()) c += 1;
            s.push(tmp);
        } else s.push({n, 1});
        // cout << c << ": " << s.top().val << " " << s.top().count << "\n";
    }
    cout << c << "\n";
    return 0;
}
