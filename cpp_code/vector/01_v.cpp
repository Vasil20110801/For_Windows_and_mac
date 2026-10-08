#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> numbers;
    int n ;
    cin >> n;
    while(n != 0 ){
        numbers.push_back(n);
        cin >> n ;
    }
    cout << "size is "<<numbers.size()<<endl;
    return 0 ;

}