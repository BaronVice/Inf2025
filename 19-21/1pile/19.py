from sys import setrecursionlimit

setrecursionlimit(10**8)

v = dict()
def game(n,t):
    if n in v:
        return v[n]

    if t == 0:
        if n * 2 >= 333:
            v[n] = False
            return False
    if t == 1:
        if n * 2 >= 333:
            v[n] = True
            return True
        else:
            v[n] = False
            return False
    
    if t % 2 == 0:
        res = game(n + 3, t + 1) and game(n + 8, t + 1) and game(n * 2, t + 1)
        v[n] = res
        return res
    else:
        res = game(n + 3, t + 1) or game(n + 8, t + 1) or game(n * 2, t + 1)
        v[n] = res
        return res


for s in range(1, 332 + 1):
    if game(s, 0):
        print(s)