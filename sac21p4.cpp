#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
int num, q;
int one, two;
int main()
{
    boost();
    cin >> num >> q;
    int psa[num + 1];
    psa[0] = 0;
    for (int i = 1; i <= num; i += 1) {
        cin >> psa[i];
        psa[i] += psa[i - 1];
    }
    for (int i = 0; i < q; i += 1) {
        cin >> one >> two;
        cout << (psa[two] - psa[one - 1]) / (two - one + 1) << endl;
    }
    
    
    return 0;
}
