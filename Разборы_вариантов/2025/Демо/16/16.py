"""
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1 при n = 1;
F(n) = (n - 1) * F(n - 1), если n > 1.

Чему равно значение выражения (F(2024) + 2 * F(2023)) / F(2022)?
"""

# Перепишем как есть (и поймаем RecursionError: maximum recursion depth exceeded -> расширяем лимит рекурсии)
from sys import setrecursionlimit
setrecursionlimit(10**9)

def f(n):
    if n == 1: return 1
    if n > 1: return (n - 1) * f(n - 1)

print((f(2024) + 2 * f(2023)) / f(2022)) # 4094550
