def f(i, j, t):
    #if t == 1 and k >= 22: return 0
    if t == 3 and (i+j) > 87: return 1
    if t == 3 or (i+j) > 87: return 0
    if t % 2 == 1: return f(i+1, j, t+1) or f(i, j+1, t+1) or f(i*3, j, t+1) or f(i, 3*j, t+1)
    t += 1
    return f(i+1, j, t) or f(i, j+1, t) or f(i*3, j, t) or f(i, 3*j, t)

for i in range(1, 72):
    if f(i, 6, 1) == 1: print(i)