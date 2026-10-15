#include <iostream>
using namespace std;




int main() {

  int i = 6 ;
    if ((i & 1 ) == 0) {
        cout << i <<"cetno"<<  endl;
    }
    else {
        cout << i <<"necetno"<< endl;
    }


    int n = 9;
    int g = 8;

     cout << "predi razmqnata "<< n << g << endl;


    n = n ^ g;
    g = n ^ g ;
    n = n ^ g;

    cout << "sled razmqnata "<< n << g << endl;

}