#include <iostream>

using namespace std;

void print_array(int A[], int N)
{
    for(int i = 0; i < N; i++)
        cout << A[i] << ' ';
    cout << '\n';
}

void radix_sort(int *A, int N, int radix_max)
{
    int *a0 = new int[N];
    int *a1 = new int[N];
    
    for(int radix = 0; radix < radix_max; radix++) {
        int a0_size = 0;
        int a1_size = 0;
        for(int i = 0; i < N; i++) {
            if ((A[i] & (1 << radix)) == 0)
                a0[a0_size++] = A[i];
            else
                a1[a1_size++] = A[i];
        }
        for(int i = 0; i < a0_size; i++)
            A[i] = a0[i];
        for(int i = 0; i < a1_size; i++)
            A[a0_size + i] = a1[i];
        
        print_array(A, N);
    }
    
    delete[] a0;
    delete[] a1;
}

int length(int n) {
    int l = 0;
    do {
        l++;
        n /= 10;
    } while(n);
    return l;
}

int main()
{
    int N, temp, k=0, radix_max = 0;
    int *A = new int[1000];
    while (cin >> temp) {
        A[k] = temp;
        if (length(temp) > radix_max)
        {
            radix_max = length(temp);
        }
        k++;
    }
    N = k;

    radix_sort(A, N, radix_max);
    

    return 0;
}