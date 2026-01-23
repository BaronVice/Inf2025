
# Все пятибуквенные слова, составленные из букв С, Т, Р, О, К, А, записаны в алфавитном порядке и пронумерованы

i = 0
ans = 0

for a1 in "АКОРСТ":
    for a2 in "АКОРСТ":
        for a3 in "АКОРСТ":
            for a4 in "АКОРСТ":
                for a5 in "АКОРСТ":

                    i += 1
                    word = a1 + a2 + a3 + a4 + a5

                    if (
                        # ... с чётным номером
                        i % 2 == 0
                        # не начинается с букв А, С или Т
                        and (not word.startswith("А")) and (not word.startswith("С")) and (not word.startswith("Т")) 
                        # и при этом содержит в своей записи ровно две буквы О
                        and word.count("О") == 2
                    ):
                        ans = i

print(ans)
                        