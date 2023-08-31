#include <iostream>

using namespace std;

void print_array2d(int *A, int N, int M)
{
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cout << A[i*M + j] << '\t'; // A[i][j]
        }
        cout << '\n';
    }
}

int main()
{
    int N, M;
    cin >> N >> M;

    int **A = new int*[N];
    A[0] = new int[N*M];

    for (int i = 0; i < N; i++)
    { //сопоставляем адреса 1d и 2d массивов
        A[i] = A[0] + M*i; 
    }
    

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            A[i][j] = i*M + j;
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cout << A[i][j] << '\t';
        }
        cout << '\n';
    }

    print_array2d(A[0], N, M);

    delete[] A[0];
    delete[] A;
    
    return 0;
}