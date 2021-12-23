#include <iostream>
using namespace std;


bool isReadable(long long vowels, long long consts) {
    if (vowels + consts == 1) {
        if (vowels == 1) {
            return true;
        }
    } else {
        if (abs(vowels - consts) <= 1) {
            return true;
        }
    }
    return false;
}

string sentence;
int main()
{
    getline(cin, sentence);
    sentence += " ";
    long long v = 0;
    long long c = 0;
    for (long long i = 0; i < sentence.length(); i += 1) {
        char letter = sentence[i];
        if (letter == ' ') {
            if (!isReadable(v, c)) {
                cout << "not readable" << endl;
                return 0;
            }
            v = 0;
            c = 0;
        } else if (letter == 'a' || letter == 'e' || letter == 'i' ||letter == 'o' || letter == 'u') {
            v += 1;
        } else {
            c += 1;
        }
    }
    cout << "readable" << endl;
    return 0;
}
