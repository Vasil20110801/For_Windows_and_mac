#include <iostream>
using namespace std;

void FibonacciIterative(int n) {
    int a = 0, b = 1;

    for (int i = 0; i < n; ++i) {
        cout << a << (i == n - 1 ? "" : " ");
        int next = a + b;
        a = b;
        b = next;
    }
    cout << '\n';
}


void printFibonacciRecursive(int n,int  a = 0, int  b = 1) {
    if (n <= 0) {
        cout << '\n';
        return;
    }

    cout << a << (n == 1 ? "" : " ");
    printFibonacciRecursive(n - 1, b, a + b);
}

int main() {
    int n;
    cout << "Въведи брой числа (n): ";
    cin >> n;

    if (n <= 0) {
        cout << "Моля, въведи положително число.\n";
        return 0;
    }

    cout << "Итеративно: ";
    FibonacciIterative(n);

    cout << "Рекурсивно: ";
    printFibonacciRecursive(n);

    return 0;
}