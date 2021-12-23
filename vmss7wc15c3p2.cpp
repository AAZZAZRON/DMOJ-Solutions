#include <iostream>
using namespace std;

int n, k;

int main()
{
    cin >> n >> k;
    int array[n];
    for (int i = 0; i < n; i += 1) {
        cin >> array[i];
    }
    sort(array, array + n);
    long long sum = 0;
    for (int i = n - 1; i >= n - k; i -= 1) {
        if (array[i] < 0) {
            break;
        }
        sum += array[i];
        // cout << array[i] << endl;
    }
    cout << sum << endl;
    return 0;
}
