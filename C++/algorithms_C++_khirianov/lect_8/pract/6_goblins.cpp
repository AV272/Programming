#include <iostream>

using std::cout;
using std::cin;
using std::string;


int main()
{
    int n, num, j=0, tmp, middle, tmp2;
    char rang;
    cin >> n;
    int *arr = new int[n];
    for (int i = 0; i < n; i++)
    {
        cout << j << '\n';
        cin >> rang;
        cout << rang << '\n';
        if (rang == '-')
        {
            cout << "--- case" << '\n';
            cout << arr[0] << '\n';
            for (int k = 0; k < j; k++)
            {
                arr[k] = arr[k+1];
            }
            j = j-1;
            continue;
        }
        cin >> num;
        cout << num << '\n';
        if (rang == '+')
        {
            cout << "+++ case" << '\n';
            arr[j] = num;
            j++;
        }else
        {
            cout << "*** case" << '\n';
            middle = j/2;
            cout << middle << '\n';
            if (j%2 ==0)
            {
                cout << "even case" << '\n';
                tmp = arr[middle];
                arr[middle] = num;
                cout << middle << ' ' << tmp << ' ' << arr[middle] << '\n';
                for (int k = 0; k < middle; k++)
                {
                    tmp2 = arr[middle + k + 1];
                    arr[middle + k + 1] = tmp;
                    tmp = tmp2; 
                    
                }
                // в tmp и tmp2 находится шум
                
            }else
            {
                cout << "odd case" << '\n';
                tmp = arr[middle + 1];
                arr[middle + 1] = num;
                for (int k = 0; k < middle; k++)
                {
                    
                    tmp2 = arr[middle + k + 2];
                    arr[middle + k + 2] = tmp;
                    tmp = tmp2;
                    
                }
            }
            j++;
            
        }
    }
    
    delete[] arr;
    return 0;
}
