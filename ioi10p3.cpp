#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
#define MAXR 3001
#define MAXC 3001
typedef int board[MAXR][MAXC];

using namespace std;

int canMakeMedian(int want, int r, int c, int h, int w, board q) {
    static int psa[MAXR + 1][MAXC + 1];
    static int adjusted[MAXR][MAXC];
    int i, j;
    int topR, leftC, bottomR, rightC;
    int total;
    for (i = 0; i < r; i += 1) {
        for (j = 0; j < c; j += 1) {
            if (q[i][j] <= want) {
                adjusted[i][j] = -1;
            } else {
                adjusted[i][j] = 1;
            }
        }
    }

    for (i = 0; i <= r; i += 1) {
        for (j = 0; j <= c; j += 1) {
            psa[i][j] = 0;
        }
    }
    for (i = 1; i <= r; i += 1) {
        for (j = 1; j <= c; j += 1) {
            psa[i][j] = adjusted[i - 1][j - 1] + psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1];
        }
    }

    for (topR = 1; topR <= r - h + 1; topR += 1) {
        for (leftC = 1; leftC <= c - w + 1; leftC += 1) {
            bottomR = topR + h - 1;
            rightC = leftC + w - 1;
            total = psa[bottomR][rightC] - psa[topR - 1][rightC] - psa[bottomR][leftC - 1] + psa[topR - 1][leftC - 1];
            if (total <= 0) {
                return 1;
            }
        }
    }
    return 0;
}


int rectangle(int r, int c, int h, int w, board q) {
    int low = 0;
    int high = r * c + 1;
    int mid;
    while (high - low > 1) { // binary search the minimum value
        mid = (low + high) / 2;
        if (canMakeMedian(mid, r, c, h, w, q)) {
            high = mid; // go lower
        } else {
            low = mid; // go higher
        }
    }
    return high;
}