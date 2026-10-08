# include <iostream>
# include <string>
using namespace std;

int main(){
    string name ;
    int age;
    cout << "What is your name\n";
    cin >> name;
    cout << "Nice to meet you "<< name << ".\n" ;
    cout << "How old are you\n";
    cin >> age;
    while (age < 7 ||age > 150 ){
        cout<<"Error!Enter again age \n";
        cin >> age; 
    }


    cout << "Ti si roden prez "<< (2026 - age) <<"!\n";
    if (age < 18){
        cout <<"Ti si maluk";
    }
    else {
        cout << " Ti si mnogo durt\n";

    }
    return 0 ;
}

