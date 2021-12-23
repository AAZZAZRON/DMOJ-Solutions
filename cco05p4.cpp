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
int cases, num;
bool solved;
long long window;
int numArray[10000];

bool isPrime(long long n) {
    for (int i = 2; i <= (int) sqrt(n) + 1; i += 1) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    cin >> cases;
    for (int i = 0; i < cases; i += 1) {
        cin >> num;
        for (int j = 0; j < num; j += 1) {
            cin >> numArray[j];
        }
        solved = false;
        // solve
        for (int length = 2; length <= num; length += 1) {
            window = 0;
            for (int j = 0; j < length; j += 1) {
                window += numArray[j];
            }
            if (isPrime(window)) {
                solved = true;
                cout << "Shortest primed subsequence is length " << length << ":";
                for (int ind = 0; ind < length; ind += 1) {
                    cout << " " << numArray[ind];
                }
                cout << endl;
                break;
            }
            for (int low = 0, high = length; high < num; low += 1, high += 1) {
                window += numArray[high];
                window -= numArray[low];
                if (isPrime(window)) {
                    solved = true;
                    cout << "Shortest primed subsequence is length " << length << ":";
                    for (int ind = low + 1; ind <= high; ind += 1) {
                        cout << " " << numArray[ind];
                    }
                    cout << endl;
                    break;
                }
            }
            if (solved) {
                break;
            }
        }
        if (!solved) {
            cout << "This sequence is anti-primed." << endl;
        }
    }
    return 0;
}
