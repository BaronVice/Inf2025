
m = 0
for x in range(0, 100):
    for y in range(0, 100):
        for z in range(0, 100):
            for w in range(0, 100):
                if 2 * x + w == 2 * y + z and 47 == y + 2 * z and 70 > x + 2 * w:
                    m = max(x + 2 * w, m)
print(m)
