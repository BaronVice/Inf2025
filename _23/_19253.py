# 19253 здесь https://kompege.ru/task

def F(n, used19, used29):
    if n == 6 and used19 and used29:
        return 1
    if n == 29:
        used29 = 1
    if n == 19:
        used19 = 1
    if n == 24:
        return 0
    if n < 6:
        return 0
    
    return F(n - 1, used19, used29) + F(n - 6, used19, used29) + F(n // 2, used19, used29)


print(F(34, 0, 0))