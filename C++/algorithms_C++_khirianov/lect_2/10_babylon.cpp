#include <iostream>
#include <string>
using namespace std;

int main()
{
    int x, z;
    cin >> x;
    int it = 0;
    int N = 100;

    string *y = new string[N];

        
    while (x >= 60)
    {
        z = x%60;
        
        for (int i = 0; i < z%10; i++)
        {
            y[it] = "v";
            it += 1;
        }

        for (int i = 0; i < z/10; i++)
        {
            y[it] = "<";
            it += 1;
        }
        
        y[it] = ".";
        it +=1;
            
        x = x/60;
        
    }

    z = x;

    for (int i = 0; i < z%10; i++)
    {
        y[it] = "v";
        it += 1;
    }

    for (int i = 0; i < z/10; i++)
    {
        y[it] = "<";
        it += 1;
    }
    
    for(int i = 0; i < N / 2; i++) {
        string tmp = y[i];
        y[i] = y[N-1-i];
        y[N-1-i] = tmp;
    }

    for (int i = 0; i < N; i++)
    {
        cout << y[i]; 
    }

    delete[] y;

    return 0;
    
}