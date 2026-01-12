
s = open('Inf2025\\_24\\24_17563.txt').read()
s = s.replace('-*', '@')
s = s.replace('--', '@')
s = s.replace('*-', '@')
s = s.replace('**', '@')
for i in "789":
    s = s.replace('-0'+i, '-0@'+i)
    s = s.replace('*0'+i, '*0@'+i)
    s = s.replace(i+'0', i+'^')
while '^0' in s: s = s.replace('^0', '^^')
while '00' in s: s = s.replace('00', '0')

s = s.replace('^', '0')
ans = 0
for i in s.split('@'):
    if len(i) > ans:
        ans = len(i)
        print(i)
print(ans)
    
        