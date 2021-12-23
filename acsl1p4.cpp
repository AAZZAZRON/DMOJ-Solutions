//
// Created by Aaron Zhu on 2021-06-22.
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
#define MAX 22
vector<int> connections[MAX];
int low[MAX], onStack[MAX], ids[MAX];
stack<int> s;
int id = 1;
int n, k;
int one, two, s1, s2;
int total = 0;

void dfs(int at) {
    ids[at] = low[at] = id++;
    s.push(at);
    onStack[at] = 1;
    for (int next : connections[at]) {
        if (ids[next] == 0) dfs(next);
        if (onStack[next]) low[at] = min(low[at], low[next]);
    }
    if (ids[at] == low[at]) { // found cycle
        int counter = 1;
        int curr = s.top();
        while (curr != at) {
            counter += 1;
            s.pop();
            low[curr] = at;
            onStack[curr] = 0;
            curr = s.top();
        }
        s.pop();
        onStack[at] = 0;
        if (counter != 1) total += counter;
    }
}


int main()
{
    cin >> n >> k;
    for (int i = 0; i < k; i += 1) {
        cin >> one >> two >> s1 >> s2;
        if (s1 > s2) connections[one].push_back(two);
        else connections[two].push_back(one);
    }
    for (int i = 1; i <= n; i += 1) {
        if (ids[i] == 0) dfs(i);
    }
    cout << total << endl;



    return 0;
}
