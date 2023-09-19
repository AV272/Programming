#include <iostream>
using std::cin;
using std::cout;
using std::endl;

struct citizen
{
    char name[20];
    bool status;
    bool alive; 
};


int main()
{
    int n, news, m, alive_num, house=0;
    cin >> n >> news;
    citizen *arr = new citizen[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i].name >> arr[i].status;
        arr[i].alive = true;
    }
    
    cin >> m;
    alive_num = n;
    for (int i = 0; i < m; i++)
    {
        if (!arr[house].alive)
        {
            house++;
        }
        if (alive_num == 1)
        {
            break;
        }
        
        if (news)
        {
            if (!arr[house].status)
            {
                news = 0;
            }
        }else
        {
            if (arr[house].status)
            {
                arr[house].alive = false;
                alive_num -=1;
            }else
            {
                arr[house].status = 1;
                news = 1;
            }
        }
        
        house++;
    }
    
    for (int i = 0; i < n; i++)
    {
        if (arr[i].alive)
        {
            cout << arr[i].name << ' ' << arr[i].status << '\n';
        }
    }
    
    
    delete[] arr;
    return 0;
}