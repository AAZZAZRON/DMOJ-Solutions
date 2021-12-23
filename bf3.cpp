#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

using namespace std;
long long num;
bool isPrime(long long n) {
    for (long long i = 2; i < sqrt(n) + 1; i += 1) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
int main()
{
    boost();
    cin >> num;
    if (num == 2 || num == 1) {
        cout << 2 << endl;
        return 0;
    }
    if (num % 2 == 0) {
        num += 1;
    } 
    while (!isPrime(num)) {
        num += 2;
    }
    cout << num << endl;

    return 0;
}
