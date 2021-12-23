//
// Created by Aaron Zhu on 2021-12-03.
//

#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 100001

struct val {
    int n, v, ind;
};

vector<val> conn[MAX];
ll fastest[MAX];
bool visited[MAX];
int n, m;
int a, b, c;
int start, ending;
int low, high;
ll C;
priority_queue<pair<int, ll> > pq;

inline bool canTravel(int below) {
    for (int i = 1; i <= n; i += 1) {
        fastest[i] = 1000000000000;
        visited[i] = 0;
    }
    fastest[start] = 0;
    pq.push(make_pair(0, start));
    while (!pq.empty()) {
        int node = pq.top().second;
        ll cost = -pq.top().first;
        pq.pop();
        if (fastest[node] != cost) continue;
        for (val next : conn[node]) {
            if (next.ind <= below && visited[next.n] == 0 && cost + next.v < fastest[next.n]) {
                fastest[next.n] = cost + next.v;
                pq.push(make_pair(-cost - next.v, next.n));
            }
        }
        visited[node] = 1;
    }
    return fastest[ending] < C;
}

int main() {
    scan(n); scan(m);
    for (int i = 1; i <= m; i += 1) {
        scan(a); scan(b); scan(c);
        conn[a].push_back((val) {b, c, i});
        conn[b].push_back((val) {a, c, i});
    }
    scan(start); scan(ending); scan(C);
    if (!canTravel(m)) {
        cout << "-1\n";
        return 0;
    }
    low = 0; high = m + 1;
    while (high - low > 1) {
        int mid = (low + high) / 2;
        if (canTravel(mid)) high = mid;
        else low = mid;
    }
    cout << high << "\n";
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
