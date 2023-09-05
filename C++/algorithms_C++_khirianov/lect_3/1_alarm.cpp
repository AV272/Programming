#include <iostream>
#include <string>

using namespace std;

int time2sec(int h, int m, int s)
{
    return h*60*60 + m*60 + s;
}

int main()
{
    string sh1, sm1, ss1;
    int h1, m1, s1;
    string sh2, sm2, ss2;
    int h2, m2, s2;
    
    getline(cin, sh1, ':');
    getline(cin, sm1, ':');
    getline(cin, ss1);
    getline(cin, sh2, ':');
    getline(cin, sm2, ':');
    getline(cin, ss2);

    h1 = stoi(sh1);
    m1 = stoi(sm1);
    s1 = stoi(ss1);
    h2 = stoi(sh2);
    m2 = stoi(sm2);
    s2 = stoi(ss2);
        
    int dif = time2sec(h2,m2,s2) - time2sec(h1,m1,s1);
    
    if (dif < 0)
    {
        dif = 24*3600 + dif;
    }

    cout << dif << '\n';

    return 0;
}