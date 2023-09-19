#include <iostream>

using std::cout;
using std::cin;


int main()
{
    int n;
    cin >> n;

    int A[n][n], B[n][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> A[i][j];
        }
            
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            B[i][j] = A[n-j-1][i];
        }
        
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << B[i][j] << ' ';
        }
        cout << '\n';
        
    }

    return 0;
}