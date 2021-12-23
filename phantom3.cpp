#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#include <bitset>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
#define MAX 20000001
ll start, ending;
bitset<MAX> primes;
ll n, length;
float tmp;
ll i, j;
ll counter = 0;

int isPrime(int num) {
    if (num == 2) return 1;
    for (j = 3; j * j <= num; j += 2) {
        if (num % j == 0) {
            return 0;
        }
    }
    return 1;
}


int main()
{
    boost(); 
    primes.reset();
    cin >> start >> ending;
    if (start == 1) start += 1;
    else if (start != 2 && start % 2 == 0) start += 1;
    length = ending - start;
    for (i = 2; i * i <= 10000000000; i += 1) {
        tmp = (float) start / (float) i;
        if (ceil(tmp) == tmp) n = ceil(start / i) * i;
        else n = (ceil(start / i) + 1) * i;
        if (i == n && isPrime(i)) n += i;
        for (j = n; j <= ending; j += i) {
            if (j - start >= 0 && !primes[j - start]) primes.flip(j - start);
        }
    }
    for (i = 0; i < length; i += 1) {
        if (!primes[i]) counter += 1;
    }
    cout << counter << endl;
    return 0;
}
