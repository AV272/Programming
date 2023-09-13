#include <iostream>
using std::cin;
using std::cout;
using std::endl;

void my_slightly_less_dumb_reallocation(int** source, unsigned int n_old, unsigned int n_new)
{
    if (*source == NULL)
    {
        cout << "*source = NULL" << endl;
        *source = new int[n_new];
        return;
    }else
    {
        unsigned int k;
        int *copy = new int[n_new];
        if (n_new >= n_old)
        {
            k = n_old;
        }else
        {
            k = n_new;
        }
        for (int i = 0; i < k; i++)
        {
            cout << **(source+i) << endl;
            copy[i] = **(source+i);
        }

        delete[] *source;
        *source = copy;
    }
}

int main() {
    unsigned int n, i;
    cin >> n;
    int *a = NULL;
    my_slightly_less_dumb_reallocation(&a, 0, n / 2);
    for (i = 0; i < n / 2; i++)
        cin >> a[i];
    my_slightly_less_dumb_reallocation(&a, n / 2, n);
    for (; i < n; i++)
        cin >> a[i];
    int sum = 0;
    for (i = 0; i < n; i++)
        sum += a[i];
        cout << a[i] << endl;
    cout << sum << endl;
    my_slightly_less_dumb_reallocation(&a, n, n / 2);
    my_slightly_less_dumb_reallocation(&a, n / 2, 0);
    my_slightly_less_dumb_reallocation(&a, 0, 0);
    return 0;
}