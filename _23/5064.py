

def F(n):
    if n == 13:
        return 1
    if n > 13:
        return 0
    
    if n % 2 == 0:
        return F(n - 3) + F(n // 2)
    else:
        return F(n - 3) + F(n - 5)


print(F(1))