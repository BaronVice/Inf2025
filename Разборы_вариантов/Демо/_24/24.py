s = open("Inf2025\\Разборы_вариантов\\Демо\\24\\demo_2025_24.txt", encoding="UTF8").read()
k = 1
ans = 0
a = ""
b = ""
i = 1

while s[i-1] == '-' or s[i-1] == '*':
    i += 1

while i < len(s):
    a += s[i-1]
    w = s[i - 1] + s[i]
    if w == "-*" or w == "*-" or w =="--" or w =="**" or (s[i-1] in "*-" and s[i] == '0' and i < len(s) and s[i+1] in '06789'):
        if len(a) and (a[-1] == '-' or a[-1] == '*'): k -= 1
        ans = max(ans, k)
        a = ""
        k = 1
        i += 1
        while (s[i-1] == '-' or s[i-1] == '*') and i < len(s):
            i += 1
    else:
        k += 1
        i += 1

print(ans)
