#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
vector<pii> days[100001];
vector<pii> queries;
int answers[100001];
int places[1000001];
int people, q;
int counter = 0;
int num = 0;
char command;
int x, y;
int pp, ind;
int main()
{
    cin >> people;
    for (int i = 1; i <= people; i += 1) {
        cin >> places[i];
    }
    cin >> q;
    for (int i = 0; i < q; i += 1) {
        cin >> command >> x >> y;
        if (command == 'C') {
            queries.push_back(make_pair(x, y));
        } else {
            days[y].push_back(make_pair(x, counter));
            counter += 1;
        }
    }
    for (int j = 0; j < days[num].size(); j += 1) {
        pp = days[num][j].first;
        ind = days[num][j].second;
        answers[ind] = places[pp];
    }
    for (int i = 0; i < queries.size(); i += 1) {
        x = queries[i].first;
        y = queries[i].second;
        num += 1;
        places[x] = y;
        for (int j = 0; j < days[num].size(); j += 1) {
            pp = days[num][j].first;
            ind = days[num][j].second;
            answers[ind] = places[pp];
        }
    }
    for (int i = 0; i < counter; i += 1) {
        cout << answers[i] << endl;
    }
    
    return 0;
}
