#include <iostream>
#include <cmath>

using std::cout;
using std::cin;
using std::round;
using std::string;

double find_root(double f, float a, float b, float tol)
{
    float mid = (b-a)/2;
    float result, f_round;
    int iter;
    while (b-a > tol and iter< 20000)
    {
        float middle = (a + b) / 2;
        f_round = round(f(middle)*1000000.0)/1000000.0; 
        if (f_round == 0)
        {
            result = middle;
            break;
        }
        else if (f(middle)* f(b) < 0)
        {
            a = middle;
        }else
        {
            b = middle;
        }
        iter++;   
    }
    
    return result;
}

int main()
{
    string s;
    getline(cin, s);
    
    return 0;
}
