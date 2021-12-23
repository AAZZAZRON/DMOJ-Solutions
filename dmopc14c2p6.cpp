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
using namespace std;
#define MAXMASS 200001
#define MAXTREES 1000001

vector<int> trees[MAXMASS];
vector<pair<int, pii> > queries[MAXMASS];
int BIT[MAXTREES];
ll answers[MAXMASS];
int n, mass;
int start, ending, m;

void insert(int ind, int inc) {
    ind += 1;
    for (; ind <= MAXTREES; ind += ind & (-ind)) {
        BIT[ind] += inc;
    }
}

ll query(int ind) {
    ind += 1;
    if (ind == 0) return 0;
    ll tmp = 0;
    for (; ind > 0; ind -= ind & (-ind)) {
        tmp += BIT[ind];
    }
    return tmp;
}

// add trees by descending mass, then answering the queries
// let BIT[i] be the answer to the query from [i, end]

int main()
{
    boost();
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> mass; 
        trees[mass].push_back(i);
    }
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> start >> ending >> m;
        queries[m].push_back(make_pair(i, make_pair(start, ending)));
    }
    for (int i = MAXMASS - 1; i > 0; i -= 1) {
        for (int val : trees[i]) insert(val, i);
        for (pair<int, pii> el : queries[i]) {
            answers[el.first] = query(el.second.second) - query(el.second.first - 1);
        }
    }
    for (int i = 0; i < n; i += 1) cout << answers[i] << endl;


    return 0;
}
