# https://inf-ege.sdamgia.ru/problem?id=47219

"""
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».

Для какого наименьшего натурального числа А формула
(ДЕЛ(x, 2) → ¬ДЕЛ(x, 3)) ∨ (x + A ≥ 100)
тождественно истинна (то есть принимает значение 1) при любом натуральном значении переменной х?
"""

def d(n,m):
    return n % m == 0

for a in range(1000):
    if all(
        [
            (d(x,2) <= (not d(x,3))) or (x + a >= 100)
            for x in range(1, 1000)
        ]
    ):
        print(a)
        break