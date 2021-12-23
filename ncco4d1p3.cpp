#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <queue>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
ll nodes, lines, one, two, cost;
vector<pair<ll, ll> > theQueue, added;
ll a, node, additional;
int main()
{
    cin >> nodes >> lines;
    vector<pair<ll, ll> > connections[nodes + 1];
    long long minimum[nodes + 1][2];
    for (int i = 0; i < nodes + 1; i += 1) {
        minimum[i][0] = 999999999;
        minimum[i][1] = 999999999;
    }
    for (int i = 0; i < lines; i += 1) {
        cin >> one >> two >> cost;
        connections[one].push_back(make_pair(two, cost));
        connections[two].push_back(make_pair(one, cost));
    }
    theQueue.push_back(make_pair(1, 0));
    while (true) {
        added.clear();
        for (int i = 0; i < theQueue.size(); i += 1) {
            a = theQueue[i].first;
            cost = theQueue[i].second;
            for (int j = 0; j < connections[a].size(); j += 1) {
                node = connections[a][j].first;
                additional = connections[a][j].second;
                if (cost + additional < minimum[node][1] && cost + additional != minimum[node][0]) {
                    minimum[node][1] = cost + additional;
                    sort(minimum[node], minimum[node] + 2);
                    added.push_back(make_pair(node, cost + additional));
                }
            }
        }
        if (added.size() == 0) {
            cout << minimum[nodes][1] << endl;
            return 0;
        } else {
            theQueue.clear();
            for (int i = 0; i < added.size(); i += 1) {
                theQueue.push_back(added[i]);
            }
        }
    }

    return 0;
}
