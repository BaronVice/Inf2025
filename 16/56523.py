

def f(n, is_used):
    if n == 11 and is_used: return 1
    if n > 11: return 0

    s = f(n + 1, is_used) + f(n + 2, is_used)
    if not is_used:
        is_used = True
        s += f(n * 2, is_used) + f(n * 3, is_used)

    return s

print(f(1, False))