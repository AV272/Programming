'''
Ввод:
3
Russia
Uk
Russia

Задача:
Посчитать сколько не повторяющихся стран в списке.

Примечание:
Использвать функцию множества set(), которая создает набор неповторяющихся элементов.
set.add() -- добавление элемента к множеству.

'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
ls = []
for i in range(n):
    x = input()
    ls.append(x)
s = set(ls)
print(len(s))


# With set function
n = int(input())
s = set()
for i in range(n):
    x = input()
    s.add(x)
print(len(s))
