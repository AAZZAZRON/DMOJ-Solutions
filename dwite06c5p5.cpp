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
int seive[1000000];
vector<int> palindromes;
int start, ending;
int a, b;
string str;
bool isPalindrome;
int main()
{
    boost();
    for (int i = 0; i < 1000000; i += 1) {
        seive[i] = true;
    }
    seive[0] = seive[1] = false;
    for (int i = 0; i < 1000000; i += 1) {
        if (seive[i]) {
            str = to_string(i);
            isPalindrome = true;
            for (int j = 0; j < str.size(); j += 1) {
                if (str[j] != str[str.size() - j - 1]) {
                    isPalindrome = false;
                    break;
                }
            }
            if (isPalindrome) {
                palindromes.push_back(i);
            }
            for (int j = i + i; j < 1000000; j += i) {
                seive[j] = false;
            }
        }
    }
    for (int i = 0; i < 5; i += 1) {
        cin >> start >> ending;
        a = lower_bound(palindromes.begin(), palindromes.end(), start) - palindromes.begin() + 1;
        b = upper_bound(palindromes.begin(), palindromes.end(), ending) - palindromes.begin() + 1;
        cout << b - a << endl;
    }
    
    
    return 0;
}
