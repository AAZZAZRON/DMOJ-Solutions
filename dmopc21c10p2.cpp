//
// Created by Aaron Zhu on 2022-09-01.
//

#include "bits/stdc++.h"
using namespace std;
#define MAX 1000001
int arr[MAX];
int ans[MAX];
int og[MAX];
int tmp[MAX];
int ind[MAX];
int n;

inline void rt(int a[MAX], int b[MAX], int st) {
    for (int i = 0; i < n; i += 1) {
        b[(i + st) % n] = a[i];
    }
}

inline bool smaller(int a[MAX], int b[MAX]) {
    for (int i = 0; i < n; i += 1) {
        if (a[i] < b[i]) return true;
        if (a[i] > b[i]) return false;
    }
    return true;
}

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);

    cin >> n;
    if (n == 1) {
        cout << "1\n";
        return 0;
    }

    for (int i = 0; i < n; i += 1) {
        cin >> og[i];
        ind[og[i]] = i;
    }

    int mv = n - ind[1];
    rt(og, ans, mv); // move two

    for (int i = 2; i <= n; i += 1) {
        if ((ind[i - 1] + mv + 1) % n != (ind[i] + mv) % n) {
            swap(ans[(ind[i - 1] + mv + 1) % n], ans[(ind[i] + mv) % n]);
            break;
        }
    }

    mv = (n - ind[2] + 1) % n;
    rt(og, arr, mv); // move one
    swap(arr[0], arr[(ind[1] + mv) % n]);
    if (smaller(arr, ans)) swap(arr, ans);

    if ((ind[2] + 1) % n == ind[1]) { // swap 1 and 2
        rt(og, arr, n - ind[2]);
        swap(arr[0], arr[1]);
        if (smaller(arr, ans)) swap(arr, ans);
    }
    assert(ans[0] == 1 && ans[1] == 2);
    for (int i = 0; i < n; i += 1) cout << ans[i] << ' ';
    cout << '\n';

    return 0;
}
