
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

# n = 2**i * p1**a1 * ...
# A = 5 (нечетные) = (a1 + 1) * (a2 + 1) * ...
# 1) (a1 + 1) = 5 -> a1 = 4
# n = 2**i * p**4, p - простое число
# 1, p, p**2, p**3, p**4

for n in range(55000000, 60000000):
    p_pow4 = n
    while p_pow4 % 2 == 0:
        p_pow4 //= 2
    
    p = int(p_pow4**0.25)
    if p ** 4 != p_pow4: continue

    if is_prime(p):
        print(n, p**3)