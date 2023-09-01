// Поиск НОД методом Евклида

#include <iostream>

using namespace std;

int main()
{
    int x,y;

    cin >> x;
    cin >> y;
    
    while (x!=0 && y!=0)
    {
        if (x>y)
        {
            x = x%y;
        }else
        {
            y = y%x;
        }
        
    }
    
    cout << (x+y) << '\n';

    return 0;
}