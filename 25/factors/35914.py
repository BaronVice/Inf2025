
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

for i in range(40000000, 50000000 + 1):
    n = i
    while n % 2 == 0:
        n //= 2

    p4 = n
    p = int(p4**0.25)
    if p**4 == p4 and is_prime(int(p)):
        print(i)

