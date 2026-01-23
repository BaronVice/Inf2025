f = open("Inf2025\\Разборы_вариантов\\Демо\\26\\demo_2025_26.txt").readlines()
n = int(f[0])
sd = []
sbs = []
sb_arid = {}
t2 = []
c2 = []
for i in range(n):
    line = f[i + 1].split()
    ids = int(line[0])
    ocenk = [int(line[i]) for i in range(1, 5)]
    if min(ocenk) > 2:
        sd.append(ids)
        sb = sum(ocenk) / 4
        if sbs.count(sb) == 0: sbs.append(sb)
        if sb not in sb_arid.keys(): sb_arid[sb] = []
        sb_arid[sb].append(ids)
    else:
        if ocenk.count(2) == 3: t2.append(ids)
        else: c2.append(ids)
laststip = n // 4
k = 0
sbs.sort(reverse = -1)
for b in sbs:
    a = sb_arid[b]
    if 52326 in a: print(1)
    if k + len(a) >= laststip:
        a.sort()
        print(a[laststip - k - 1])
        break
    k += len(a)
t2.sort()
c2.sort()
if len(t2) > 0: print(t2[0])
else: print(c2[0])
