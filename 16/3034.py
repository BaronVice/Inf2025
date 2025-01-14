
ans = [0]
def f(n, even):
    if n > 1_000_000_000: return
    
    if even == 3: ans[0] += 1
    
    f(n*2 + 1, even)
    if even != 3:
        f(n * 2, even + 1)

f(1, 0)
print(ans[0])