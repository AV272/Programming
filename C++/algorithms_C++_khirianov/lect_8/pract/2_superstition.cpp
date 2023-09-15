#include <iostream>
using namespace std;

int main()
{
    int n, x;
    bool check = true;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        if (x%4 ==0)
        {
            if (!(x/1000==4 or x/1000==5))
            {
                cout << x << '\n';
                check = false;
            }else if (x%7 == 0)
            {
                if (!(x/1000==7 or x/1000==1))
                {
                    cout << x << '\n';
                    check = false;
                }else if (x%9 ==0)
                {
                    if (!(x/1000==9 or x/1000==8))
                    {
                        cout << x << '\n';
                        check = false;
                    }
                }
            }else if (x%9 ==0)
            {
                if (!(x/1000==9 or x/1000==8))
                {
                    cout << x << '\n';
                    check = false;
                }
            }
        }else if (x%7 == 0)
        {
            if (!(x/1000==7 or x/1000==1))
            {
                cout << x << '\n';
                check = false;
            }else if (x%9 ==0)
            {
                if (!(x/1000==9 or x/1000==8))
                {
                    cout << x << '\n';
                    check = false;
                }
            }
        }else if (x%9 ==0)
        {
            if (!(x/1000==9 or x/1000==8))
            {
                cout << x << '\n';
                check = false;
            }
        }
    }

    if (check)
    {
        cout << 0;
    }
    
    return 0;
}