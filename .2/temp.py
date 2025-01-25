for i11 in [0, 1]:
    for i12 in [0, 1]:
        for i13 in [0, 1]:
            for i21 in [0, 1]:
                for i23 in [0, 1]:
                    for i31 in [0, 1]:
                        for i32 in [0, 1]:
                            t = (
                                (1, 0, i11, 0, 1),
                                (1, 0, i21, i23, 0),
                                (i31, 1, 1, i32, 0),
                            )
                            if len({t[0], t[1], t[2]}) == 3:
                                for x in range(4):
                                    for y in range(4):
                                        for z in range(4):
                                            for w in range(4):
                                                if len({x, y, z, w}) == 4:
                                                    if all([
                                                        (((row[w] <= row[y]) <= row[x]) == row[-1])
                                                        for row in t
                                                    ]):
                                                        print(f"wxyz: {w+1}{x+1}{y+1}{z+1}")