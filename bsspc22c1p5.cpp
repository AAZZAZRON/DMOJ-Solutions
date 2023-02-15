#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <unordered_map>
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT

ifstream IN;
ofstream OUT;
#define MOD 1000000007
#define MAX 200001
#define int long long
int arr[MAX];
unordered_map<int, int> memo;

inline int dfs(int ar[], int sz) {
    int ct = 1;
    //printArr(ar, sz);
    for (int i = 0; i < sz; i += 1) {
        int el = ar[i];
        if (el % 2 == 0) {
            if (memo.find(el) == memo.end()) {
                memo[el] = dfs(new int[] {el / 2, el / 2}, 2);
            }
            ct = (ct * memo[el]) % MOD;
        }
    }
    return ct + 1;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    IN.open("../in.txt");
    OUT.open("../out.txt");

    int n;
    cin >> n;
    for (int i = 0; i < n; i += 1) cin >> arr[i];
    cout << dfs(arr, n) - 1 << '\n';

    IN.close();
    OUT.close();
    return 0;
}