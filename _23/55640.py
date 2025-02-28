

def F(n, a):
    if n == 24:
        return 1
    if n > 24:
        return 0
    
    if a == 0:
        return F(n + 1, 1) + F(n + 2, 1) + F(n * 2, 2) + F(n * 3, 2)
    if a == 1:
        return F(n * 2, 2) + F(n * 3, 2)
    if a == 2:
        return F(n + 1, 1) + F(n + 2, 1)


print(F(1, 0))