

def win(n1, n2):
    return (n1+1) >= 65 or (n1*3) >= 65 or (n2+1) >= 65 or (n2*3) >= 65

def game(n1, n2, t):
    if t == 0:
        if win(n1, n2): return False
    if t == 1:
        if win(n1, n2): return True
        else: return False

    t += 1
    if t % 2 == 0: # Петя
        return game(n1+1, n2, t) or game(n1*3, n2, t) or game(n1, n2+1, t) or game(n1, n2*3, t)
    else: # Ваня
        return game(n1+1, n2, t) or game(n1*3, n2, t) or game(n1, n2+1, t) or game(n1, n2*3, t)

for s in range(1, 59):
    if game(6, s, 0):
        print(s)
        break
