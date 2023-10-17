'''
Ввод:
3
123
3
pop # удаляет первый элемент множества. Так как множество не упорядочено, неизвестно какой элемент будет удален.
remove 2 # удаляет указанный элемент. Если элемента нет выводит ошибку.
discard 3 # Удаляет указанный элемент. Если элемента нет не выводит ошибку.

Задача:
Записать заданные значения в множество. Считать и выполнить следующие команды.
Вывести сумму получившегося множества.

Примечание:
Функция A.union(B) (A|B) объединяет два множества в одно.
Функция A.intersection(B) (A&B) возвращает пересечение двух множеств.
Функция A.difference(B) (A-B) возвращает разницу двух множеств (элементы А которые не входят в В).
Функция A.symmetric_difference(B) (A^B) возвращает элементы которые входят только в какое-нибудь одно множество. 

'''



n = int(input())
s = set(map(int, input().split()))
N = int(input())
command = []
for i in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))

'''
Функция A.union(B) объединяет два множества в одно.
'''
n = int(input())
eng = set(map(int,input().split()))
N = int(input())
french = set(map(int,input().split()))

s = eng.union(french)
print(len(s))

'''
Функция A.intersection(B) возвращает пересечение двух множеств
'''
n = int(input())
eng = set(map(int,input().split()))
N = int(input())
french = set(map(int,input().split()))

s = eng.intersection(french)
print(len(s))
