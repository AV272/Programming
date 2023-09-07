#include <iostream>
using namespace std;

uint64_t factorial(uint16_t n)
{
    if (n==0)
    {
        return 1; // base case
    }else
    {
        return factorial(n-1)*n; // recurrent cases
    }
    
}

int main()
{
    uint16_t x;
    cin >> x;
    cout << factorial(x) << '\n';

    return 0;

}