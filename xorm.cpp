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
#include <bitset>
#include <string>
#include <unordered_map>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;
using namespace std;
#define INF 0x7fffffff
#define MAX 31

struct node {
    struct node* children[2];
};

inline struct node *init(void) {
    struct node *pNode = new node;
    pNode->children[0] = nullptr;
    pNode->children[1] = nullptr;
    return pNode;
}

inline void insert(node *root, string s) {
    node *curr = root;
    int bit;
    for (int i = 0; i < MAX; i += 1) {
        if (s[i] == '0') bit = 0;
        else bit = 1;
        if (!curr->children[bit]) {
            curr->children[bit] = init();
        }
        curr = curr->children[bit];
    }
}

inline int query(node *root, string s) {
    node *curr = root;
    string ans = "";
    int bit;
    for (int i = 0; i < MAX; i += 1) {
        if (s[i] == '0') bit = 0;
        else bit = 1;
        if (!curr->children[bit]) {
            ans += to_string((!bit));
            curr = curr->children[!bit];
        } else {
            ans += to_string(bit);
            curr = curr->children[bit];
        }
    }
    return stoi(ans, 0, 2);
}

int n, q, v;
unordered_map<int, int> d;
int main() {
    node *root = init();
    scan(n); scan(q);
    for (int i = 0; i < n; i += 1) {
        scan(v);
        if (d.find(v) == d.end()) d[v] = i;
        insert(root, bitset<MAX>(v).to_string());
    }
    int curx = 0;
    for (int i = 0; i < q; i += 1) {
        scan(v);
        curx ^= v;
        cout << d[query(root, bitset<MAX>(curx).to_string())] << "\n";
    }
    return 0;
}
