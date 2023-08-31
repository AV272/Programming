#include <iostream>

using namespace std;

struct t_Pair {
    int a;
    int b;
};

void modify_pair(t_Pair * p) // вызывает адрес переменной
{
    p->a += 1;    // p->a и (*p).b это одно и тоже
    (*p).b += 10; // (*p) переменная на которую указывает адрес p
}

int main()
{
    t_Pair x;
    cin >> x.a >> x.b;

    t_Pair y;
    y = x;

    modify_pair(&x);

    cout << x.a << ' ' << x.b << '\n';
    cout << y.a << ' ' << y.b << '\n';

    return 0;
}
