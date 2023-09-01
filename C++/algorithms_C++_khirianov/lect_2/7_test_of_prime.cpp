#include <iostream>
using namespace std;

int main()
{
    int n;
	cin >> n;

    // создаем булев массив необходимой длинны с всеми true
	bool sieve[n+1]; 
	sieve[0] = false;
    sieve[1] = false;
    for(int i=2; i < n+1; i++){
		sieve[i] = true;

	}
    // по порядку ставим элементы составные как false 
	int x = 2; 
    // начинаем с квадрата элемента т.к. остальные уже есть
	while (x*x <= n){ 
		if (sieve[x]){
			for (int y = x*x; y <= n; y += x){
				sieve[y] = false; 
			}
		}
		x += 1;

	}
	
	cout << sieve[n];
	return 0;


}