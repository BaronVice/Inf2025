s = open("Inf2025\\_24\\24.txt").read()

s_max = 0
s_cur = 0
i = 0
while i != len(s):
    while i != len(s) and s[i] in ['*', '+', '0']:
        i += 1
    s_cur = 0
    while i != len(s):
        while i != len(s) and s[i] not in ['*', '+']:
            i += 1
        s_cur += 1
        if i == len(s):
            s_max = max(s_max, s_cur)
            break

        if s[i+1] not in ['*', '+', '0']:
            i += 1
        else:
            s_max = max(s_max, s_cur)
            break
        
print(s_max)
