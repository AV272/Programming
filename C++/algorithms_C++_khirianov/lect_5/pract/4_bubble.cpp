#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int A[N];
    

    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    
    bool is_sorted = false;
    while (not is_sorted) {
        int i = 0;
        is_sorted = true;
        while (i < N-1)
        {
            if (A[i] > A[i+1]) { // поднимаем число до большего числа и доходим 
                int tmp = A[i]; // до конца массива находя большие числа
                A[i] = A[i+1];
                A[i+1] = tmp;
                is_sorted = false; // если хотя бы один элемент не сортирован, будет запущена новая итерация
            }
            i += 1;
        }
    }

    for(int i = 0; i < N; ++i) {
        cout << A[i] << ' ';
    }
    
    return 0;
}