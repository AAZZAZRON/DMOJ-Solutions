//
// Created by Aaron Zhu on 2021-07-05.
//

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
#define MAX 100001
ll q, n;
ll l, r, a, b, c;
ll one[MAX];
ll two[MAX];
ll three[MAX];

int main()
{
    boost();
    cin >> q >> n;
    for (int i = 0; i < q; i += 1) {
        cin >> l >> r >> a >> b >> c;
        one[l] += c;
        one[r + 1] -= a * (r - l) * (r - l) + b * (r - l) + c;
        two[l + 1] += a + b;
        two[r + 1] -= 2 * a * (r - l) - a + b;
        three[l + 2] += 2 * a;
        three[r + 1] -= 2 * a;
    }
    /*
    for (int i = 0; i <= n; i += 1) cout << one[i] << " ";
    cout << endl;
    for (int i = 0; i <= n; i += 1) cout << two[i] << " ";
    cout << endl;
    for (int i = 0; i <= n; i += 1) cout << three[i] << " ";
    cout << endl << endl;
    */

    for (int i = 1; i <= n; i += 1) {
        three[i] += three[i - 1];
        two[i] += two[i - 1] + three[i];
        one[i] += one[i - 1] + two[i];
    }
    /*
    for (int i = 0; i <= n; i += 1) cout << one[i] << " ";
    cout << endl;
    for (int i = 0; i <= n; i += 1) cout << two[i] << " ";
    cout << endl;
    for (int i = 0; i <= n; i += 1) cout << three[i] << " ";
    cout << endl;
    */

    for (int i = 1; i <= n; i += 1) cout << one[i] << " ";
    cout << endl;
    return 0;
}
