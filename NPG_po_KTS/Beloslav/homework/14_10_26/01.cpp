#include <iostream>
using namespace std;

int main () {


    int led  = 0 ;

  led |= (1 << 3) | (1 << 5);

    led &= ~(1 << 2);

    if (led & (1 << 7)) {
        cout << "Led 7 e on ";
        return 0;
    }

    else {
        cout << "Led 7 e off ";
        return 0 ;
    }
}

