"""
На числовой прямой даны два отрезка: P  =  [15; 40] и Q  =  [21; 63].
Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение

(x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))

истинно (т.е. принимает значение 1) при любом значении переменной х.
"""

ans = 1000
for i in range(100):
    for j in range(i+1, 100):
        fl = True
        for x in range(100):
            if not ( (15 <= x <= 40) <= (((21 <= x <= 63) and (not (i <= x <= j))) <= (not(15 <= x <= 40))) ):
                fl = False
        if fl:
            ans = min(ans, j - i + 1)
print(ans)



