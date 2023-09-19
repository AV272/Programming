#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float_t x = 1.0, sum = 0.0, n =0.0, sum2 = 0.0;
    while (x!= 0)
    {
        cin >> x;
        sum += x;
        sum2 += x*x;
        n++;
    }
    n = n-1.0;
    float_t m, D, m2;
    m = sum/n;
    m2 = sum2/n;
    D = m2 - m*m;

    m = round(1000.0*m)/1000.0;
    D = round(1000.0*D)/1000.0;

    //cout << m << ' ' << D << '\n';
    printf("%.1f ", m);
    printf("%.1f\n", D);
    
    return 0;
}