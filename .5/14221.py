

for n in range(100, 1000):
    s = str(n)
    d1 = int(s[0])
    d2 = int(s[1])
    d3 = int(s[2])

    s1 = d1 + d2
    s2 = d2 + d3
    minn = str(min(s1, s2))
    maxx = str(max(s1, s2))

    r = int(minn + maxx)
    if r == 714:
        print(n)
        break
