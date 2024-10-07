
def game(i, j, t):
    if t == 1 and i + j >= 67:
        return False
    if t == 2:
        return max(i, j) + i + j >= 67
    
    t += 1
    return game(i+1, j, t) or game(i, j+1, t) or game(i+j, j, t) or game(i, j+i, t)
        

for i in range(1, 57):
    if game(9, i, 1):
        print(i)
        break 
