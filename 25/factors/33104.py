# https://inf-ege.sdamgia.ru/problem?id=33104
"""
Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
Например, у числа 6 есть два нетривиальных делителя: 2 и 3. Найдите все натуральные числа,
принадлежащие отрезку [289123456; 389123456] и имеющие ровно три нетривиальных делителя.

Для каждого найденного числа запишите в ответе его наибольший нетривиальный делитель.
Ответы расположите в порядке возрастания.

Например, в диапазоне [5; 16] ровно три различных натуральных делителя имеет число 16,
поэтому для этого диапазона вывод на экране должна содержать следующие значения: 16 8
"""

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

# Количество делителей A = 3 (нетривиальные делители) + 2 (1 и n) = 5
#
# n = p1**a1 * p2**a2 * ... * pk**ak
# A = 5 = (a1 + 1) * (a2 + 1) * ... * (ak + 1)
# A = 5 только если один из множителей 5, а остальные 1,
# Тогда рассматриваем n вида
# n = p**4, где p - простое число

print("Решение 1")
for n in range(289123456, 389123456+1):
    p4 = n
    p = int(p4**0.25)
    # Проверим, что корень - целое число и простое число
    if p**4 == p4 and is_prime(int(p)):
        # Делители i: 1 < p < p**2 < p**3 < p**4 (p**4 = i)
        # Поскольку в задании просят наибольший делитель
        #  отличный от самого числа, то выводим p**3
        print(n, p**3)

# Альтернативное решение: переберем все простые числа p от 1 до 1000 (1000 хватит поскольку 1000**4 > 389123456),
# проверяя, что 289123456 <= p**4 <= 389123456
print("Решение 2")
for p in range(1, 1000):
    if is_prime(p) and 289123456 <= p**4 <= 389123456:
        print(p**4, p**3)