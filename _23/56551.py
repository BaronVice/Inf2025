

def F(n, a):
    if n == 10 and a == 1:
        return 1
    if n > 10:
        return 0
    
    if a == 1:
        return F(n + 1, a) + F(n + 2, a)
    if a == 0:
        return F(n + 1, a) + F(n + 2, a) + F(n * 2, 1) + F(n * 3, 1)

print(F(1, 0))
