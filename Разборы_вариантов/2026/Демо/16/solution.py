
"""
Алгоритм вычисления функций F(n) и G(n), где n – целое число, задан следующими соотношениями:
F(n) = 2 * (G(n - 3) + 8);
G(n) = 2 * n, если n < 10;
G(n) = G(n - 2) + 1, если n ≥ 10.
Чему равно значение выражения F(15548)?
"""

from sys import setrecursionlimit
setrecursionlimit(10**9)

def f(n):
    return 2 * (g(n - 3) + 8)

def g(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return g(n - 2) + 1
    
print(f(15548))
