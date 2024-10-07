s, n = map(int, input().split())
a = []
for i in range(n):
    r = int(input())
    a.append(r)
a.sort()
to = 0
k = 0
ded = n-1
for i in range(n):
    if to + a[i] <= s:
        k += 1
        to += a[i]
    else:
        to -= a[i-1]
        ded = i-1
        break
print(k)
ans = a[ded]
for i in range(ded, n):
    if a[i] + to <= s: ans = a[i]
    else: break
print(ans)