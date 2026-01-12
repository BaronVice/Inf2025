f = open("Inf2025\\_26\\Система_наблюдения\\26_9847.txt").readlines()
ans1, ans2 = 0, 0
k = 0
lk = -1
n = int(f[0])
arr = [0] * 1441
voshol = {}
vishel = {}
for i in range(1, n + 1):
    s, e = map(int, f[i].split())
    if s not in voshol.keys(): voshol[s] = 0
    if e not in vishel.keys(): vishel[e] = 0
    voshol[s] += 1
    vishel[e] += 1
    for i in range(s,e):
        arr[i] += 1
print(max(arr))

for t in range(1440):
    if t in voshol.keys(): k += voshol[t]
    
    if k == ans2 and k > lk:
        ans1 += 1
    elif k > ans2:
        ans1 = 1
        ans2 = k
    if t in vishel.keys(): k -= vishel[t]
    lk = k
print(ans1, ans2)