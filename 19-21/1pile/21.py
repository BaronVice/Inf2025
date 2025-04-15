def win1(n1,n2):
    return (n1 * 2 + n2) >= 47 or (n1 + 2 + n2 + 1) >= 47 or (n1 + 1 + n2 + 2) >= 47 or (n1 + n2 * 2) >= 47

def game(n1, n2, t):
    if t == 0:
        if win1(n1,n2):
            return False
        if win1(n1, n2 * 2) and win1(n1 + 1, n2 + 2) and win1(n1 + 2, n2 + 1) and win1(n1 * 2 , n2): return False
    if t == 1:
        if win1(n1,n2):
            return True
    if t == 2:
        if win1(n1,n2):
            return False
    if t == 3:
        if win1(n1,n2):
            return True
        else: return False
        
    if t % 2 == 0:
        return game(n1 * 2, n2, t + 1) and game(n1 + 2, n2 + 1, t + 1) and game(n1 + 1, n2 + 2, t + 1) and game(n1,  n2 * 2,t + 1 ) 
    else:
        return game(n1 * 2, n2, t + 1) or game(n1 + 2, n2 + 1, t + 1) or game(n1 + 1, n2 + 2, t + 1) or game(n1,  n2 * 2,t + 1 )


for s in range(1, 36):
    if game(10, s, 0):
        print(s)
