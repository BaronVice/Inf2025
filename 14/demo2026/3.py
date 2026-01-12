

for x in range(3000, 0, -1):
    res =  9 * 11**210 + 8 * 11**150 - x
    digits = []
    while res != 0:
        digits.append(res % 11)
        res //= 11
    
    if digits.count(0) == 60:
        print(x)
        break
