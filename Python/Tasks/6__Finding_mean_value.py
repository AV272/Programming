'''
Ввод: 
3
Test1 30 31 32
Test2 20 21 22
Test3 10 11 12
Test2

Задача:
Создать словарь с ключом Test и списком чисел в качестве значения словаря. 
Вычислить среднее значение указанного в конце ключа (Test2) и вывести с точность до двух знаков после запятой.
'''


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = student_marks[query_name]
    print('%.2f' % (sum(x)/len(x)))
