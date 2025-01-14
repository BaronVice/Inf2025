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
