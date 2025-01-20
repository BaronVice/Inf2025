s = open("Inf2025\\Разборы_вариантов\\Демо\\24\\demo_2025_24.txt", encoding="UTF8").read()
k = 1
ans = 0
a = ""
b = ""
for i in range(1, len(s)):
    a += s[i-1]
    w = s[i - 1] + s[i]
    if w == "-*" or w == "*-" or w =="--" or w =="**" or (s[i-1] in "*-" and s[i] == '0' and i < len(s) and s[i+1] in '06789'):
        ans = max(ans, k)
        if k == 156: b = a
        a = ""
        k = 1
    else: 
        k += 1
ans = max(ans, k)
print(ans)
print(b)
