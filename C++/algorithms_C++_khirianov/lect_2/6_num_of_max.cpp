//Найти количество элементов равных максимуму
#include <iostream>
using namespace std;

int main()
{
    int N = 10000;
    int A[N];
    int x;
    int topA = 0;
    int num_of_max = 1;

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
    
    for (int i = 0; i < topA-1; i++)
    {
        if (A[i]>A[i+1])
        {
            int tmp = A[i];
            A[i] = A[i+1];
            A[i+1] = tmp;
            
        }else if (A[i] == A[i+1])
        {
            num_of_max +=1;
        }else
        {
            num_of_max = 1;
        }
        
    }
    
    cout << num_of_max;
    
    return 0;
}