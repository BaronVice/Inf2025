
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

ans = 10**9
for k1 in range(100):
    for k2 in range(100):
        for k3 in range(100):
            if 2 * k3 + 4 * k2 + 4 * k1 + 3 == 65:
                if is_prime(6 * k1 + 7 * k2 + 4 * k3 + 1):
                    ans = min(ans, 2 * k1 + k2 + 1)
print(ans)