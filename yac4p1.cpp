//
// Created by Aaron Zhu on 2022-09-16.
//

#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <fstream>
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
#define MAX 2000001

int arr[MAX];

ifstream IN;
ofstream OUT;

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    IN.open("../in.txt");
    OUT.open("../out.txt");

    int n; cin >> n;
    for (int i = 0; i < 2 * n; i += 1) cin >> arr[i];
    int ct = 0;
    for (int i = 0; i < n; i += 1) {
        if (arr[i] == arr[i + n]) ct += 1;
    }
    cout << ct << '\n';


    IN.close();
    OUT.close();
    return 0;
}