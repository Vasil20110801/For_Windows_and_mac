#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> numbers;
    vector<int> reverse_numbers;
    int n ;
    cout << "Enter digit: ";
    cin >> n ;
    while (n != 0 ){
        numbers.push_back(n);
        cout << "Enter again: ";
        cin >> n ;
    }
    for (int i  = numbers.size() - 1;i >= 0  ;i--){
        reverse_numbers.push_back(numbers[i]);
    }
    cout << "Reverse numbers: ";
    cout << "[";
    for (int i = 0 ;i < reverse_numbers.size();i ++){
        cout << reverse_numbers[i];
        if (i < reverse_numbers.size() -1){
            cout<< ", ";
    }
    }
    cout << "]";
    return 0 ;
}   