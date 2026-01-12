
def win(n1):
    return (n1-3) <= 11 or (n1-7) <= 11 or (n1//3) <= 11

def game(n1, t):
    if t == 0:
        if win(n1): return False
        s1 = n1-3
        s2 = n1-7
        s3 = n1//3
        if win(s1) and win(s2) and win(s3): return False
    if t == 1:
        if win(n1): return True
    if t == 2:
        if win(n1): return False
    if t == 3:
        if win(n1): return True
        else: return False

    if t % 2 == 0:
        return game(n1-3, t+1) and game(n1-7, t+1) and game(n1//3, t+1)
    else:
        return game(n1-3, t+1) or game(n1-7, t+1) or game(n1//3, t+1)

for s in range(12, 100):
    if game(s, 0):
        print(s)
