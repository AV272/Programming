#include <iostream>

using namespace std;

int main()
{
    int n, m;
    //n = 3;
    //m = 4;
    cin >> n >> m;

    int A[n][m];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            A[i][j] = i*m + j;
        }
            
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << A[i][j] << '\t';
        }
        cout << '\n';
        
    }
    
    // memory investigation
    int *p = reinterpret_cast<int *>(A);
    for(int i = 0; i < m*n; i++) 
    {
        cout << *(p + i) << ' ';
    }

    cout << '\n';

    return 0;
}