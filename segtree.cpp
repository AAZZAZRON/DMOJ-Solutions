//
// Created by Aaron Zhu on 2021-07-01.
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
#define MAX 100001
struct SegNode {
    int left, right, minimum;
};
int n, q, ind, x;
char instruction;
SegNode seg[MAX * 4];
int arr[MAX];

int segInit(int node, int left, int right) {
    int mid;
    seg[node].left = left;
    seg[node].right = right;
    if (left == right) {
        return seg[node].minimum = arr[left];
    }
    mid = (left + right) / 2;
    return seg[node].minimum = min(segInit(node * 2, left, mid), segInit(node * 2 + 1, mid + 1, right));
}

int query(int node, int left, int right) {
    if (right < seg[node].left || left > seg[node].right) return 200000000;
    if (left <= seg[node].left && seg[node].right <= right) return seg[node].minimum;
    return min(query(node * 2, left, right), query(node * 2 + 1, left, right));
}

int update(int node, int index) {
    if (seg[node].left == seg[node].right) return seg[node].minimum = arr[index];
    if (index <= seg[node * 2].right) update(node * 2, index);
    else update(node * 2 + 1, index);
    return seg[node].minimum = min(seg[node * 2].minimum, seg[node * 2 + 1].minimum);
}

int main()
{
    boost();
    cin >> n >> q;
    for (int i = 0; i < n; i += 1) cin >> arr[i];
    segInit(1, 0, n - 1);
    for (int i = 0; i < q; i += 1) {
        cin >> instruction >> ind >> x;
        if (instruction == 'Q') {
            cout << query(1, ind, x) << endl;
        } else {
            arr[ind] = x;
            update(1, ind);
        }
    }
    return 0;
}
