#include <iostream>

using namespace std;

int main()
{
    int N, tmp1, tmp2;
    cin >> N;
    int A[N];
    

    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    int first = A[0];
    int last = A[N-1];
    
    for(int i = 0; i < N; i++) {
        
        tmp1 = A[i];
        if (i == N-1)
        {
            A[i] = (tmp2 + A[i] + first)/3;
        }else if (i==0)
        {
            A[i] = (last + A[i] + A[i+1])/3;
        }else
        {
            A[i] = (tmp2 + A[i] + A[i+1])/3;
        }
        
        tmp2 = tmp1;
    
    }
    
    for(int i = 0; i < N; i++) {
        cout << A[i] << ' ';
    }

    return 0;
}