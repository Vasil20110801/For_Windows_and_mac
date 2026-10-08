# include <iostream>
# include <vector>
using namespace std;
int main() {
    vector<int> numbers;
    vector<int> even_numbers;
     int n ;
    cout << "Enter numbers: ";
    cin >> n;
    while (n != 0 ) {
        numbers.push_back(n);
        cout << "Enter new number: ";
        cin >> n ;
    }
    for (int i  = 0 ;i < numbers.size(); i++) {
        if (numbers[i] % 2 == 0) {
            even_numbers.push_back(numbers[i]);
        }
    }
    cout << "event numbers is : ";
    cout<<"[";
    for (int i = 0 ;i < even_numbers.size(); i++) {
        cout << even_numbers[i];
        if (i < even_numbers.size() -1){
            cout<< ", ";
        }
    }
    cout << "]";
    return 0;
}


