//
// Created by Aaron Zhu on 2022-08-21.
//

#include "bits/stdc++.h"

using namespace std;
#define MAX 10000001
#define PL 700001
#define int long long
vector<int> primes;
int sieve[MAX];
int one[PL], two[PL];
inline bool check() {
    for (int i = 0; i < PL; i += 1) {
        if (one[i] > two[i]) return 0;
    }
    return 1;
}

inline void processPrimes(int arr[], int end, int m) {
    int ct = 0;
    for (int p : primes) {
        if (p > end) return;
        int t = p;
        do {
            arr[ct] += (end / t) * m;
            t *= p;
        } while (t <= end);
        ct++;
    }
}

inline void factorize(int arr[], int a, int b) {
    processPrimes(arr, b, 1);
    processPrimes(arr, a - 1, -1);
}

inline void sievePrime() {
    for (int i = 2; i < MAX; i += 1) {
        if (!sieve[i]) {
            primes.push_back(i);
            for (int j = i; j < MAX; j += i) sieve[j] = 1;
        }
    }
}

signed main() {
    cin.tie(0); cin.sync_with_stdio(0);
    sievePrime();
    int t; cin >> t;
    for (int _ = 0; _ < t; _ += 1) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        memset(one, 0, sizeof one);
        memset(two, 0, sizeof two);
        factorize(one, a, b);
        factorize(two, c, d);
//        for (int i = 0; i < 20; i += 1) cout << one[i] << " ";
//        cout << '\n';
//        for (int i = 0; i < 20; i += 1) cout << two[i] << " ";
//        cout << '\n';
        cout << (check() ? "DA\n" : "NE\n");
    }
    return 0;
}