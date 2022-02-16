//
// Created by Aaron Zhu on 2021-07-29.
//

#include "bits/stdc++.h"
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 100001

int n, v, counter;
queue<int> q;
vector<int> forwards[MAX], backward[MAX];
bool visited[MAX];
int main() {
    for (int e = 0; e < 2; e += 1) {
        for (int i = 0; i < MAX; i += 1) {
            forwards[i].clear();
            backward[i].clear();
            visited[i] = 0;
        }
        counter = 0;
        scan(n);
        for (int i = 1; i <= n; i += 1) {
            scan(v);
            forwards[i].push_back(v);
            backward[v].push_back(i);
        }
        for (int i = 1; i <= n; i += 1) {
            if (!visited[i]) {
                visited[i] = 1;
                counter += 1;
                q.push(i);
                while (!q.empty()) {
                    int node = q.front(); q.pop();
                    for (int next : forwards[node]) {
                        if (!visited[next]) {
                            q.push(next);
                            visited[next] = 1;
                        }
                    }
                    for (int next : backward[node]) {
                        if (!visited[next]) {
                            q.push(next);
                            visited[next] = 1;
                        }
                    }
                }
            }
        }
        if (e == 0) cout << counter << " ";
        else cout << counter << "\n";
    }
    return 0;
}
