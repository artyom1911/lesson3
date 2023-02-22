"""Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12"""

c = 0

x_1 = ({x: 1 for x in 'AEIOULNSTRАВЕИНОРСТ'})
x_2 = ({x: 2 for x in 'DGДКЛМПУ'})
x_3 = ({x: 3 for x in 'BCMPБГЁЬЯ'})
x_4 = ({x: 4 for x in 'FHVWYЙЫ'})
x_5 = ({x: 5 for x in 'KЖЗХЦЧ'})
x_6 = ({x: 8 for x in 'ШЭЮJX'})
x_7 = ({x: 10 for x in 'QZФЩЪ'})

x = x_1|x_2|x_3|x_4|x_5|x_6|x_7

word = input()
split_word = list(word)
print(split_word)
split_word_upper = [v.upper() for v in split_word]
print(split_word_upper)
for i in range(len(split_word_upper)):
    c = x.get(split_word_upper[i]) + c
print(c)