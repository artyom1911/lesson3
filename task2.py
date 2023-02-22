"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5"""

list_1 = []

count = 0
eq=0
rng = int(input())
for i in range(rng):
    list_1.append(1 + i)
print(list_1)
number = int(input())
for i in range(rng):
    if list_1[i] == number:
        eq = number
    elif number == 0:
        eq = list_1[0]
    elif number > list_1[i]:
        eq = list_1[i]
print(eq)