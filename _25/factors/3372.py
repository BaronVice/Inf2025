def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# C = 6
# A = 5
# 1, 2, 2*p, 2*p**2, p, p**2
# 1) a1 = 1, a2 = 2
# 2) a1 = 4
for p in range(2, 1000):
    if f(p) and 289123456 <= p**4 <= 389123456:
        print(p**4, p**3)