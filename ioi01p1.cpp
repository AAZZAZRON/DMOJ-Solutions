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
#define MAX 1025
using namespace std;
int BIT[MAX][MAX];
int i, j, maxSize;
int instruction;
int X, Y, A;
int XTwo, YTwo;

void updateBIT(int iIndex, int jIndex, int value) {
    iIndex += 1;
    jIndex += 1;
    for (i = iIndex; i <= maxSize; i += i & (-i))
        for (j = jIndex; j <= maxSize; j += j & (-j))
            BIT[i][j] += value;
}

ll getSum(int iIndex, int jIndex) {
    iIndex += 1;
    jIndex += 1;
    ll total = 0;
    for (i = iIndex; i > 0; i -= i & (-i))
        for (j = jIndex; j > 0; j -= j & (-j))
            total += BIT[i][j];
    return total;
}

int main()
{
    boost();
    cin >> instruction >> maxSize;
    for (i = 0; i <= maxSize; i += 1)
        for (j = 0; j <= maxSize; j += 1)
            BIT[i][j] = 0;
    
    while (true) {
        cin >> instruction;
        if (instruction == 1) { // update BIT
            cin >> X >> Y >> A;
            updateBIT(X, Y, A);
        } else if (instruction == 2) { // get sum query
            cin >> X >> Y >> XTwo >> YTwo;
            cout << getSum(XTwo, YTwo) - getSum(X - 1, YTwo) - getSum(XTwo, Y - 1) + getSum(X - 1, Y - 1) << endl;
        } else {
            return 0;
        }
    }
}
