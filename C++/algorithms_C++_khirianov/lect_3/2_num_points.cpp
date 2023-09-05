#include <iostream>

using namespace std;

int main()
{
    int n, x, y, quat1=0, quat2=0, quat3=0, quat4=0;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        if (x ==0 || y==0)
        {
            continue;
        }
        if (x>0)
        {
            if (y>0)
            {
                quat1++;
            }else
            {
                quat4++;
            }
        }else
        {
            if (y>0)
            {
                quat2++;
            }else
            {
                quat3++;
            }
        }
    }
    
    if (quat1 >= quat2)
    {
        if (quat1 >= quat3)
        {
            if (quat1 >= quat4)
            {
                cout << 1 << " " << quat1;

            }else
            {
                cout << 4 << " " << quat4;
            }
        }else if (quat3 >= quat4)
        {
            cout << 3 << " " << quat3;
        }else
        {
            cout << 4 << " " << quat4;
        }

    }else if  (quat2 >= quat3)
    {
        if (quat2 >= quat4)
        {
            cout << 2 << " " << quat2;
        }else
        {
            cout << 4 << " " << quat4;
        }
    }else if (quat3 >= quat4)
    {
        cout << 3 << " " << quat3;
    }else
    {
        cout << 4 << " " << quat4;
    }



    return 0;
}