from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**9)

@lru_cache(maxsize=None)
def f(i, j, t):
    #if t == 1 and (max(i,j)*3+min(i,j)) >= 88: return 0
    if t % 2 == 1 and (i+j) > 87: return 1
    if (i+j) > 87: return 0
    if t % 2 == 0:
        t+=1
        return f(i+1, j, t) or f(i, j+1, t) or f(i*3, j, t) or f(i, 3*j, t)
    t+=1
    return f(i+1, j, t) and f(i, j+1, t) and f(i*3, j, t) and f(i, 3*j, t)

for i in range(71, 0, -1):
    if f(i, 6, 1) == 1: print(i)
print(-1)