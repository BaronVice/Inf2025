import sys
sys.setrecursionlimit(10**9)

def F(n):
    if n == 20:
        return 1
    elif n > 20:
        return 0
    
    if n == 0:
        return F(n + 3)
    elif n == 1:
        return F(n + 3) + F(n * 2)
    elif n < 0:
        return F(n + 3) + F(n ** 2)
    else:
        return F(n + 3) + F(n * 2) + F(n ** 2)

s = 0
for i in range(-20, 20 + 1):
    s += F(i)
print(s)
