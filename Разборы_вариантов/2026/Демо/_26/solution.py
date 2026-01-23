
lines = open("Путь\\до\\файла.txt").readlines()[1:]

nums = []

for i in range(len(lines)):
    num1, num2 = map(int, lines[i].split())
    # +1 потому что счет продуктов начинается с 1, i начинается с 0
    nums.append([num1, 1, i+1])
    nums.append([num2, 2, i+1])

nums.sort()

first = []
last = []
visited = set()
# последний продукт, для которого будет определено его место в рейтинге...
last_product = -1
for num in nums:
    date_type = num[1]
    product_id = num[2]

    if product_id in visited: continue
    else: visited.add(product_id)

    # ...это последний продукт при распределении в рейтинг
    last_product = product_id
    if date_type == 1:
        first.append(product_id)
    else:
        last.append(product_id)

print(last_product) # 564

last.reverse()
rating = first + last
for i in range(len(rating)):
    if rating[i] == last_product:
        # - 1 т.к. без учета последнего продукта
        print(len(rating) - i - 1) # 444
