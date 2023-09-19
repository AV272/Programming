#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int n, k, left, right, min, max, new_box, k2, k3;
    bool flag = true;

    cin >> n >> k;

    int *A = new int[n];
    int *B = new int[k];

    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }
    
    if (k == 2)
    {
        cout << A[n-1] - A[0];
        exit(0);
    }

    B[0] = A[0];
    B[1] = A[n-1];
    k2 = k-2;
    k3 = 2;
    min = A[n-1] - A[0];
    max = 0;
    new_box = 0;

    for (int i = 0; i < k2; i++)
    {
        for (int j = 1; j < n-1; j++)
        {
            min = A[n-1] - A[0];
            for (int l = 0; l < k3; l++)
            {
                if (abs(A[j] - B[l]) < min)
                {
                    min = abs(A[j] - B[l]);
                }
            }
            if (min > max)
            {
                max = min;
                new_box = j;
            }
        }
        B[i+2] = A[new_box];
        k3++;
    }
    
    while (flag)
    {
        flag = false;
        for (int i = 0; i < k-1; i++)
        {
            if (B[i]>B[i+1])
            {
                int tmp = B[i]; 
                B[i] = B[i+1];
                B[i+1] = tmp;
                flag = true;
            }
        }
    }
    
    int x = A[n-1] - A[0];
    for (int i = 1; i < k; i++)
    {
        if (B[i]-B[i-1]< x)
        {
            x = B[i]-B[i-1];
        }
    }
    
    cout << x;
    
    delete[] A;
    delete[] B;
    return 0;
}