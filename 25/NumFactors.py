# Ищем делители числа n
def findFactors(n) :
    # Делители числа
    factors = []

    a = 2
    # До корня числа
    while a * a <= n:
        # Если делится
        if (n % a == 0):
            # Если у числа n есть делитель a < sqrt(n), то у n есть делитель b > sqrt(n), причем n // a = b
            if (n // a == a):
                # Здесь особый случай: если корень числа делитель, то добавляем его только один раз (чтобы не добавлять sqrt(n) дважды)
                factors.append(a)
            else:
                factors.append(a)
                factors.append(n//a)
        a += 1
    # Внимательно смотрим задание - если 1 и/или n считаются делителями, то их тоже надо добавить
    # divisors.append(1)
    # divisors.append(n)

    return factors

print(
  sorted(findFactors(100)) # Можно еще посортировать
) # -> [2, 4, 5, 10, 20, 25, 50]
