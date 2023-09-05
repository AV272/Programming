#include <iostream>
using namespace std;

int main()
{
    int n, n1, n2, max1, max2, min1, min2;
    cin >> n;
    cin >> max1 >> max2;
    min1 = max1;
    min2 = max2;
    
    if (max1 < max2)
    {
        int x = max1;
        max1 = max2;
        max2 = x;
    }

    if (min1 > min2)
    {
        int y = min1;
        min1 = min2;
        min2 = y;
    }

    for (int i = 0; i < n-2; i++)
    {
        cin >> n1;
        if (max1 <= n1)
        {
            int tmp1 = max1; 
            max1 = n1;
            max2 = tmp1;
        }else if (max2 < n1)
        {
            max2 = n1;
        }

        if (min1 >= n1)
        {
            int tmp2 = min1; 
            min1 = n1;
            min2 = tmp2;
        }else if (min2 > n1)
        {
            min2 = n1;
        }
    }
    
    cout << min1+min2 << " " << max1+max2;
    
    
    
    
    return 0;
}