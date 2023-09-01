#include <iostream>
using namespace std;

int main()
{
    int x;
    cin >> x;
    int tmp = x;
    int i = 2;

    while (i < x)
    {
        if (x%i == 0)
        {
            cout << i << '\n';
            x = x/i;
        }else
        {
            i += 1;
        }
    }

    if (x!= tmp)
    {
        cout << x;
    }
        
    return 0;
}