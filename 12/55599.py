# https://inf-ege.sdamgia.ru/problem?id=55599

"""
Дана программа для редактора:

НАЧАЛО
    ПОКА НЕ нашлось (00)
        заменить (02, 101)
        заменить (11, 2)
        заменить (12, 21)
        заменить (010, 00)
    КОНЕЦ ПОКА
КОНЕЦ

Известно, что исходная строка A содержала ровно два нуля — на первом и на последнем месте,
а также поровну единиц и двоек, при этом всего в строке A было более 140 цифр.
После выполнения данной программы получилась строка B, сумма цифр которой оказалась простым числом.

Какое наименьшее количество единиц могло быть в строке A?

* Пусть
1) заменить (02, 101) это операция a
2) заменить (11, 2) это операция b
3) заменить (12, 21) это операция c
4) заменить (010, 00) это операция d

* Заметим, что
1) операция d завершающая
2) можно выстроить s так, чтобы a, b и с выполнялись нужное нам количество раз
3) сумма строки B = сумма A-1: (при выполнении a, b и c сумма не меняется, при d становится на 1 меньше)
"""

# В строке было более 140 символов, из них 2 нуля -> 1 и 2 было как минимум по 69
for i in range(69, 1000):
    # Поскольку 1 и 2 было поровну, то сумма B считается так
    sum_b = 1*i + 2*i - 1
    # Здесь проверяем условие простоты суммы B
    is_prime = True
    for j in range(2, int(sum_b**0.5) + 1):
        if sum_b % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
        break