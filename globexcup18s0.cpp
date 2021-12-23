#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 200001
int aX[MAX], aY[MAX];
ll n, low, high, timeX, timeY;

inline ll calculate(int pos, int arr[MAX]) {
    ll c = 0;
    for (int i = 0; i < n; i += 1) c += abs(arr[i] - pos);
    return c;
}

int main() {
    scan(n);
    for (int i = 0; i < n; i += 1) {
        scan(aX[i]);
        scan(aY[i]);
    }
    timeX = min(calculate(0, aX), calculate(1000000000, aX));
    low = 0; high = 1000000000;
    while (high - low > 1) {
        int mid = (low + high) / 2;
        ll v = calculate(mid, aX);
        ll v2 = calculate(mid + 1, aX);
        timeX = fmin(timeX, fmin(v, v2));
        if (v < v2) high = mid;
        else low = mid;
    }

    timeY = min(calculate(0, aY), calculate(1000000000, aY));
    low = 0; high = 1000000000;
    while (high - low > 1) {
        int mid = (low + high) / 2;
        ll v = calculate(mid, aY);
        ll v2 = calculate(mid + 1, aY);
        timeY = fmin(timeY, fmin(v, v2));
        if (v < v2) high = mid;
        else low = mid;
    }

    cout << timeX + timeY << "\n";


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
