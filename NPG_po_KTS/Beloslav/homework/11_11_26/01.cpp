#include <iostream>

using namespace std;


int iteraciq(int n) {
    int sum = 0;

    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }

    return sum;

}

int main() {
    int n = 1234;
    if (n < 0) n = -n;

    cout << "Числото е  -- : " << n << endl;
    cout << "Итерация -- : " << iteraciq(n) << endl;

    return 0;
}