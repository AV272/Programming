#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	bool sieve[n+1]; // создаем булев массив необходимой длинны с всеми true 
	for(int i=2; i < n+1; i++){
		sieve[i] = true;

	}
	int x = 2; // по порядку ставим элементы составные как false 
	while (x*x <= n){ // начинаем с квадрата элемента т.к. остальные уже есть
		if (sieve[x]){
			for (int y = x*x; y <= n; y += x){
				sieve[y] = false; 
			}
		}
		x += 1;

	}
	// выводим номера ячеек с true
	for (int i =2; i < n+1; i++){
		if (sieve[i]){
			cout << i << '\t';
		}
	}
	cout << '\n';
	return 0;
}
