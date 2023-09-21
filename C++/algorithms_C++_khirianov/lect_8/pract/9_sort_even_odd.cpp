#include <iostream>
using std::cout;
using std::cin;

int main()
{
    int64_t temp;
    int k = 0;
    bool check = true;
    int32_t *arr = new int32_t[10000];
    while (cin >> temp) {
        arr[k] = temp;
        k++;
    }
    int n = k;
    while (check)
    {
        check = false;
        for (int j = 0; j < n-1; j++)
        {
            int buf;
            if (arr[j]%2 != 0 and arr[j+1]%2==0)
            {
                buf = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = buf;
                check = true;
            }else if (arr[j]%2==arr[j+1]%2 and arr[j]>arr[j+1])
            {
                buf = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = buf;
                check = true;
            }
        }

    }
    
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << ' ';
    }
    
    
    delete[] arr;
    return 0;
}
