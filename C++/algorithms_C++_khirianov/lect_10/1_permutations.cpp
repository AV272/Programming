#include <iostream>
using namespace std;

void permutations(int16_t number, int16_t current, int16_t buffer[], bool used[])
{
    if (current == number)
    {
        for (int i = 0; i < number; i++)
        {
            cout << buffer[i] << ' ';
        }
        cout << '\n';
    }else
    {
        for (int16_t variant = 0; variant < number; variant++)
        {
            if (not used[variant])
            {
                buffer[current] = variant;
                used[variant] = true;
                permutations(number, current +1, buffer, used);
                used[variant] = false;
            }
        }
    }
}

int main()
{
    int16_t n;
    cout << "Enter length to generate all permutations: ";
    cin >> n;
    if (n > 20)
    {
        cerr << "Your number is too big!";
        return 1;
    }else if (n <= 0)
    {
        cerr << "Your number is negative";
        return 1;
    }
    
    int16_t buffer[n];
    bool used[n] = {false};
    permutations(n, 0, buffer, used);
    
    
    return 0;
}