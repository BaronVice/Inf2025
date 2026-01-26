
f = open("_26\\Сорвенования_контрольные_точки\\26_23383.txt").readlines()

n = int(f[0])
point_to_men = dict()
for pair in f[1:]:
    man, point = map(int, pair.split())
    if point not in point_to_men:
        point_to_men[point] = set()
    point_to_men[point].add(man)

max_point = 10**10
max_in_row = 0
for point in point_to_men:
    men = list(point_to_men[point])
    men.sort()
    men.append(-1)
    this_max = 1
    for i in range(len(men) - 1):
        if men[i] + 1 == men[i + 1]:
            this_max += 1
        else:
            if max_in_row == this_max and point < max_point:
                max_point = point
            if max_in_row < this_max:
                max_in_row = this_max
                max_point = point
            this_max = 1

print(max_in_row, max_point)
