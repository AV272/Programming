#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;

int main()
{
    int topA = 0;
    int N = 100;
    int sum = 0;
    int speed;
    string number;
    string boss("A999AA");
    char n[3];


    cin >> speed >> number;
    while (number.compare(boss)){
    	topA += 1;
        if (topA > N)
        {
            cout << "Ошибка! Переполнение массива";
            exit(0);
        }

        if (speed > 60)
        {
            size_t len =  number.copy( n, 3, 1);
            if (n[0] == n[1]||n[0] == n[2])
            {
                if(n[1]==n[2])
                {
                    sum += 1000;
                }else
                {
                    sum += 500;
                }
            }else if (n[1]==n[2])
            {
                sum += 500;
            }else
            {
                sum += 100;
            }
        }
        
        // cout << typeid(n).name() << '\n';
        
    	cin >> speed >> number;
    }

    cout << sum << '\n';

    return 0;

}