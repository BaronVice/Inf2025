

n = 0
a = 1_125_000
while n != 6:
    a += 1
    got_div = False
    for div in range(17, a//2 , 10):
        if a % div == 0:
            got_div = True
            break
    if got_div:
        print(a, div)
        n += 1