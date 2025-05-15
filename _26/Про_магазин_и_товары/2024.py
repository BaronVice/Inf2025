# https://inf-ege.sdamgia.ru/problem?id=59851

f = open("Inf2025\\_26\\Про_магазин_и_товары\\2024.txt").readlines()
n = int(f[0])
a = [0] * n
for i in range(n): a[i] = int(f[i + 1])
a.sort()
print(sum(a[:(n - (n // 3))]))
a.sort(reverse = 1)
s = 0
for i in range(2, n, 3): s += a[i]
print(sum(a) - s)

