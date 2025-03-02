# 19748 из https://kompege.ru/task

"""
В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее,
какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу самого узла в этой сети.
При этом в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места – нули.
Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и маске.
Например, если IP-адрес узла равен 231.32.255.131, а маска равна 255.255.240.0, то адрес сети равен 231.32.240.0.

Узлы с IP-адресами 157.220.185.237 и 157.220.184.230 принадлежат одной сети.
Какое наименьшее количество IP-адресов, в двоичной записи которых ровно 15 единиц, может содержаться в этой сети?
"""

"""
--- Немного теории ---
В двоичной записи адрес узла состоит из двух частей: первая - адрес сети, вторая - номер узла в сети.
Сопоставив маску и адрес узла можно узнать адрес сети и порядковый номер узла.

Пусть адрес узла 153.202.16.37
В двоичной записи это 10011001.11001010.00010000.00100101
Пусть маска 255.255.128.0
В двоичной записи это 11111111.11111111.10000000.00000000
(важное свойство маски - в двоичной записи сперва идут 1, затем 0)

Сопоставим адрес узла и маску.
- узел  10011001.11001010.0|0010000.00100101
- маска 11111111.11111111.1|0000000.00000000
* Часть, где у маски 1 - относится к адерсу сети
* Часть, где у маски 0 - порядковый номер узла в сети
- сеть  10011001.11001010.00000000.00000000 (при желании можно перевести в десятичную запись)
- номер узла:
0010000.00100101 (уберем разделитель)
001000000100101  (теперь перевод в десятичную запись через int("001000000100101", 2))
4133

--- Решение ---
Узел1 157.220.185.237
Узел2 157.220.184.230

Переведем в двоичную запись
Узел1 10011101.11011100.10111001.11101101
Узел2 10011101.11011100.10111000.11100110

* Какое наименьшее количество IP-адресов, в двоичной записи которых ровно 15 единиц, может содержаться в этой сети?
-> Чем больше 1 в маске, тем меньше адресов доступно сети -> тем меньше адресов, в двоичной записи которых ровно 15 единиц. 

Минимально возможная маска: 10000000.00000000.00000000.00000000 (в теории да, но на практике нет)
Максимально возможная: набираем биты узла/сети слева направо пока они совпадают
Узел1 10011101.11011100.1011100|1.11101101
Узел2 10011101.11011100.1011100|0.11100110
* Из чего адрес сети 10011101.11011100.1011100|0.00000000

На основании этого построим маску (первая часть из 1, вторая из 0)
Маска 11111111.11111111.11111110.00000000

Количество доступных узлов = 2**количество_нулей_в_маске = 2**9 = 512
Количество 1 в адресе узла = количество 1 в адресе сети + количество 1 в номере узла (все в двоичной записи).
"""

ans = 0 # количество IP-адресов, в двоичной записи которых ровно 15 единиц
for node in range(512): # Всего сети доступно 512 адресов
    # 10011101.11011100.1011100|0.00000000 адрес сети, в нем 14 единиц
    if 14 + bin(node).count('1') == 15: ans += 1
print(ans) # 9
