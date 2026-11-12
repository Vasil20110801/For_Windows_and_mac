#include <iostream>
using namespace std;

int rekursiq(int n) {
    if (n == 0) return 0;

    return (n % 10) + rekursiq(n / 10);
}

int main() {
    int n = 1234;
    if (n < 0) n = -n;
    cout << "Въведено число е --  " << n << endl;
    cout << "С рекурсия -- : " << rekursiq(n) << endl;

    return 0;
}