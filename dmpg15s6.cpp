//
// Created by Aaron Zhu on 2021-06-25.
//

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
double connections[501][501];
map<string, int> translate;
int n, m;
string one, two;
int node;
double price;
double amount[501];
queue<int> q;
int main()
{
    boost();
    cin >> n >> m;
    for (int i = 0; i < n; i += 1) {
        cin >> one;
        translate.insert({one, i});
    }
    for (int i = 0; i < m; i += 1) {
        cin >> one >> two >> price;
        int x = translate[one];
        int y = translate[two];
        connections[x][y] = max(connections[x][y], price);
    }
    amount[translate["APPLES"]] = 1;
    q.push(translate["APPLES"]);
    while (!q.empty()) {
        node = q.front(); q.pop();
        price = amount[node];
        for (int next = 0; next < n; next += 1) {
            if (connections[node][next] != 0) {
                double value = round(price * connections[node][next] * 10000000000) / 10000000000;
                if (value > amount[next]) {
                    amount[next] = value;
                    q.push(next);
                    if (next == translate["APPLES"]) {
                        cout << "YA" << "\n";
                        return 0;
                    }
                }
            }
        }
    }
    // for (int i = 0; i <= n; i += 1) cout << amount[i] << " ";
    // cout << endl;
    cout << "NAW" << "\n";
    return 0;
}
