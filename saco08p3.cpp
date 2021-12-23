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

int matrix[700][700];
int minDistances[700][2], done[700][2], hasCookie[700], numPaths[700][2];
int length, minimumD, found, townInd, townState, previousD;
int num, ind;

using namespace std;

int main()
{
    boost();
    cin >> length;
    for (int i = 1; i <= length; i += 1) {
        for (int j = 1; j <= length; j += 1) {
            cin >> matrix[i][j];
        }
    }
    // initialize arrays
    for (int state = 0; state <= 1; state += 1) {
        for (int i = 0; i <= length; i += 1) {
            hasCookie[i] = 0;
            done[i][state] = 0;
            minDistances[i][state] = -1;
            numPaths[i][state] = 0;
        }
    }

    cin >> num;
    for (int i = 0; i < num; i += 1) {
        cin >> ind;
        hasCookie[ind] = 1;
    }

    minDistances[1][0] = 0;
    numPaths[1][0] = 1;
    
    for (int i = 0; i < length * 2; i += 1) {
        minimumD = -1;
        found = 0;

        // find the closest node
        for (int state = 0; state <= 1; state += 1) {
            for (int j = 1; j <= length; j += 1) {
                if (!done[j][state] && minDistances[j][state] >= 0) {
                    if (minimumD == -1 || minDistances[j][state] < minimumD) {
                        minimumD = minDistances[j][state];
                        townInd = j;
                        townState = state;
                        found = 1;
                    }
                }
            }
        }
        if (!found) {
            break;
        }
        done[townInd][townState] = 1; // set to true

        if (townState == 0 && hasCookie[townInd]) {
            previousD = minDistances[townInd][1];
            if (previousD == -1 || previousD >= minimumD) {
                minDistances[townInd][1] = minimumD;
                if (previousD == minimumD) {
                    numPaths[townInd][1] += numPaths[townInd][0];
                } else {
                    numPaths[townInd][1] = numPaths[townInd][0];
                }
                numPaths[townInd][1] %= 1000000;
            } 
        } else {
            for (int j = 1; j <= length; j += 1) {
                previousD = minDistances[j][townState];
                if (j != townInd) {
                    if (previousD == -1 || previousD >= minimumD + matrix[townInd][j]) {
                        minDistances[j][townState] = minimumD + matrix[townInd][j];

                        if (previousD == minimumD + matrix[townInd][j]) {
                            numPaths[j][townState] += numPaths[townInd][townState];
                        } else {
                            numPaths[j][townState] = numPaths[townInd][townState];
                        }
                        numPaths[j][townState] %= 1000000;
                    }
                }
            }
        }
    }
    cout << minDistances[length][1] << " " << numPaths[length][1] << endl;

    return 0;
}
