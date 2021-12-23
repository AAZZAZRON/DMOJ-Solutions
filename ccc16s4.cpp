//
// Created by Aaron Zhu on 2021-06-28.
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
#define MAX 401
int n, tmp;
int combine[MAX][MAX];
int balls[MAX];
int maximum = 0;

int canCombine(int i, int j) {
    if (i >= j) return 1;
    else if (combine[i][j] != -1) return combine[i][j];
    tmp = 0;
    for (int a = i; a < j; a += 1) {
        int b = j;
        while (b > a) {
            tmp = canCombine(i, a) * canCombine(a + 1, b - 1) * canCombine(b, j);
            if (tmp && balls[j + 1] - balls[b] == balls[a + 1] - balls[i]) {
                // cout << i << ", " << j << ": " << balls[j + 1] << ", " << balls[i] << endl;
                maximum = max(maximum, balls[j + 1] - balls[i]);
                return combine[i][j] = 1;
            }
            b -= 1;
        }
    }
    return combine[i][j] = 0;
}

int main()
{
    boost();
    cin >> n;
    for (int i = 0; i < MAX; i += 1) {
        for (int j = 0; j < MAX; j += 1) combine[i][j] = -1;
    }
    for (int i = 1; i <= n; i += 1) {
        cin >> balls[i];
        maximum = max(maximum, balls[i]);
        balls[i] += balls[i - 1];
    }
    canCombine(0, n - 1);
    cout << maximum << endl;

    return 0;
}
