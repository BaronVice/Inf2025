def count_zeros_in_ternary(n):
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary.count('0')

max_x = 2030
result_x = 0

for x in range(max_x, 0, -1):
    if count_zeros_in_ternary(3**100 - x) == 5:
        result_x = x
        break

print(result_x)
