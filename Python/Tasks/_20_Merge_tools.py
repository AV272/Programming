'''
Задача:
Нарезать заданную строку на куски заданного размера (к) и оставить в них только неповторяющиеся буквы.
Вывести на экран получившиеся строки.

'''

string, k = input(), int(input())
cut = int(len(string)/k)
for i in range(cut):
    c = string[k*i:k*i+k]
    uni =''
    for i2 in range(k):
        if c[i2] in uni:
            continue
        else:
            uni += c[i2]
    print(uni)
