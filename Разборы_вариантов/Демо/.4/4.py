"""
По каналу связи передаются шифрованные сообщения, содержащие только
десять букв: А, B, C, D, E, F, S, X, Y, Z; для передачи используется
неравномерный двоичный код. Для кодирования букв используются
кодовые слова.

А - 00,
B - , 
C - 010,
D - 011,
E - 1011,
F - 1001,
S - 1100,
X - 1010,
Y - 1101,
Z - 111

Укажите кратчайшее кодовое слово для буквы B, при котором код
удовлетворяет условию Фано. Если таких кодов несколько, укажите код
с наименьшим числовым значением.
Примечание. Условие Фано означает, что никакое кодовое слово не является
началом другого кодового слова. Это обеспечивает возможность
однозначной расшифровки закодированных сообщений.
"""

"""
Решим перебором:
0 нет, начало A
1 нет, начало E
00 нет, это A
01 нет, начало C
10 нет, начало E
11 нет, Z начало
000 нет, A начало
001 нет, A начало
010 нет, это C
011 нет, это D
100 нет, начало F
101 нет, начало X
110 нет, начало Y
111 нет, это Z
1000 подходит, дальше не рассматриваем
...
"""

# И напишем решение...

from itertools import * # эта штука нам нужна, чтобы не писать много циклов для генерации кодовых слов

# Нагенерируем различные коды длины от 1 до 6 (их должно быть достаточно для подбора одного слова под условие Фано)
generated = []
for i in range(1, 7):
    p = product("01", repeat = i) # генерация tuple-ов длины i из элементов 0 и 1
    for result in p:
        generated.append( "".join(result) ) # из tuple в строку

answer = "-----------------------"
for word in generated:
    # В задании известны коды девяти букв, добавляем к ним десятый код для B
    words = ["00", "010", "011", "1011", "1001", "1100", "1010", "1101", "111", word]
    # Для каждой пары слов проверим, что одно не является началом второго
    pairs = combinations(words, 2) # комбинации из words длины 2
    # Проверка всех пар на выполнение условия Фано
    is_good = all(
        [False if pair[0].startswith(pair[1]) or pair[1].startswith(pair[0]) else True for pair in pairs]
        # is_good True при условии, что для каждой одно слово не является началом другого и наоборот
    )
    if is_good:
        # Если длина разная, то проверяем по длине
        if len(answer) > len(word): answer = word
        # Иначе если они одной длины, то берем по наименьшему числовому значению
        elif len(answer) == len(word) and answer > word: answer = word

print(answer) # 1000
