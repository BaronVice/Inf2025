# https://inf-ege.sdamgia.ru/problem?id=69893

"""
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».

Для какого наименьшего натурального числа А формула

(ДЕЛ(x, 2) → ¬ДЕЛ(x, 5)) ∨ (x + A ≥ 70)
тождественно истинна (т.е. принимает значение 1) при любом целом положительном значении переменной х?
"""

def d(n,m):
    return n % m == 0

for a in range(1,1000):
    if all(
        [
            (d(x,2) <= (not d(x,5))) or (x + a >= 70)
            for x in range(1, 1000)
        ]
    ):
        print(a)
        break