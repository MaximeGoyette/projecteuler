#include <iostream>
using namespace std;

int main() {
    int a = 1;
    int b = 2;
    int total = b;

    while (b < 4000000) {
        int c = a + b;

        if (c%2==0) {
            total += c;
        }

        a = b;
        b = c;
    }

    cout << total << endl;
}