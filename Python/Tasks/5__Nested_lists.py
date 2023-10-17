'''
Задача:
Задан вложенный список из имени и оценки ученика [['alpa',1],['beta',2],['gamma',3]]. Нужно вывести имя второго с конца ученика по успеваемоти.
Если учеников с такой оценкой несколько, то нужно вывести их имена в алфовитном порядке в отдельной строке.

Замечание:
Ввод предполагается следующий:
3 
Test1
52
Test2
53
Test3
53
'''



if __name__ == '__main__':
    stud = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stud.append([score,name])

        
stud.sort()
for i in range(len(stud)):
    if stud[i][0]>min(stud)[0]:
        print(stud[i][1])
        if i==len(stud)-1 or stud[i+1][0]>stud[i][0]:
            break
