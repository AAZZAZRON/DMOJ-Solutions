//
// Created by Aaron Zhu on 2021-06-29.
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

struct SegNode {
    int left, right;
    int minimum, gcd, freq;
};

int GCD(int a, int b) {
    if (b == 0) return a;
    return GCD(b, a % b);
}

void segInit(SegNode seg[], int node, int left, int right) {
    int mid;
    seg[node].left = left;
    seg[node].right = right;
    if (left == right) return;
    mid = (left + right) / 2;
    segInit(seg, node * 2, left, mid);
    segInit(seg, node * 2 + 1, mid + 1, right);
}

void fill(SegNode seg[], int node, int arr[]) {
    if (seg[node].left == seg[node].right) {
        seg[node].minimum = arr[seg[node].left];
        seg[node].gcd = arr[seg[node].left];
        seg[node].freq = 1;
        return;
    }
    fill(seg, node * 2, arr);
    fill(seg, node * 2 + 1, arr);
    SegNode leftNode = seg[node * 2];
    SegNode rightNode = seg[node * 2 + 1];
    seg[node].minimum = min(leftNode.minimum, rightNode.minimum);
    seg[node].gcd = GCD(leftNode.gcd, rightNode.gcd);
    seg[node].freq = 0;
    if (seg[node].gcd == leftNode.gcd) seg[node].freq += leftNode.freq;
    if (seg[node].gcd == rightNode.gcd) seg[node].freq += rightNode.freq;
}

void update(SegNode seg[], int node, int arr[], int index) {
    if (seg[node].left == seg[node].right) { // if index is leaf
        seg[node].minimum = arr[index];
        seg[node].gcd = arr[index];
        seg[node].freq = 1;
        return;
    }
    if (index <= seg[node * 2].right) update(seg, node * 2, arr, index);
    else update(seg, node * 2 + 1, arr, index);

    SegNode leftNode = seg[node * 2];
    SegNode rightNode = seg[node * 2 + 1];
    seg[node].minimum = min(leftNode.minimum, rightNode.minimum);
    seg[node].gcd = GCD(leftNode.gcd, rightNode.gcd);
    seg[node].freq = 0;
    if (seg[node].gcd == leftNode.gcd) seg[node].freq += leftNode.freq;
    if (seg[node].gcd == rightNode.gcd) seg[node].freq += rightNode.freq;
}

int minimumQuery(SegNode seg[], int node, int left, int right) {
    // case 1: [left, right] lies outside our zone
    if (right < seg[node].left || left > seg[node].right) return 2000000000;
    // case 2: [left, right] lies completely in our zone
    if (left <= seg[node].left && seg[node].right <= right) return seg[node].minimum;
    // case 3: [left, right] lies partially in our zone
    return min(minimumQuery(seg, node * 2, left, right), minimumQuery(seg, node * 2 + 1, left, right));
}

int GCDQuery(SegNode seg[], int node, int left, int right) {
    if (right < seg[node].left || left > seg[node].right) return -1;
    if (left <= seg[node].left && seg[node].right <= right) return seg[node].gcd;
    int one = GCDQuery(seg, node * 2, left, right);
    int two = GCDQuery(seg, node * 2 + 1, left, right);
    if (one == -1 && two == -1) return -1;
    else if (one == -1) return two;
    else if (two == -1) return one;
    else return GCD(one, two);
}

int freqQuery(SegNode seg[], int node, int left, int right, int g) {
    if (right < seg[node].left || left > seg[node].right) return 0;
    if (left <= seg[node].left && seg[node].right <= right) {
        if (seg[node].gcd == g) return seg[node].freq;
        return 0;
    }
    return freqQuery(seg, node * 2, left, right, g) + freqQuery(seg, node * 2 + 1, left, right, g);
}

#define MAX 100001
int n, q, a, b;
int nums[MAX];
char instruction;
SegNode segmentTree[4 * MAX];
int main() {
    boost();
    cin >> n >> q;
    for (int i = 1; i <= n; i += 1) cin >> nums[i];

    segInit(segmentTree, 1, 0, n);
    fill(segmentTree, 1, nums);

    for (int i = 0; i < q; i += 1) {
        cin >> instruction >> a >> b;
        if (instruction == 'C') {
            nums[a] = b;
            update(segmentTree, 1, nums, a);
        } else if (instruction == 'M') cout << minimumQuery(segmentTree, 1, a, b) << endl;
        else if (instruction == 'G') cout << GCDQuery(segmentTree, 1, a, b) << endl;
        else if (instruction == 'Q') {
            int tmp = GCDQuery(segmentTree, 1, a, b);
            cout << freqQuery(segmentTree, 1, a, b, tmp) << endl;
        }
    }
    return 0;
}
