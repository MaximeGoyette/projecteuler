#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool is_prime(long n) {
    if (n < 2) {
        return false;
    }
    for (long i=2; i<=sqrt(n); i++) {
        if (n%i==0) {
            return false;
        }
    }
    return true;
}

long next_prime(long n) {
    while (!is_prime(++n));
    return n;
}

int main() {

    long max_factor = 0;
    long n = 600851475143;

    while (n > 1) {

        long i = 2;
        while(n%i != 0) {
            i = next_prime(i);
        }

        if (i > max_factor) {
            max_factor = i;
        }
        n /= i;
    }

    cout << max_factor << endl;

}