import sys
sys.setrecursionlimit(10**9)

def F(n,a,b):
    if n == 6 and a == 1 and b == 1:
        return 1
    if n < 6:
        return 0
    if n == 19:
        a = 1
    if n == 29:
        b = 1
    if n == 24:
        return 0


    return (F(n - 1,a,b) + F(n - 6,a,b) + F(n // 2,a,b))


print (F(34,0,0)) 