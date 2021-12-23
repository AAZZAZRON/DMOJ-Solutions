//
// Created by Aaron Zhu on 2021-08-13.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <cassert>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
int n;
int cost = 0;

inline bool isPrime(int num) {
    if (num == 2) return 1;
    if (num % 2 == 0) return 0;
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) return 0;
    }
    return 1;
}


int main() {
    scan(n);
    while (n != 1) {
        if (isPrime(n)) {
            n -= 1;
            cost += n;
        } else {
            for (int i = 2; i < n; i += 1) {
                if (n % i == 0) {
                    n -= n / i;
                    cost += i - 1;
                    break;
                }
            }
        }
    }
    cout << cost << "\n";

    return 0;
}
