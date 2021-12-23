#include <iostream>
#include <vector>
#define boost() cin.tie(0); cin.sync_with_stdio(0)

using namespace std;

int num, big, value, amount, counter, take;
int values[20001], quantity[20001], dp[20001], previous[20001];
int main()
{
    boost();
    cin >> num;
    for (int i = 0; i < 20001; i += 1) {
        previous[i] = 200000;
    }
    for (int i = 0; i < num; i += 1) {
        cin >> values[i];
    }
    for (int i = 0; i < num; i += 1) {
        cin >> quantity[i];
    }
    cin >> big;
    previous[0] = 0;

    for (int i = 0; i < num; i += 1) {
        value = values[i];
        amount = quantity[i];
        for (int j = 1; j < 20001; j += 1) {
            take = 2000000;
            counter = 0;
            for (int q = j; q >= 0; q -= value) {
                if (counter > amount) {
                    break;
                }
                take = min(take, previous[q] + counter);
                counter += 1;
            }
            dp[j] = take;
        }
        swap(dp, previous);
    }
    cout << previous[big] << endl;
    return 0;
}
