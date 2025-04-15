# https://inf-ege.sdamgia.ru/problem?id=63066

a = open("Inf2025\\17\\63066.txt").readlines()
mx = 0
for i in range(len(a)):
    a[i] = int(a[i])
    if a[i] % 1000 == 321: mx = max(mx, a[i])
print(mx)

ans1, ans2 = 0, 0
for i in range(2, len(a)):
    f2 = a[i] % 5 == 0 or a[i - 1] % 5 == 0 or a[i - 2] % 5 == 0
    t = [a[i], a[i - 1], a[i - 2]]
    f3 = sum(t) > mx
    f1 = [len(str(t[0])), len(str(t[1])), len(str(t[2]))].count(5) == 2
    if f1 * f2 * f3 == 1:
        ans1 += 1
        ans2 = max(ans2, sum(t))
print(ans1, ans2)
