#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int do_some_awesome_work(int* a, int*b);

int main() {
    int a, b;
    cin >> a >> b;
    cout << do_some_awesome_work(&a, &b);
        
    return 0;
}