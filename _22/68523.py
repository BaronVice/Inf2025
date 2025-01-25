ids = [
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114
]

p_time = [
    4,
    3,
    1,
    5,
    7,
    3,
    1,
    2,
    8,
    6,
    16,
    5,
    14,
    14
]

depends = [
    [0],
    [0],
    [101,102],
    [103],
    [103],
    [104],
    [105,106],
    [107],
    [0],
    [0],
    [109],
    [110],
    [111,114],
    [109]
]

id_time = dict()
for i in range(len(ids)):
    id_time[ids[i]] = p_time[i]

id_depends = dict()
for i in range(len(ids)):
    id_depends[ids[i]] = depends[i]

results = dict()
timeline = [0 for i in range(1000)]
def f(id):
    if id in results: return

    results[id] = id_time[id]
    maxx = 0
    for el in id_depends[id]:
        if el != 0:
            f(el)
            maxx = max(maxx, results[el])
    results[id] += maxx
    for i in range(maxx, results[id]+1):
        timeline[i] += 1

for id in ids:
    f(id)

print(timeline[:100])