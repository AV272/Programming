#include <iostream>
using namespace std;

int main()
{
    int N = 100;
    int A[N];
    int B[N];
    int x;
    int topA = 0;
    int num_of_even =0;

    // записываем массив в А
    cin >> x;
    while (x != 0){
    	A[topA] = x;
	    topA += 1;
        if (topA > N)
        {
            cout << "Ошибка! Переполнение массива";
            exit(0);
        }

    	cin >> x;
    }
    
    // находим четные числа и складываем в массив В
    int topB = 0;
    for (int i = 0; i < topA; i++)
    {
        if (A[i]%2 == 0)
        {
            B[topB] = A[i];
            topB += 1;
        }
    }
        
    // находим максимальное число среди четных
    for (int i = 0; i < topB-1; i++)
    {
        if (B[i]>B[i+1])
        {
            int tmp = B[i]; 
            B[i] = B[i+1];
            B[i+1] = tmp;
        }

    }
        
    if (topB == 0)
    {
        cout << 0;
    }else
    {
        cout << B[topB-1];
    }
    
    return 0;
}