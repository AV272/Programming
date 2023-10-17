'''
Задача: 
Нарисовать индийский рисунок рагноли из букв.
'''

import string
def print_rangoli(size):
    # your code goes here
    let = string.ascii_lowercase      # записываем все буквы нижнего регистра
    l = n*4-3                         # ширина рисунка
    L=[]
    for i in range(1,n+1):
        s = '-'.join(let[(n-i):n])                  # добавляет к итерируемому списку разделитель между элементами '-'
        print((s[::-1]+s[1:]).center(l,'-'))        # s[bigin:end:step] step (-1) означает в обратном порядке.
    for i in range(1,n):                            # str.center(width,'full') дополнить str до ширины width, обложив элементами 'full'
        s = '-'.join(let[i:n])
        print((s[::-1]+s[1:]).center(l,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
