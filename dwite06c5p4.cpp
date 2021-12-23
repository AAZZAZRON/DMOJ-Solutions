//
// Created by Aaron Zhu on 2021-08-08.
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

inline bool win(int arr[7][7], int a, int b) {
    for (int m = 0; m < 7; m += 1) {
        for (int n = 0; n < 7; n += 1) {
            if (arr[m][n] == arr[a][b]) {
                for (int i = -1; i <= 1; i += 1) {
                    for (int j = -1; j <= 1; j += 1) {
                        int x = m;
                        int y = n;
                        for (int k = 0; k < 3; k += 1) {
                            if (x + i == x && y + j == y) break;
                            x += i; y += j;
                            if (0 > x || x >= 7 || 0 > y || y >= 7 || arr[x][y] != arr[a][b]) break;
                            if (k == 2) return 1;
                        }
                    }
                }
            }
        }
    }
    return 0;
}

int main() {
    for (int q = 0; q < 5; q += 1) {
        int board[7][7];
        for (int i = 0; i < 7; i += 1)
            for (int j = 0; j < 7; j += 1)
                board[i][j] = 0;
        int c = getchar() - 49;
        bool done = 0;
        int current = 2;
        int counter = 0;
        while (c != -39) {
            if (current == 2) current = 1;
            else current = 2;
            if (!done) {
                counter += 1;
                int i = 6;
                while (board[i][c]) i -= 1;
                board[i][c] = current;
                if (win(board, i, c)) done = 1;
            }
            c = getchar() - 49;
        }
        if (counter % 2 == 0) cout << "BLUE-";
        else cout << "RED-";
        cout << counter << "\n";
    }
}
