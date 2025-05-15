
def win(n1,n2):
    return ((n1 * 2) + n2 >= 227) or  (n1 + (n2 * 2)  >= 227) or  ((n1 + 1) + n2 >= 227) or (n1 + (n2 + 1 )  >= 227)

def game(n1,n2,t):
    if t == 0:
        if win(n1,n2):
            return False
    if t == 1:
        if win(n1,n2):
            return True
        else: return False

    if t % 2 == 0:
        return   game(n1 * 2 ,n2, t + 1  ) or  game(n1, n2 * 2 , t + 1) or  game(n1 + 1 , n2, t + 1) or game(n1 , n2 + 1 ,  t + 1)
    else:
        return  game(n1 * 2 ,n2, t + 1  ) or  game(n1, n2 * 2 , t + 1) or  game(n1 + 1 , n2, t + 1) or (n1 , n2 + 1 ,  t + 1)

for s in range(1, 209 + 1):
    if game(17,s,0):
        print(s)