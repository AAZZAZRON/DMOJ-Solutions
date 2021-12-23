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
#define MAX 251
using namespace std;
ll BIT[MAX][MAX][MAX], values[MAX][MAX][MAX];
ll i, j, k, q;
ll maxSize, numQueries;
char instruction;
ll X, Y, Z, A;
ll XTwo, YTwo, ZTwo;
ll final = 0;

void updateBIT(ll iIndex, ll jIndex, ll kIndex, ll value) {
    for (i = iIndex; i <= maxSize; i += i & (-i))
        for (j = jIndex; j <= maxSize; j += j & (-j))
            for (k = kIndex; k <= maxSize; k += k & (-k))
                BIT[i][j][k] += value;
}

ll getSum(ll iIndex, ll jIndex, ll kIndex) {
    ll total = 0;
    for (i = iIndex; i > 0; i -= i & (-i))
        for (j = jIndex; j > 0; j -= j & (-j))
            for (k = kIndex; k > 0; k -= k & (-k))
                total += BIT[i][j][k];
    return total;
}

int main()
{
    boost();
    cin >> maxSize >> numQueries;
    for (i = 0; i <= maxSize; i += 1)
        for (j = 0; j <= maxSize; j += 1)
            for (k = 0; k <= maxSize; k += 1) {
                BIT[i][j][k] = 0;
                values[i][j][k] = 0;
            }
    for (q = 0; q < numQueries; q += 1) {
        cin >> instruction;
        if (instruction == 'C') { // update BIT
            cin >> X >> Y >> Z >> A;
            updateBIT(X, Y, Z, A - values[X][Y][Z]);
            values[X][Y][Z] = A;
        } else { // get sum query
            cin >> X >> Y >> Z >> XTwo >> YTwo >> ZTwo;

            final += (getSum(XTwo, YTwo, ZTwo) - getSum(X - 1, YTwo, ZTwo) - getSum(XTwo, Y - 1, ZTwo) + getSum(X - 1, Y - 1, ZTwo)) - (getSum(XTwo, YTwo, Z - 1) - getSum(X - 1, YTwo, Z - 1) - getSum(XTwo, Y - 1, Z - 1) + getSum(X - 1, Y - 1, Z - 1));
        }
    }
    cout << final << endl;
    return 0;
}
