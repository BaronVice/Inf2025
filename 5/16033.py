
ans = 1000000000000
for n in range(1, 100000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += "01"
    else:
        bin_n += "10"

    r = int(bin_n, 2)
    if r > 102 and r < ans:
        ans = r

print(ans)
    