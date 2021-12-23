#include <iostream>
using namespace std;

long long total, discount;
int main()
{
    cin >> total >> discount;
    discount += 1;
    long long answer = (total / discount) * (discount - 1) + total - (total / discount) * discount;
    cout << answer << endl;
    return 0;
}
