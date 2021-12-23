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
#define MAX 1000001
using namespace std;
ll sumBIT[MAX], freqBIT[MAX], values[MAX];
ll n, m;
ll i, num;
char type;
ll one, two;

void updateBIT(ll array[], ll value, ll index, ll ending) {
    for (;index <= ending; index += index & (-index)) {
        array[index] += value;
    }
}

ll getSum(ll array[], ll index) {
    ll total = 0;
    for (; index > 0; index -= index & (-index)) {
        total += array[index];
    }
    return total;
}

int main()
{
    boost();
    cin >> n >> m;
    for (i = 0; i <= n; i += 1) {
        sumBIT[i] = 0;
        freqBIT[i] = 0;
    }
    for (i = 1; i <= n; i += 1) {
        cin >> num;
        updateBIT(sumBIT, num, i, n);
        updateBIT(freqBIT, 1, num, MAX - 1);
        values[i] = num;
    }

    for (i = 0; i < m; i += 1) {
        cin >> type;
        if (type == 'C') {
            cin >> one >> two;
            updateBIT(sumBIT, two - values[one], one, n);
            updateBIT(freqBIT, -1, values[one], MAX - 1);
            updateBIT(freqBIT, 1, two, MAX - 1);
            values[one] = two;
        } else if (type == 'S') {
            cin >> one >> two;
            cout << getSum(sumBIT, two) - getSum(sumBIT, one - 1) << endl;
        } else {
            cin >> one;
            cout << getSum(freqBIT, one) << endl;
        }
    }

    return 0;
}
