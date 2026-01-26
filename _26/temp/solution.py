

f = open("_26\\temp\\DEMO_26.txt").readlines()

n = int(f[0])

sorted_list = []
for i in range(n):
    n1, n2 = map(int, f[i + 1].split())
    sorted_list.append([n1, 1, i+1])
    sorted_list.append([n2, 2, i+1])

sorted_list.sort()

visited_products = set()
rating_start = 0
rating_last = 0

last_product = -1
last_product_type = -1
for product in sorted_list:
    n = product[0]
    t = product[1]
    o = product[2]
    if o in visited_products:
        continue

    visited_products.add(o)
    last_product = o
    last_product_type = t
    if t == 1:
        rating_start += 1
    else:
        rating_last += 1

print(last_product)
if last_product_type == 1:
    print(rating_last)
else:
    print(rating_last - 1)
