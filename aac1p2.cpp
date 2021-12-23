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

long long num, length, uses, change;
long long mySpeed, speed;
int main()
{
    boost();
    cin >> num >> length >> uses >> change;
    long long alpacas[num];
    for (int i = 0; i < num; i += 1) {
        cin >> alpacas[i];
    }
    cin >> mySpeed;
    for (int i = 0; i < num; i += 1) {
        speed = alpacas[i];
        while (mySpeed <= speed) {
            if (uses == 0) {
                cout << "NO" << endl;
                return 0;
            }
            speed = speed * (100 - change) / 100;
            uses -= 1;
            if (speed == 0) {
                break;
            }
        }
    }
    cout << "YES" << endl;
    
    return 0;
}
