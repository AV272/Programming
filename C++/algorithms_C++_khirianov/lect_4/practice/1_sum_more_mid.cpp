#include <iostream>
using namespace std;

int main()
{
    int n, sum=0, sum2=0;
    float mid;
    
    cin >> n;

    int *A = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
        sum = sum + A[i];
    }
    
    mid = sum/n;

    for (int i = 0; i < n; i++)
    {
        if (A[i]>mid)
        {
            sum2 = sum2 + A[i];
        }
    }
    
    
    
    cout << sum2;
    
    delete[] A;
    return 0;
}