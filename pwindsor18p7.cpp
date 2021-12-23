//
// Created by Aaron Zhu on 2021-08-04.
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

bool compare(string a, string b) { return (a+b > b+a);}

string lexSmallest(string a[], int n) {
    sort(a, a+n, compare);
    string answer = "";
    for (int i = 0; i < n; i++) answer += a[i];
    return answer;
}
int num;
// Driver code
int main() {
    boost();
    cin >> num;
    string a[num];
    for (int i = 0; i < num; i += 1) cin >> a[i];
    cout << lexSmallest(a, num) << "\n";
    return 0;
}