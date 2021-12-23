#include <iostream>
#include <vector>
#define boost() cin.tie(0); cin.sync_with_stdio(0)

using namespace std;

int start, finish, counter, num;
bool squares[10000001];
vector<int> queue;
int main()
{
    boost();
    cin >> start >> finish;
    for (int i = 0; i < 10000000; i += 1) {
        squares[i] = false;
    }
    squares[start] = true;
    queue.push_back(start);
    while (!squares[finish]) {
        vector<int> added;
        counter += 1;
        for (int i = 0; i < queue.size(); i += 1) {
            num = queue[i];
            if (num * 3 <= 10000000 && !squares[num * 3]) {
                added.push_back(num * 3);
                squares[num * 3] = true;
            }
            if (0 <= num - 3 && !squares[num - 3]) {
                added.push_back(num - 3);
                squares[num - 3] = true;
            }
            if (0 <= num - 1 && !squares[num - 1]) {
                added.push_back(num - 1);
                squares[num - 1] = true;
            }
            if (num % 2 == 0 && !squares[num / 2]) {
                added.push_back(num / 2);
                squares[num / 2] = true;
            }
        }
        queue = added;
    }    

    cout << counter << endl;
    return 0;
}
