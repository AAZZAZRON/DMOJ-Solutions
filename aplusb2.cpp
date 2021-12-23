#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <queue>
#define ll long long
#define pii pair<int, int>
#define boost() cin.tie(0); cin.sync_with_stdio(0)
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
int n;
int add;
int lenX, lenY, tmpX, tmpY, tmp, sub, del;
bool addNeg;
string one, two, rVar, sTmp;

string reverseStr(string str) {
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);
    return str;
}

string addition(string x, string y) {
    string result = "";
    int carry = 0;
    lenX = x.size() - 1;
    lenY = y.size() - 1;
    while (lenX >= 0 || lenY >= 0) {
        if (lenX < 0) {
            tmpX = 0;
            tmpY = y[lenY] - 48;
        } else if (lenY < 0) {
            tmpY = 0;
            tmpX = x[lenX] - 48;
        } else {
            tmpX = x[lenX] - 48;
            tmpY = y[lenY] - 48;
        }
        tmp = tmpX + tmpY + carry;
        sTmp = to_string(tmp);
        if (sTmp.size() > 1){ 
            result += sTmp[1];
            carry = 1;
        } else {
            carry = 0;
            result += sTmp;
        }
        lenX -= 1;
        lenY -= 1;
    }
    if (carry == 1) result += "1";
    return reverseStr(result);
}

string subtraction(string x, string y) {
    string result = "";
    lenX = x.size() - 1;
    lenY = y.size() - 1;

    while (lenX >= 0 || lenY >= 0) {
        if (lenX < 0) {
            tmpX = 0;
            tmpY = y[lenY] - 48;
        } else if (lenY < 0) {
            tmpY = 0;
            tmpX = x[lenX] - 48;
        } else {
            tmpX = x[lenX] - 48;
            tmpY = y[lenY] - 48;
        }
        tmp = tmpX - tmpY;
        if (tmp < 0) {
            int tmpX = lenX - 1;
            while (tmpX >= 0 && x[tmpX] == '0') {
                x[tmpX] += 9;
                tmpX -= 1;
            }
            x[tmpX] -= 1;
            tmp += 10;
        }
        result += to_string(tmp);

        lenX -= 1;
        lenY -= 1;
    }

    return reverseStr(result);
}


int main()
{
    boost();
    cin >> n;
    for (int q = 0; q < n; q += 1) {
        addNeg = 0;
        cin >> one >> two;
        add = 1;
        if (one[0] == '-') {
            add -= 1;
            one.erase(0, 1);
            sub = 1;
        }
        if (two[0] == '-') {
            add -= 1;
            two.erase(0, 1);
            sub = 2;
        }
        if (add == 1) rVar = addition(one, two);
        else if (add == -1) {
            addNeg = 1;
            rVar = addition(one, two);
        }
        else {
            addNeg = 1;
            if (sub == 1) { 
                swap(one, two);
            }
            if (two.length() > one.length()) rVar = subtraction(two, one);
            else if (one.length() == two.length() && max(one, two) == two) {
                rVar = subtraction(two, one);
            }
            else {
                addNeg = 0;
                rVar = subtraction(one, two);
            }
        }
        del = 0;
        while (del < rVar.length() && rVar[del] == '0') del += 1;
        rVar.erase(0, del);
        if (rVar == "") cout << 0 << endl;
        else if (addNeg) cout << '-' << rVar << endl;
        else cout << rVar << endl;
    }

    return 0;
}
