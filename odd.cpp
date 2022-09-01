#include <cstdio>

using namespace std;
int n, v, t;
int main() {
    scanf("%d", &n);
    while (n--) {
        scanf("%d", &t);
        v ^= t;
    }
    printf("%d\n", v);
}
