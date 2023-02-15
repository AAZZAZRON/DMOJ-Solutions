//
// Created by Aaron Zhu on 2022-09-16.
//

#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';

using namespace std;
ifstream IN;
ofstream OUT;

//#define cin IN
//#define cout OUT
#define MAX 1000002

int arr[26][MAX];

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    IN.open("../txt/in.txt");
    OUT.open("../txt/out.txt");

    string s;
    getline(cin, s);

    int n = s.length();

    for (int i = 0; i < 26; i += 1) {
        for (int j = 1; j <= n; j += 1) {
            arr[i][j] = arr[i][j - 1] + (s[j - 1] == i + 97 ? 1 : 0);
        }
    }

    int q; cin >> q;
    for (int i = 0; i < q; i += 1) {
        int a, b; cin >> a >> b;
        char c; cin >> c;
        cout << arr[c - 97][b] - arr[c - 97][a - 1] << '\n';
    }


    IN.close();
    OUT.close();
    return 0;
}