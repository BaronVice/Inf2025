def F(n, used):
    if n == 20:
        return 1
    if n > 21:
        return 0
    
    return F(n * 2, False) + F(n * 3, False) + (0 if used else F(n - 1, True))

print(F(3, False))