#include <iostream>
using namespace std;

const int MAX_DIGITS = 100;

void generate_binary_numbers(int digits_left_to_generate)
{
    static int digits_combinations[MAX_DIGITS];
    static int top = 0;
    if (digits_left_to_generate == 0)
    { //base case
        for (int i = 0; i < top; i++)
        {
            cout << digits_combinations[i];
        }
        cout << '\n';
        
    }else
    {// recursive case
        digits_combinations[top++] = 1;
        generate_binary_numbers(digits_left_to_generate -1);
        top--;

        digits_combinations[top++] = 0;
        generate_binary_numbers(digits_left_to_generate -1);
        top--;
    }
}

int main()
{
    int n;
    cin >> n;
    generate_binary_numbers(n);
        
    return 0;
}