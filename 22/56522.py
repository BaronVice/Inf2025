ids = [
    10075,
    10167,
    10226,
    10235,
    10263,
    10323,
    10353,
    10378,
    10401,
    10452,
    10474,
    10495,
    10565,
    10621,
    10668,
    10751,
    10755,
    10815,
    10884,
    10934,
    11014,
    11045,
    11067,
    11146,
    11243,
    11246,
    11335,
    11411,
    11477,
    11553,
    11557,
    11609,
    11703,
    11733,
    11765,
    11805,
    11810,
    11902,
    11964,
    12046,
    12060,
    12137,
    12224,
    12296,
    12362,
    12431,
    12504,
    12527,
    12599,
    12668,
    12762,
    12816,
    12848,
    12857,
    12890,
    12931,
    12994,
    13025,
    13058,
    13103,
    13138,
    13225,
    13308,
    13379,
    13457,
    13486,
    13522,
    13607,
    13669,
    13758,
    13791,
    13831,
    13893,
    13954,
    14028,
    14070,
    14142,
    14237,
    14270,
    14324,
    14362,
    14461,
    14534,
    14560,
    14622,
    14675,
    14748,
    14765,
    14802,
    14864,
    14921,
    15010,
    15045,
    15143,
    15239,
    15264,
    15317,
    15337,
    15387,
    15396
]

p_time = [
    68,
    86,
    69,
    26,
    66,
    47,
    71,
    95,
    51,
    87,
    18,
    90,
    34,
    26,
    64,
    76,
    41,
    27,
    90,
    11,
    67,
    28,
    97,
    30,
    43,
    91,
    85,
    24,
    61,
    35,
    5,
    42,
    77,
    44,
    71,
    76,
    24,
    12,
    12,
    38,
    1,
    98,
    44,
    82,
    97,
    94,
    49,
    73,
    52,
    72,
    88,
    53,
    84,
    15,
    68,
    59,
    37,
    50,
    79,
    24,
    8,
    83,
    15,
    78,
    64,
    95,
    39,
    27,
    78,
    17,
    37,
    36,
    80,
    10,
    71,
    91,
    71,
    79,
    97,
    19,
    54,
    85,
    18,
    87,
    29,
    93,
    21,
    83,
    44,
    78,
    79,
    63,
    15,
    13,
    29,
    16,
    25,
    6,
    38,
    16
]

depends = [
    [0],
    [0],
    [10075,10167],
    [0],
    [0],
    [10226],
    [0],
    [10226],
    [0],
    [10226],
    [10353,10401],
    [10401],
    [10378,10452],
    [0],
    [10263],
    [10226],
    [10226],
    [0],
    [0],
    [10565,10815],
    [10323],
    [10668,11014],
    [10263,10495],
    [0],
    [10884,11014],
    [11067,11243],
    [11146,11243],
    [0],
    [10495],
    [10474,11243],
    [0],
    [0],
    [11335,11609],
    [0],
    [0],
    [10751],
    [11243,11609],
    [11477],
    [10565,11411],
    [11703],
    [10235],
    [0],
    [0],
    [12137],
    [0],
    [0],
    [11902],
    [11146],
    [0],
    [0],
    [10353,12504],
    [0],
    [0],
    [0],
    [10474],
    [11243,12762],
    [0],
    [11805,12504],
    [11411],
    [10353],
    [12046],
    [0],
    [0],
    [0],
    [10263],
    [0],
    [0],
    [11703],
    [10474,13457],
    [10474,11609],
    [12431,13607],
    [0],
    [12137],
    [13486,13522],
    [11243,13954],
    [0],
    [10378,11146],
    [10226],
    [0],
    [12816],
    [10751,12046],
    [0],
    [14028],
    [0],
    [10621,11733],
    [10934,13791],
    [12046,13025],
    [0],
    [0],
    [0],
    [0],
    [14237,14461],
    [10323,13893],
    [14921],
    [15045,15143],
    [0],
    [10934],
    [12137],
    [11553,11902],
    [0]
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

a = sorted(results.values())
print(a[69])