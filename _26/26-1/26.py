f = open("Inf2025\\_26\\26-1\\261.txt").readlines()
n, mv = map(int, f[0].split())
a = []
af = []
for i in range(1, len(f)):
    r = int(f[i])
    if 309 < r < 321: af.append(r)
    else: a.append(r)
af.sort()
a.sort()
k, v = 0, 0
while k < len(af) and af[k] + v <= mv:
    v += af[k]
    k += 1
k1 = 0
b = 0
while k1 < len(a) and a[k1] + v <= mv:
    b = 1
    v += a[k1]
    k1 += 1
print(k + k1)

k1 -= 1
kmax = a[k1]
v -= kmax
while a[k1] + v <= mv:
    kmax = a[k1]
    k1 += 1
print(v + kmax)
'''
else:
    k2 = k
    v -= af[k - 1]
    while k2 < len(af) and v + af[k2] <= mv:
        v = v + a[k2 + k1] - a[k2]
        k2 += 1
'''