def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

for i in range(101000000, 102000000+1):
    if i % 2 == 1: continue

    p2 = i // 2
    p = int(p2 ** 0.5)
    if p**2 == p2 and is_prime(p):
        print(i)