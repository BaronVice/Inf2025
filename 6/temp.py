a = open("17.txt").readlines()
mx = 456320
for i in range(len(a)):
    a[i] = int(a[i])
    if abs(a[i]) % 10 == 7: mx = min(mx, a[i])
mx *= mx
ans1, ans2 = 0, -200000
for i in range(1, len(a)):
    if abs(a[i - 1]) % 10 == abs(a[i]) % 10:
        if (a[i] % 7 == 0 and a[i - 1] % 7 != 0) or (a[i - 1] % 7 == 0 and a[i] % 7 != 0):
            if a[i] + a[i - 1] <= mx:
                ans1 += 1
                ans2 = max(ans2, a[i] + a[i - 1])
print(ans1, ans2)
