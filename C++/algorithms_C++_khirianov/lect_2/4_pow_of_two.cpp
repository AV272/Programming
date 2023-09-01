#include <iostream>

using namespace std;

int main()
{
    int i = 0;
    int power = 2;
    int N = 20;
    int A[N];
    int X;
    int check = 0;
    
    while (power < 10000)
    {
        A[i] = power;
        power = power*2;
        i += 1;
    }

    /*for (int l = 0; l < i; l++)
    {
        cout << A[l] << ' ';
    }*/
    

    cin >> X;

    for (int j = 0; j < i; j++)
    {
        if (A[j] == X)
        {
            check = 1;
            break;
        }
    }

    if (check)
    {
        cout << "YES";
    }else
    {
        cout << "NO";
    }

    return 0;
}