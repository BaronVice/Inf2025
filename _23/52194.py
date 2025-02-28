

def F(n, a1, a2):
    if n == 16:
        return 1
    if n > 16:
        return 0
    
    if a1 < 2 and a2 < 2:
        return F(n + 1, a1 + 1, 0) + F(n * 2, 0, a2 + 1)
    if a1 < 2:
        return F(n + 1, a1 + 1, 0)
    if a2 < 2:
        return F(n * 2, 0, a2 + 1)

print(F(1, 0, 0))
