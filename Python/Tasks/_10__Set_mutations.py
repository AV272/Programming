'''
Ввод:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

Задача:
Считать все множества и команды изменения множества. Вывести сумму элементов полученного множества.

Примечание:
Рассматриваются функции, которые изменяют множество над которым действуют (в отличии от предыдущих (без update))
A.update(B) -- объединение
A.intersection_update(B) -- пересечение
A.symmetric_difference_update(B) -- объединение без элементов входящих в оба множества
A.difference_update(B) -- разница 
'''

n = int(input())
A = set(map(int,input().split()))
nn = int(input())
for i in range(nn):
    com = input().split()
    eval('A.'+com[0]+'(set(map(int,input().split())))') # Функция eval() воспринимает строку как команду
print(sum(A))
