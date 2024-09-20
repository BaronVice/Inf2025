# https://inf-ege.sdamgia.ru/problem?id=46983

# https://github.com/BaronVice/Inf2025/blob/main/25/NumFactors.py
def findFactors(n) :
    factors = []

    a = 2
    while a * a <= n:
        if (n % a == 0):
            if (n // a == a):
                factors.append(a)
            else:
                factors.append(a)
                factors.append(n//a)
        a += 1

    return factors


num = 460000000
i = 0

while i != 5:
    num += 1
    factors = findFactors(num)
    if len(factors) >= 5:
        i += 1
        # !!! ВАЖНО !!!
        # Смотрим задание - "вывести пятый по ВЕЛИЧИНЕ делитель"
        # findFactors вернет делители не по возрастанию -> нужна сортировка делителей
        factors.sort(reverse=True)
        print(factors[4])
"""
Ответ:
41818182
261959
5
271
57500001
"""
