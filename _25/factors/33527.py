# https://inf-ege.sdamgia.ru/problem?id=33527
"""
Найдите все натуральные числа, принадлежащие отрезку [101000000; 102000000],
у которых ровно три различных чётных делителя (при этом количество нечётных делителей может быть любым).

В ответе перечислите найденные числа в порядке возрастания.
"""

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

# n = 2**a1 * p2**a2 * ... * pk**ak
# A = a1 * (a2+1) * ... * (ak + 1)
# Три различных четных делителя возможны при:
# 1) a1 = 3 (n = 2**3 < 101000000 -> такой вариант не подойдет)
# 2) a1 = 1, a2 = 2
# Тогда рассматриваем n вида
# n = 2 * p**2, где p - простое число
for n in range(101000000, 102000000+1):
    if n % 2 == 1: continue

    p_pow2 = n // 2
    p = int(p_pow2 ** 0.5)
    if p**2 == p_pow2 and is_prime(p):
        print(n)