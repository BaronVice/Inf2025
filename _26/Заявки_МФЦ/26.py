

f = open("_26\\Заявки_МФЦ\\26_23283.txt").readlines()

windows = [[] for _ in range(int(f[0]))]
n = int(f[1])

times = []
for i in range(2, len(f)):
    start, finish = map(int, f[i].split())
    times.append([start, finish])

ans1 = 0
ans2 = 0

times.sort()
times.reverse()

for i in range(1, 1440+1):
    for j in range(len(windows)):
        if windows[j] != [] and windows[j][-1] == i - 1:
            windows[j] = []

    taken = []
    while times and times[-1][0] == i:
        time = times.pop()
        for j in range(len(windows)):
            if windows[j] == []:
                ans1 += 1
                taken.append(j + 1)
                windows[j] = time
                break

    if taken:
        ans2 = taken[0]

print(ans1)
print(ans2)
    
