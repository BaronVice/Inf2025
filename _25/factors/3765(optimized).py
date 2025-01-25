"""
Пусть N(b) = 1 850 000 000 + b, где b – натуральное число.
Найдите пять наименьших значений b, при которых N(b) имеет нечётное
количество различных чётных делителей.
В ответе запишите найденные значения b в порядке возрастания,
справа от каждого значения запишите число чётных делителей N(b).
"""

# Натуральное число - целое и больше 0 (1, 2, 3, 4, 5, ...)

# Эту задачу можно решить разными способами, я приведу решение через ОТА.
# n имеет нечетное количество четных делителей, если A % 2 == 1, где
# n = 2**a1 * p2**a2 * ... * pk**ak (p2..pk - простые числа)
# A = a1 * (a2 + 1) * ... * (ak + 1)

# Упростим задачу, убрав на некоторое время b:
# - Найти первые 5 чисел n > 1 850 000 000,
# у которых нечётное количество различных чётных делителей

# Какой максимальный простой делитель может быть у числа n?
# Ответ: sqrt(n). Все, что больше - составные делители

# * Для небольшой оптимизации заметим следующее:
# У нечетных чисел 0 четных делителей, 0 - четное число -> нечетные не рассматриваем

# Я думаю, что хватит простых чисел до sqrt(2_000_000_000) = 44722

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primes_list = []
erathosphenus = [0 for i in range(100_000_000)]
erathosphenus[0] = 1,
erathosphenus[1] = 1

for i in range(100_000_000):
    if erathosphenus[i] == 0:
        primes_list.append(i)
        for j in range(i, 100_000_000, i):
            erathosphenus[j] += 1

print(len(primes_list))
max_prime = max(primes_list)
primes_set = set(primes_list)
print(max_prime)

i = 0
num = 1850000000
while i != 5:
    a1 = 0
    a2_to_ak = []

    n = num
    A = 1
    while n % 2 == 0:
        n //= 2
        a1 += 1
        if n > 2 and (n in primes_set or (n > max_prime and is_prime(n))): A *= 2
    
    A *= a1
    for prime in primes_list:
        if prime**2 > n: break
        if n % prime != 0: continue

        a = 0
        while n % prime == 0:
            n //= prime
            a += 1
            if n > prime and (n in primes_set or (n > max_prime and is_prime(n))): A *= 2

        a2_to_ak.append(a)

    for a in a2_to_ak: A *= (1 + a)
    if A % 2 == 1:
        print(num-1_850_000_000, A)
        i += 1

    num += 2

