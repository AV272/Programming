#include <iostream>
using namespace std;

int main()
{
    int n, k;

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
    B[k-1] = A[n-1];
    k = k-2;

    for (int i = 0; i < k; i++)
    {
        float mid = (A[n-1] - A[0])/2;
        int j = 1;
        while (A[j] - A[0] < mid)
        {
            
            j++;
        }
        if (A[j] - mid < mid - A[j-1] )
        {

        }
    }
    






    for (int i = 0; i < n; i++)
    {
        cout << A[i] << '\t';
    }
    
    
    
    
    
    delete[] A;
    delete[] B;
    return 0;
}