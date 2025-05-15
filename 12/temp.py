
otvet = 0

for n in range(4, 1000):
    s = '4' + '7' * n

    while '444' in s or  '777' is s:
        if '777' in s:
            s = s.replace ('777', '4', 1)
        else: 
            s = s.replace ('444', '7', 1)

    

print(n)