"""
На числовой прямой даны два отрезка: P=[15;40] и Q=[21;63].
Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение

(x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))

истинно (т.е. принимает значение 1) при любом значении переменной х.
"""

ans = 10**9
for a1 in range(0, 500):
    for a2 in range(a1, 500):
        if all(
            [
                (15 <= x <= 40) <= (((21 <= x <= 63) and (not(a1 <= x <= a2))) <= (not(15 <= x <= 40)))
                for x in range(1, 1000)
            ]
        ):
            ans = min(ans, a2-a1)
print(ans)