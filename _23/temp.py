

def f(n, a):
    if n == 1 and a == True:
        return 1
    if n < 1:
        return 0
    if n == 8:
        a = True

    return f(n - 2, a) + f(n // 2, a)


print(f(32, False))