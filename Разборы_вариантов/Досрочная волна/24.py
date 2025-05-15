s = open("24.txt").read()
i = 0
alp = "0123456789AB"
c = "02468A"
ans = 0
while i < len(s):
    while i < len(s) and (s[i] not in alp or s[i] == '0'):
        i += 1
    
    t = 1
    while i < len(s) and s[i] in alp:
        if s[i] in c:
            ans = max(ans, t+1)
        if s[i] == '0': t -= 1
        i += 1
    i += 1
print(ans)
