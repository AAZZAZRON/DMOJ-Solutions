//
// Created by Aaron Zhu on 2022-09-01.
//

#include "bits/stdc++.h"
using namespace std;

queue<int> curr, nex;
int n, a, b;
signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    cin >> n;

    for (int i = 1; i <= n; i += 1) curr.push(i);

    while (curr.size() != 1) {
        while (!curr.empty()) {
            a = curr.front();
            curr.pop();
            if (!curr.empty()) {
                b = curr.front();
                curr.pop();
            } else {
                nex.push(a);
                continue;
            }

            cout << "? " << a << " " << b << '\n';
            cout.flush();
            int res;
            cin >> res;
            if (res) nex.push(b);
            else nex.push(a);
        }
        swap(curr, nex);
    }

    cout << "! " << curr.front() << '\n';
    return 0;
}
