# https://inf-ege.sdamgia.ru/problem?id=48464

ans = 0
fn = 0
for n in range(1, 1_542_613_234 + 1):
    fn = (fn + n)
    if 765_432_010 <= n <= 1_542_613_234:
        if fn % 3 != 0: ans += 1

print(ans)

# for n in range(765_432_010, 1_542_613_234 + 1):
#     fn = (fn + n) % 3
#     if fn != 0: answer += 1

# print(answer)
# 259_060_409
