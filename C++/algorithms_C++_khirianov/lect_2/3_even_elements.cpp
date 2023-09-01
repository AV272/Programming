#include <iostream>

using namespace std;

const int MAX_A_SIZE = 100;

int main()
{
    int N = MAX_A_SIZE;
    int A[N];
    int x;
    int top = 0;
    int num_of_even =0;

    cin >> x;
    while (x != 0){
    	A[top] = x;
	    top += 1;
        if (top > N)
        {
            cout << "Ошибка! Переполнение массива";
            exit(0);
        }

    	cin >> x;
    }

    for (int i = 0; i < top; i++)
    {
        if (A[i]%2 == 0)
        {
            num_of_even +=1;
        }
    }

    cout << num_of_even;

    return 0;
    
}