import sys
sys.setrecursionlimit(10**9)

def F(n):
    if n == 1:
        return 0 
    if n == 0:
        return 1
    if n > 1 and n % 2 == 0:
        return F(n // 2) + 1
    if n > 1 and n % 2 != 0:
        return F(n // 2)
        
for n in range (1, 10000 + 1):
    if F(n) == 10:
        print(n)
        break
