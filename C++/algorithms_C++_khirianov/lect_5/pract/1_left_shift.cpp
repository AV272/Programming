#include <iostream>
using namespace std;

int main()
{
    int n, m, pos;
    bool flag=true;
    cin >> n >> m;

    int *A = new int[n];
    int *B = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++)
    {
        
        if (i>=m)
        {
            pos = i-m;
        }else
        {
            pos = n-(abs(i-m)%n);
            
            if (pos==n)
            {
                pos = 0;
                
            }
        }
        
        B[pos] = A[i];
        
    }

    for (int i = 0; i < n; i++)
    {
        cout << B[i] << ' ';
    }

    delete[] A;
    return 0;
}