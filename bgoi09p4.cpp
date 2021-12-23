//
// Created by Aaron Zhu on 2021-08-07.
//

#include <iostream>
#include <vector>
#include <set>
#include <functional>
#include <deque>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 1000001
int n, jumps;
int arr[MAX];
int j[MAX];
deque<ll> s;
int main() {
    scan(n);
    for (int i = 0; i < n; i += 1) scan(arr[i]);
    for (int i = 0; i < n; i += 1) scan(j[i]);
    for (int i = n - 1; i >= 0; i -= 1) {
        int num = arr[i];
        jumps = j[i];
        while (!s.empty() && s.front() <= num) s.pop_front();
        s.push_front(num);
        //for (ll el : s) cout << el << " ";
        if (jumps >= s.size()) j[i] = -1;
        else j[i] = s.at(jumps);
    }
    for (int i = 0; i < n; i += 1) cout << j[i] << " ";
}
