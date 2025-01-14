f = open("D:\\vscode\\Inf2025\\Inf2025\\17\\17.txt").readlines()
a = [0] * len(f)
k = 30000
ans1, ans2 = 0, 0
for i in range(len(a)):
    if int(f[i]) % 10 == 5 and len(f[i]) == 3: k = min(k, int(f[i]))
    a[i] = int(f[i])
for i in range(1, len(a)):
    f1 = (a[i] > 999 and a[i] < 10000) and (a[i - 1] > 9999 or a[i - 1] < 1000)
    f2 = (a[i - 1] > 999 and a[i - 1] < 10000) and (a[i] > 9999 or a[i] < 1000)
    if (f1 or f2) and (a[i]*a[i]+a[i-1]*a[i-1]) % k == 0:
        ans1 += 1
        ans2 = max(ans2, a[i]*a[i] + a[i - 1]*a[i - 1])
print(k) # 85, но должно быть трехзначное
print(ans1, ans2)
