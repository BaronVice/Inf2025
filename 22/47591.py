ids = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15
]

p_time = [
    5,
    3,
    8,
    2,
    4,
    6,
    2,
    6,
    3,
    1,
    4,
    1,
    3,
    9,
    2
]

depends = [
    [0],
    [0],
    [0],
    [2,3],
    [2,4],
    [0],
    [5],
    [3],
    [7],
    [0],
    [3],
    [3,4],
    [0],
    [7,8],
    [7,9]
]

id_time = dict()
for i in range(len(ids)):
    id_time[ids[i]] = p_time[i]

id_depends = dict()
for i in range(len(ids)):
    id_depends[ids[i]] = depends[i]

results = dict()
def f(id):
    if id in results: return

    results[id] = id_time[id]
    maxx = 0
    for el in id_depends[id]:
        if el != 0:
            f(el)
            maxx = max(maxx, results[el])
    results[id] += maxx

for id in ids:
    f(id)

print(max(results.values()))