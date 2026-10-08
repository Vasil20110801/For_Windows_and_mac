#include <iostream>
# include <vector>
using namespace std;

int main(){
    vector<int> numbers;
    int n ;
    cout << "Enter  digit:" ;
    cin >> n ;
    while(n != 0 ){
        numbers.push_back(n);
        cout << "Enter another digit \n";
        cin >> n ;
    }
    if(numbers.empty()){
        cout << "No digit in vector";
        return 0;
    }

    int max_num = numbers[0];
    for (int i = 0 ;i < numbers.size();i++){
        if (numbers[i] > max_num){
            max_num = numbers[i] ;
        }
    }
    cout << "Max num is :"<<max_num<<endl;
    return 0 ;
    

}