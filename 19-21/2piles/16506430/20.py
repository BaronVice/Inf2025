
def c(i,j):
    return max(i,j)+i+j >= 67

def f(i, j, t):
    if t == 1 and c(i+1, j) and c(i, j+1) and c(i+j, j) and c(i, i+j): return False
    if t in [2,4] and (max(i, j)+i+j) >= 67: return True
    if t in [1,3] and (max(i, j)+i+j) >= 67: return False
    if t == 5: return 0
    if t % 2 == 0: return f(i+1, j, t+1) or f(i, j+1, t+1) or f(i+j, j, t+1)or f(i, i+j, t+1)
    t += 1
    return f(i+1, j, t) and f(i, j+1, t) and f(i+j, j, t) and f(i, i+j, t)

for i in range(1, 58):
    if f(i, 9, 1) == 1: print(i)