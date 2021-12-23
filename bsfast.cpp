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
#define MAX 1000001
int n, q;
int instruction, ind, v, l, r, k;
int lastAns = 0;
int arr[MAX];
int seg[MAX * 4];

int fill(int node, int left, int right) {
    if (left == right) return seg[node] = arr[left];
    int mid = (left + right) / 2;
    return seg[node] = min(fill(node * 2, left, mid), fill(node * 2 + 1, mid + 1, right));
}

int update(int node, int left, int right, int index) {
    if (left == right) return seg[node] = arr[index];
    int mid = (left + right) / 2;
    if (index <= mid) update(node * 2, left, mid, index);
    else update(node * 2 + 1, mid + 1, right, index);
    return seg[node] = min(seg[node * 2], seg[node * 2 + 1]);
}

int query(int node, int one, int two, int left, int right, int val) {
    if (right < one || left > two) return -1;
    if (left <= one && two <= right) {
        if (seg[node] >= val) return -1;
        while (one != two) {
            int mid = one + (two - one) / 2;
            if (seg[node * 2] < val) {
                node = node * 2;
                two = mid;
            } else {
                node = node * 2 + 1;
                one = mid + 1;
            }
        }
        return one;
    }
    int mid = one + (two - one) / 2;
    int tmp = query(node * 2, one, mid, left, right, val);
    if (tmp != -1) return tmp;
    return query(node * 2 + 1, mid + 1, two, left, right, val);
}

int main()
{
    boost();
    cin >> n >> q;
    for (int i = 1; i <= n; i += 1) cin >> arr[i];
    fill(1, 0, n);
    for (int i = 0; i < q; i += 1) {
        cin >> instruction;
        if (instruction == 1) {
            cin >> ind >> v;
            arr[ind ^ lastAns] = v ^ lastAns;
            update(1, 0, n, ind ^ lastAns);
        } else {
            cin >> l >> r >> k;
            lastAns = query(1, 0, n, l ^ lastAns, r ^ lastAns, k ^ lastAns);
            cout << lastAns << "\n";
        }
    }
    return 0;
}
