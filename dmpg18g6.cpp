//
// Created by Aaron Zhu on 2022-01-15.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pb push_back
#define mp make_pair
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MOD 1000000007
#define MAX 100001

int n, c, k, ct, tmp;
ll v[MAX];
vector<int> user[MAX]; // which class each user is in
vector<int> inClass[MAX]; // which user is in each class
priority_queue<pll> pq;
bool vis[MAX];
ll minD[MAX];

int main() {
    boost();
    cin >> n >> c >> k;
    for (int i = 1; i <= n; i += 1) {
        cin >> v[i];
    }
    for (int i = 1; i <= n; i += 1) {
        cin >> ct;
        for (int j = 0; j < ct; j += 1) {
            cin >> tmp;
            inClass[tmp].pb(i);
            user[i].pb(tmp);
        }
    }
    for (int i = 0; i < MAX; i += 1) minD[i] = -1;
    minD[1] = 0;
    pq.push(mp(0, 1));
    while (!pq.empty()) {
        ll cost = -pq.top().first;
        int node = pq.top().second;
        pq.pop();
        if (cost != minD[node]) continue;
        for (int cl : user[node]) {
            for (int us : inClass[cl]) {
                if (!vis[us] && (minD[us] == -1 || minD[node] + abs(v[node] - v[us]) + k < minD[us])) {
                    minD[us] = minD[node] + abs(v[node] - v[us]) + k;
                    pq.push(mp(-minD[us], us));
                }
            }
        }
        vis[node] = 1;
    }

    for (int i = 1; i <= n; i += 1) {
        cout << minD[i] << "\n";
    }

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
