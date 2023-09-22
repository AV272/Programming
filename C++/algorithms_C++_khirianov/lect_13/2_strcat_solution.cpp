#include <string>
#include <iostream>

int main()
{
    // Используется для ускорения ввода/вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    std::string hello = "Hello world! ";
    std::string result;

    std::cout << hello << '\n';
    int times_to_concatinate;
    std::cin >> times_to_concatinate;

    for (int i = 0; i < times_to_concatinate; i++)
    {
        result += hello;
    }

    std::cout << result << '\n';

    return 0;
    
}