#include <iostream>
using namespace std;

int main()
{
    int n, ident =0;
    bool flag=true;
    cin >> n;

    int *A = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    
    while (flag)
    {
        flag = false;
        for (int i = 0; i < n-1; i++)
        {
            if (A[i]>A[i+1])
            {
                int tmp = A[i]; 
                A[i] = A[i+1];
                A[i+1] = tmp;
                flag = true;
            }
        }
    }
    
    for (int i = 0; i < n-1; i++)
    {
        if (A[i] == A[i+1])
        {
            ident++;
        }

        if (ident == 2)
        {
            cout << 0;
            exit(0);
        }
    }
    
    cout << 1;

    delete[] A;
    return 0;
}