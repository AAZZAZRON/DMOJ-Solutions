//
// Created by Aaron Zhu on 2022-09-03.
//

#include "bits/stdc++.h"
using namespace std;
#define MAX 200001

int n;
int lis[MAX];
int freq[MAX];

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);

    cin >> n;
    for (int i = 0; i < n; i += 1) cin >> lis[i];

    for (int i = 0; i < n; i += 1) {
        freq[lis[i]] += 1;
        if (lis[i] > i + 1 || (i != 0 && (lis[i - 1] > lis[i] || lis[i] - lis[i - 1] > 1))) {
            cout << "-1\n";
            return 0;
        }
    }

    int ct = 0;
    for (int i = 1; i < MAX; i += 1) {
        ct += freq[i];
        for (int j = 0; j < freq[i]; j += 1) {
            cout << ct - j << ' ';
        }
    }
    cout << '\n';



    return 0;
}
