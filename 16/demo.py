from sys import setrecursionlimit

setrecursionlimit(10**9)

# TODO: lru_cache cannot be used with setrecursionlimit
def F(n):
    # Теперь распишем, что при значении n функция будет возвращать
    # F(n) = 1 при n = 1:
    if n == 1:
        return 1
    # F(n) = (n – 1) x F(n - 1), если n > 1
    if n > 1:
        return (n - 1) * F(n - 1)

# Чему равно значение выражения (F(2024) + 2 x F(2023)) / F(2022)
print( (F(2024) + 2 * F(2023)) / F(2022) )