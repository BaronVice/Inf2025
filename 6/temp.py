from functools import *
from sys import setrecursionlimit

setrecursionlimit(10**6)

@lru_cache
def f(if12, if25, el):
    if el == 12:
        if12 = True
    if el == 25:
        if25 = True
    if el > 40:
        return 0
    if el == 40 and if12 and if25:
        return 1

    return f(if12, if25, el+1) + f(if12, if25, el*2)



print(f(0, 0, 1))
