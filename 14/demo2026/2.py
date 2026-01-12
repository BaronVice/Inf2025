
# import string

# print(help(string))


for x in "0123456789abcdefghijklmnopqrs":
    result = int("923"+x+"874", 29) + int("524"+x+"6152", 29)
    if result % 28 == 0:
        print(result // 28)

