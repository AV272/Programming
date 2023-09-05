#include <iostream>

using namespace std;

int main()
{
	int n = 1000000, num;
	cin >> num;

	bool sieve[n+1];
    sieve[0] = false;
    sieve[1] = false;
    
	for(int i=2; i < n+1; i++){
		sieve[i] = true;

	}
	int x = 2;
	while (x*x <= n){
		if (sieve[x]){
			for (int y = x*x; y <= n; y += x){
				sieve[y] = false; 
			}
		}
		x += 1;

	}
	// выводим номера ячеек с true
    int i2=0, i3;
	for (int i =2; i < n+1; i++){
		if (sieve[i]){
			i2++;
		}
        if (i2 == num)
        {
            i3 = i;
            break;
        }
	}

	cout << i3;

	return 0;
}