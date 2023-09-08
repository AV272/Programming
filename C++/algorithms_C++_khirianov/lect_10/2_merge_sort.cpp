#include <iostream>
#include <array>

const int MAX_ARRAY_SIZE = 100000;

void merge_sort(double *array, int16_t array_size)
{
    if (array_size <= 1) return;
    
    int16_t middle = array_size/2;
    double *left = array;
    double *right = array + middle;
    // beware using address arithmetics: pointer + number
    int16_t left_size = middle;
    int16_t right_size = array_size - left_size;

    // recursion starts here
    merge_sort(left, left_size);
    merge_sort(right, right_size); 
    
    // Merge two sorted parts of array
    double *buffer = new double[array_size];
    int16_t left_i = 0;
    int16_t right_i = 0;
    int16_t buffer_i = 0;

    while (left_i < left_size and right_i < right_size)
    {
        if (left[left_i] <= right[right_i])
        {
            buffer[buffer_i] = left[left_i];
            left_i++;
            buffer_i++;   
        }else
        {
            buffer[buffer_i] = right[right_i];
            right_i++;
            buffer_i++;
        }
        
    }

    while (left_i < left_size)
    {
        buffer[buffer_i] = left[left_i];
        left_i++;
        buffer_i++;
    }
    while (right_i < right_size)
    {
        buffer[buffer_i] = right[right_i];
        right_i++;
        buffer_i++;
    }

    // copy from buffer
    for (int16_t i = 0; i < array_size; i++)
    {
        array[i] = buffer[i];
    }
    delete[] buffer;
}

void input_array(double *array, int16_t n)
{
    for (int i = 0; i < n; i++)
    {
        std::cin >> array[i];
    }
    
}

void print_array(double *array, int16_t n)
{
    for (int i = 0; i < n; i++)
    {
        std::cout << array[i] << ' ';
    }
    std::cout << '\n';
}

int main()
{
    int16_t array_size;
    std::cout << "Enter size of array: ";
    std::cin >> array_size;

    if (array_size <= 0 or array_size > MAX_ARRAY_SIZE)
    {
        std::cerr << "Your array size is unacceptable!\n";
        return 1;
    }

    double *array = new double[array_size];

    input_array(array, array_size);
    merge_sort(array, array_size);
    print_array(array, array_size);

    delete[] array;

    return 0;
}