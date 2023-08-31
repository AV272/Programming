// Массив неизвестной длинны

#include <iostream>

using namespace std;

const int MAX_A_SIZE = 100;

int main()
{
    int N = MAX_A_SIZE;
    int A[N];
    int x;
    int top =0;
    
    cout << "Enter elements of array" << '\n';
    cin >> x;
    while (x != 0){
    	A[top] = x;
	top += 1;

    	cin >> x;
    }


    for(int i = 0; i < top; ++i) {
        cout << A[i] << '\t';
    }
    cout << '\n';

    return 0;
}
