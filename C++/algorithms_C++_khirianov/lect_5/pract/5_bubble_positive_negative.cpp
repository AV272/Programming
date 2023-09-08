#include <iostream>

using namespace std;

int main()
{
    int N, index_pos, index_neg, tmp;
    cin >> N;
    int A[N];
    

    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    
    bool is_sorted = false;
    while (not is_sorted) {
        int i = 0;
        is_sorted = true;
        int counter_pos = 0;
        int counter_neg = 0;
        while (i < N)
        {
            
            if (A[i]>=0)
            {
                if (counter_pos == 0)
                {
                    index_pos = i;
                    counter_pos++;
                    continue;
                }
                if (A[index_pos] > A[i]) {  
                    tmp = A[i]; 
                    A[i] = A[index_pos];
                    A[index_pos] = tmp;
                    is_sorted = false;
                    
                    for(int j = 0; j < N; j++) {
                        cout << A[j] << ' ';
                    }
                    cout << '\n';
                }
                index_pos = i;
                counter_pos++;
            }else
            {
                if (counter_neg == 0)
                {
                    index_neg = i;
                    counter_neg++;
                    continue;
                }
                if (abs(A[index_neg]) > abs(A[i])) {  
                    tmp = A[i]; 
                    A[i] = A[index_neg];
                    A[index_neg] = tmp;
                    is_sorted = false;
                    
                    for(int j = 0; j < N; j++) {
                        cout << A[j] << ' ';
                    }
                    cout << '\n';
                }
                index_neg = i;
                counter_neg++;
            }
            i += 1;
        }
    }

    return 0;
}