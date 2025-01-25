
ans = 1000000000000
for n in range(1, 100000):
    bin_n = bin(n)[2:]
    summ = bin_n.count('1') % 2
    bin_n += str(summ)
    
    summ = bin_n.count('1') % 2
    bin_n += str(summ)

    r = int(bin_n, 2)
    if r > 123 and r < ans:
        ans = r
        
print(ans)