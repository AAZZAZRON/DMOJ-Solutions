//
// Created by Aaron Zhu on 2021-07-04.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <bitset>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 10002
int n, q;
bitset<MAX> board[MAX];
int x, y, w, h;
int total = 0;
int main()
{
    boost();
    cin >> n >> q;
    for (int i = 0; i < q; i += 1) {
        cin >> x >> y >> w >> h;
        board[x + 1].flip(y + 1);
        board[x + w + 1].flip(y + 1);
        board[x + 1].flip(y + h + 1);
        board[x + w + 1].flip(y + h + 1);
    }
    for (int i = 1; i <= n; i += 1) {
        for (int j = 1; j <= n; j += 1) {
            int val = 0;
            if (board[i].test(j)) val += 1;
            if (board[i - 1].test(j)) val += 1;
            if (board[i].test(j - 1)) val += 1;
            if (board[i - 1].test(j - 1)) val += 1;
            board[i].set(j, val % 2);
            if (board[i].test(j)) {
                total += 1;
            }
            //cout << board[i].test(j) << " ";
        }
        //cout << endl;
    }
    cout << total << endl;
    return 0;
}
