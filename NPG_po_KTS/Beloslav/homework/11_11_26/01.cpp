#include <iostream>

using namespace std;


int iteraciq(int n) {
    int sum = 0;
    if (n < 0) n = -n;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }

    return sum;

}

int main() {
    int n = 1234;

    cout << "Числото е  -- : " << n << endl;
    cout << "Итерация -- : " << iteraciq(n) << endl;

    return 0;
}