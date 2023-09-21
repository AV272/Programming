#include <iostream>
using std::cout;
using std::cin;

int main()
{
    int n, dist, min_dist, left, left_num;
    cin >> n;
    int *arr = new int[n];
    min_dist = n;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    
    for (int i = 0; i < n; i++)
    {
        if (arr[i] < 0)
        {
            left = abs(arr[i]);
            left_num = i;
            for (int j = i+1; j < n; j++)
            {
                if (arr[j]==left)
                {
                    dist = j-i;
                    if(dist < min_dist)
                    {
                        min_dist = dist;
                    }
                }
            }
            

        }
    }
    
    if (min_dist == n)
    {
        cout << 0;
    }else
    {
        cout << min_dist;
    }
    
    delete[] arr;
    return 0;
}
