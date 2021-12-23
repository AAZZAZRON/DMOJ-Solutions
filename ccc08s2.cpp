//
// Created by Aaron Zhu on 2021-07-15.
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
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
int r;
int main()
{
    while (1) {
        scan(r);
        int rad = r * r;
        int n = 0;
        if (r == 0) return 0;
        for (int i = 1; i <= r; i += 1) {
            n += (int) sqrt(rad - (double) i * i) + 1;
        }
        cout << n * 4 + 1 << endl;
    }
}
