# https://inf-ege.sdamgia.ru/problem?id=39241

i = 200
s = "1" * i
# Сперва рассмотрим решение перебором: подбираем строку s с количеством единиц i,
# Пока в результате программы не получим s, состоящую только из двоек
while True:
    s = "1" * i
    while "111" in s or "222" in s:
        s = s.replace("111", "22", 1)
        s = s.replace("222", "1", 1)
    # Если в полученной строке содержатся единицы, то строка не подходит
    if "1" in s:
        i += 1
    # Иначе строка подходит - вывод количества единиц
    else:
        print(i)
        break

"""
Иногда решить перебором не получится из-за больших чисел.
Поэтому надо уметь решать аналитически. Как правило такие решения сводятся
к тому, чтобы попробовать применить пару итераций цикла и что-то заметить.

Изначально строка состоит из единиц:
s = 11111111111...
- заменить (111, 22) -> s = 2211111111...
- заменить (222, 1) -> s =  2211111111...
- конец пока
- заменить (111, 22) -> s = 222211111...
- заменить (222, 1) -> s =  1211111...
- конец пока
- заменить (111, 22) -> s = 122211...
- заменить (222, 1) -> s =  111111...

* Заметим, что каждые 3 итерации из строки s удаляется 7 единиц
* Чтобы строка состояла только из двоек на первую итерацию надо остановиться
(На 2-ой появляется 1 в начале строки, на 3-ю двоек нет) - заменить 111 на 22
* Это значит, что строка s в результате алгоритма будет состоять только из двоек,
если i % 7 == 3, где i - количество единиц.
* Для i >= 200 первое такое число 206
"""