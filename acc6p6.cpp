#include <iostream>
#define boost() cin.tie(0); cin.sync_with_stdio(0)

using namespace std;
int num;
string answers[31] = {
    "A Spoonful of Sugar",
    "A to Z",
    "ALGORITHM",
    "Astrogazer",
    "AWAKE",
    " ",
    "BLSTR",
    "Breathe The Air",
    "Butterfly",
    "Circle Of Life",
    "CONGA",
    "Dance Dance Revolution",
    "Dead Heat",
    "DIVE",
    "DROP OUT",
    "Electronic or Treat!",
    "END OF THE CENTURY",
    "Ev'rybody Wants To Be A Cat",
    "FOLLOW ME",
    "Hanabi",
    "Healing Vision",
    "Illegal Function Call",
    "IRON HEART",
    "Neverland",
    "New Century",
    "Out of focus",
    "RISING FIRE HAWK",
    "Skywalking",
    "Star Trail",
    "The World Ends Now",
    "Voltississimo"};

int main()
{
    boost();
    cin >> num;
    cout << answers[num + 5] << endl;
    return 0;
}

// creds to chelsea, shane, kevin, ryman, and others for helping :)
