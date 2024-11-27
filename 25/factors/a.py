a = [32,3,37,8,2,17,1]

result =[32,3,37,8,2,17,1,100]
for i in range(7):
    for j in range(7):
        result.append(a[i] + a[j])

for i in range(7):
    for j in range(7):
        for k in range(7):
            if i != j and j != k and i != k:
                result.append(a[i] + a[j] + a[k])

for i in range(7):
    for j in range(7):
        for k in range(7):
            for t in range(7):
                if i != j and j != k and i != k :
                    result.append(a[i] + a[j] + a[k])

for total in range(100):
    if total not in result:
        print(total)