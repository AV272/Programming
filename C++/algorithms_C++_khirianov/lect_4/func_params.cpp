#include <iostream>

void increment(int* a)
{
	std::cout << *a << std::endl;
	*a = *a +1;	// значение по адресу а увеличиться на 1.
	std::cout << *a << std::endl;
}		// однако при выходе из функции указатель а уничтожиться

int  main()
{
	using namespace std;
	int b = 3;

	increment(&b);	// здесь будет скопирован адрес переменной b
	cout << "Variable b " << b << endl;	
	// вызов функции inc(b) не изменил b

	return 0; 
}
