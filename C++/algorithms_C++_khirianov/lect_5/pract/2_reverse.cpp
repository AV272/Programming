#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int A[N];

    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    
    
    for(int i = 0; i < N / 2; i++) {
        int tmp = A[i];
        A[i] = A[N-1-i];
        A[N-1-i] = tmp;
    }
    
    for(int i = 0; i < N; i++) {
        cout << A[i] << ' ';
    }

    return 0;
}