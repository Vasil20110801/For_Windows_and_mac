#include <iostream>
#include <vector>
using namespace std;
int main () {
    vector<double> numbers(4);
    double suma = 0 ;
    double n1 ;
    double n2 ;
    double n3 ;
    double n4 ;
    cin >> n1 ;
    suma += n1 ;
    cin >> n2 ;
    suma += n2 ;
    cin >> n3 ;
    suma += n3 ;
    cin >> n4 ;
    suma += n4 ;

    numbers.push_back(n1);
    numbers.push_back(n2);
    numbers.push_back(n3);
    numbers.push_back(n4);

    cout << suma / 4  << endl;
    return 0;

}