

s = open("Inf2025\\_24\\24_21597.txt").read()
i = 0
b = 0
mx_len = 0
alp = "012345"
while i < len(s):
    while (i < len(s) and s[i] not in alp) or (s[i] == '0' and i < len(s)-1 and s[i+1] in alp): i += 1

    ans = 0
    while i < len(s) and s[i] in alp:
        ans += 1 
        i += 1
    if s[i] in '-*' and i < len(s)-1 and s[i+1] in alp:
        ans += 1
        i += 1
    else:
        mx_len = max(mx_len, ans)
    
        