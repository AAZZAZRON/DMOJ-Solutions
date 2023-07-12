//
// Created by Aaron Zhu on 2023-04-10.
//
#include "bits/stdc++.h"
#define printArr(a, len) for(int asdf = 0; asdf < (len); asdf += 1) cout << (a)[asdf] << ' '; cout << '\n';
using namespace std;
//#define cin IN
//#define cout OUT
//ifstream IN;
//ofstream OUT;
#define int long long
#define MAX 101
string dp[MAX][MAX];
int grid[MAX][MAX];

string addBigNumbers(string number1, string number2) {
    if (number1.length() > number2.length())
        swap(number1, number2);
    string sum = "";
    int len1 = number1.length();
    int len2 = number2.length();
    int digitDiff = len2 - len1;
    int carry = 0;
    int intSum;
    for (int i=len1-1; i>=0; i--) {
        intSum = ((number1[i]-'0') + (number2[i+digitDiff]- '0') + carry);
        sum.push_back(intSum%10 + '0');
        carry = intSum/10;
    }
    for (int i=digitDiff-1; i>=0; i--) {
        intSum = ((number2[i]-'0')+carry);
        sum.push_back(intSum%10 + '0');
        carry = intSum/10;
    }
    if (carry)
        sum.push_back(carry+'0');
    reverse(sum.begin(), sum.end());
    return sum;
}

signed main() {
    cin.tie(); cin.sync_with_stdio(0);
    //IN.open("../txt/in.txt");
    //OUT.open("../txt/out.txt");

    int n; cin >> n;
    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < n; j += 1) {
            cin >> grid[i][j];
            dp[i][j] = "0";
        }
    }

    dp[0][0] = "1";
    for (int i = 0; i < n; i += 1) {
        for (int j = 0; j < n; j += 1) {
            int q = grid[i][j];
            if (q == 0) continue;
            if (i + q < n) dp[i + q][j] = addBigNumbers(dp[i + q][j], dp[i][j]);
            if (j + q < n) dp[i][j + q] = addBigNumbers(dp[i][j + q], dp[i][j]);
        }
    }

    cout << dp[n - 1][n - 1];

    //IN.close();
    //OUT.close();
    return 0;
}
