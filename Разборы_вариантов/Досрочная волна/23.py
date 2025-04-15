import functools
from functools import lru_cache

@lru_cache
def F(n, t1, t2):
    if n > 51: return 0
    if n == 51 and t1 == 1 and t2 == 1: return 1
    if n == 35: return 0
    if n == 13: t1 = 1
    if n == 15: t2 = 1

    return F(n + 1, t1, t2) + F(n + 2, t1, t2) + F(n * 2, t1, t2)


print(F(7, 0, 0))
