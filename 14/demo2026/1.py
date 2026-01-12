
x = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561

digits = []
while x != 0:
    digits.append(x % 27)
    x //= 27
digits.reverse()

ans = 0
for digit in digits:
    if digit > 9:
        ans += 1
print(ans)