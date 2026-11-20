#include <iostream>
using namespace std;
int main () {
    int a=5,b=5,c;
    cout <<" a == "<<a<<" b == "<<b<<endl;
    a = a + b;
    b = a - b;
    a = a - b;

    cout <<"After the slap \n a == "<<a<< " b == "<<b<<endl;
