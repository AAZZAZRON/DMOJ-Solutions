//
// Created by Aaron Zhu on 2021-06-17.
// Tarjan's + DP
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vi vector<int>
#define vii vector<pii>
#define si set<int>
#define usi unordered_set<int>
#define mii map<int, int>
#define umii unordered_map<int, int>
#define pb push_back
#define mp make_pair
#define printArr(a, len) for(int orzdaniel = 0; orzdaniel < (len); orzdaniel += 1) cout << (a)[orzdaniel] << ' '; cout << '\n';
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 1000000005
#define LLINF 1000000000000000005LL
#define MOD 1000000007
#define MAX 500005

int n, m, a, b;
int id = 1;
int scc = 1;
vi group[MAX], conn[MAX], dpConn[MAX];
int loot[MAX], ids[MAX], low[MAX], cost[MAX], gId[MAX];
pii memo[MAX][2];
bool onStack[MAX];
bitset<MAX> dupes;
stack<int> s;

inline void dfs(int node) {
    s.push(node);
    ids[node] = low[node] = id++;
    onStack[node] = 1;

    for (int nex : conn[node]) {
        if (!ids[nex]) dfs(nex);
        if (onStack[nex]) low[node] = min(low[node], low[nex]);
    }
    if (ids[node] == low[node]) {
        while (s.top() != node) {
            cost[scc] = (cost[scc] + loot[s.top()]) % MOD;
            onStack[s.top()] = 0;
            low[s.top()] = ids[node];
            gId[s.top()] = scc;
            group[scc].pb(s.top());
            s.pop();
        }
        cost[scc] = (cost[scc] + loot[s.top()]) % MOD;
        onStack[node] = 0;
        gId[node] = scc;
        group[scc].pb(node);
        s.pop();
        scc += 1;
    }
}

inline pii memoize(int node, bool canTake) {
    if (memo[node][canTake].first) return memo[node][canTake];
    else if (node == gId[n]) {
        if (canTake) return memo[node][canTake] = {cost[node], 1};
        return memo[node][canTake] = {0, 1};
    }
    int maximum = 0, ct = 1;
    for (int nex : dpConn[node]) {
        if (canTake) {
            pii tmp = memoize(nex, 0);
            if (tmp.first + cost[node] > maximum) {
                maximum = tmp.first + cost[node];
                ct = tmp.second;
            } else if (tmp.first + cost[node] == maximum) {
                ct = (ct + tmp.second) % MOD;
            }
        }
        pii tmp = memoize(nex, 1);
        if (tmp.first > maximum) {
            maximum = tmp.first;
            ct = tmp.second;
        } else if (tmp.first == maximum) {
            ct = (ct + tmp.second) % MOD;
        }
    }
    return memo[node][canTake] = {maximum, ct};
}

int main() {
    boost();
    cin >> n >> m;
    for (int i = 1; i <= n; i += 1) cin >> loot[i];

    for (int i = 0; i < m; i += 1) {
        cin >> a >> b;
        conn[a].pb(b);
    }

    // ----- TARJAN'S -----
    for (int i = 1; i <= n; i += 1) {
        if (!ids[i]) dfs(i);
    }

    for (int i = 1; i <= scc; i += 1) {
        dupes.reset();
        dupes.flip(i);
        for (int el : group[i]) {
            for (int t : conn[el]) {
                t = gId[t];
                if (!dupes[t]) {
                    dupes.flip(t);
                    dpConn[i].pb(t);
                }
            }
        }
    }

//    printArr(ids, n + 1);
//    printArr(low, n + 1);
//    printArr(gId, n + 1);
//    printArr(cost, scc + 1);
//    for (int i = 1; i < scc; i += 1) {
//        printArr(group[i], group[i].size());
//        printArr(dpConn[i], dpConn[i].size());
//    }

    // ----- DYNAMIC PROGRAMMING -----
    memoize(gId[1], 1);
    cout << memo[gId[1]][1].first << " " << memo[gId[1]][1].second << '\n';

    return 0;
}

/*
 * Stuck?
 * Did you try:
 * Integer overflow?
 * Edge cases? (n = 1)
 * Printing output?
 * Organizing your code?
 * Another approach?
 *
 * Still Stuck? Ask Daniel!
 */