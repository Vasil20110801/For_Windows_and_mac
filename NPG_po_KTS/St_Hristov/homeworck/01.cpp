#include <iostream>
using namespace std;

int main() {
    int Petq;
    int Galq;

    cout << "Vuvedete chisloto na Petq : ";
    cin >> Petq;
    cout << "Vuvedete chisloto na Galq : ";
    cin >> Galq;

    cout << "Stoinostta na Petq:  " << Petq << "\n";
    cout << "Stoinosta na Galq: " << Galq << "\n";

    int Petq_2 = Petq;
    Petq = Galq;
    Galq = Petq_2;

    cout << "After swap \n";
    cout << "Petq = " << Petq << "\n";
    cout << "Galq = " << Galq << "\n";

    return 0;
}