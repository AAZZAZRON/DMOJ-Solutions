#include <iostream>
#include <vector>
#define boost() cin.tie(0); cin.sync_with_stdio(0)

using namespace std;

long long num, one, two, x, y;
long long counter = 0;
long long lines[100001];
bool done = false;
bool visited[100001][101];
vector<pair<long long, long long> > queued, added;
pair<long long, long long> coord, start, ending;

int check(long long a, long long b) {
    coord.first = a;
    coord.second = b;
    if (1 <= a && a <= num && 1 <= b && b <= lines[a] && !visited[a][b]) {
        visited[a][b] = true;
        added.push_back(coord);
    }
    if (coord == ending) {
        done = true;
    }
    return 0;
}

int main()
{
    boost();
    cin >> num;
    for (int i = 0; i < 100001; i += 1) {
        lines[i] = 0;
        for (int j = 0; j < 101; j += 1) {
            visited[i][j] = false;
        }
    }
    for (int i = 1; i < num + 1; i += 1) {
        cin >> lines[i];
    }
    cin >> start.first >> start.second;
    cin >> ending.first >> ending.second;
    queued.push_back(start);
    visited[start.first][start.second] = true;

    while (!done) {
        added.clear();
        counter += 1;
        for (int i = 0; i < queued.size(); i += 1) {
            one = queued[i].first;
            two = queued[i].second;
            // right
            x = one;
            y = two;
            y += 1;
            if (y > lines[x]) {
                x += 1;
                y = 1;
            }
            check(x, y);

            // left
            x = one;
            y = two;
            y -= 1;
            if (y < 1) {
                x -= 1;
                y = lines[x];
            }
            check(x, y);

            // up
            x = one;
            y = two;
            x -= 1;
            y = min(lines[x], y);
            check(x, y);

            // down
            x = one;
            y = two;
            x += 1;
            y = min(lines[x], y);
            check(x, y);
        }
        queued.clear();
        for (int i = 0; i < added.size(); i += 1) {
            queued.push_back(added[i]);
        }
    }

    cout << counter << endl;
    return 0;
}
