"""
Задача:
Один игрок ищет все комбинации букв начинающихся с согласной, другой - начинающиеся с гласной.
Записать победителя и кол-во очков.

Примечание:
string = 'BANANA'
for i =1: 'A': [A, AN, ANA, ANAN, ANANA] = len(string)-i

"""
    
    
    
    string = input()
    l = len(string)
    vowels = ['A','E','I','O','U']
    k=0
    st = 0
    for i in range(l):
        if string[i] in vowels:
            k += l-i
        else:
            st += l-i
    if k>st:
        print('Kevin ' + str(k))
    elif k<st:
        print('Stuart ' + str(st))
    else:
        print('Draw')
