'''
Ввод:
3
insert 0 9
insert 1 5
sort

Задача:
Считать введеные команды и выполнить их 

Consider a list (list = []). You can perform the following commands:
  1. insert(position,element): Insert integer elem. at position pos.
  2. print(list): Print the list.
  3. remove(element): Delete the first occurrence of integer elem.
  4. append(element): Insert integer element at the end of the list.
  5. sort(): Sort the list.
  6. pop(): Pop(delete) the last element from the list.
  7. reverse(): Reverse the list.
'''


if __name__ == '__main__':
    N = int(input())
    ls =[]
    for i in range(N):
        arr, *arr2 = input().split()
        arr3 = list(map(int, arr2))
        if arr == 'insert':
            ls.insert(arr3[0],arr3[1])
        elif arr =='print':
            print(ls)
        elif arr == 'remove':
            ls.remove(arr3[0])
        elif arr == 'append':
            ls.append(arr3[0])
        elif arr == 'sort':
            ls.sort()
        elif arr == 'pop':
            ls.pop()
        elif arr == 'reverse':
            ls.reverse()
