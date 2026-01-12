
words = [""]

for i1 in "агинрт":
    for i2 in "агинрт":
        for i3 in "агинрт":
            for i4 in "агинрт":
                for i5 in "агинрт":
                    for i6 in "агинрт":
                        words.append(i1 + i2 + i3 + i4 + i5 + i6)

for i in range(1, len(words), 2):
    word = words[i]
    if word.startswith("а") or word.startswith("и") or word.startswith("г"):
        continue
    if word.count("а") == 1:
        print(i)
        break

