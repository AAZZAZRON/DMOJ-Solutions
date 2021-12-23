//
// Created by Aaron Zhu on 2021-08-03.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#define ll long long
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 2001
int num, tasks, phillip, total, inp;
int points[MAX], value[MAX];
vector<int> solved[MAX];
int main() {
    scan(num); scan(tasks); scan(phillip);
    for (int j = 0; j < num; j += 1) {
        value[j] = 0;
        points[j] = 0;
    }
    for (int i = 0; i < num; i += 1) {
        for (int j = 0; j < tasks; j += 1) {
            scan(inp);
            if (inp == 0) value[j] += 1;
            else {
                points[i] -= 2001;
                solved[i].push_back(j);
            }
        }
    }
    for (int i = 0; i < num; i += 1) {
        points[i] += i + 1;
        for (int j : solved[i]) {
            points[i] -= value[j] * 4000;
            if (i == phillip - 1) total += value[j];
        }
    }
    ll f = points[phillip - 1];
    sort(points, points + num);
    cout << total << " " << (lower_bound(points, points + num, f) - points) + 1 << "\n";
    return 0;
}