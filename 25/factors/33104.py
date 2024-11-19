def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

for i in range(289123456, 389123456+1):
    p4 = i
    p = int(p4**0.25)
    if p**4 == p4 and is_prime(int(p)):
        # Делители i: 1 < p < p**2 < p**3 < p**4 (p**4 = i)
        # Поскольку в задании просят наибольший делитель
        #  отличный от самого числа, то выводим p**3
        print(i, p**3)