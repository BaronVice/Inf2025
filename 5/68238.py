for n in range(100, 1000000):
    s = str(n)

    minn = 1000000
    maxx = -1
    for i in range(1, len(s)-1):
        num = int(s[i-1] + s[i] + s[i+1])
        minn = min(minn, num)
        maxx = max(maxx, num)

    r = maxx - minn
    if r == 415:
        print(n)
        break
