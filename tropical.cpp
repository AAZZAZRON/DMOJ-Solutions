//
// Created by Aaron Zhu on 2021-08-02.
//

#include <iostream>
#define boost() cin.tie(0); cin.sync_with_stdio(0)

#define ll long long
using namespace std;
#define MAX 200003
ll n, q, instruction, l, r, a, b;
ll psa[MAX];
ll change[MAX];

int main() {
    boost();
    cin >> n >> q;
    for (int i = 0; i < q; i += 1) {
        cin >> instruction >> l >> r >> a >> b;
        if (instruction == 0) {
            psa[l] += a + b;
            psa[r + 1] -= a + b * (r - l + 1);
            change[l + 1] += b;
            change[r + 1] -= b;
        } else {
            psa[l] += a + b * (r - l + 1);
            psa[r + 1] -= a + b;
            change[l + 1] -= b;
            change[r + 1] += b;
        }
    }
    for (int i = 1; i <= n; i += 1) {
        change[i] += change[i - 1];
        psa[i] += psa[i - 1] + change[i];
        cout << psa[i] << "\n";
    }
    return 0;
}
