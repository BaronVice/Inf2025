# https://inf-ege.sdamgia.ru/problem?id=60268

f = open("Inf2025\\_26\\Про_мероприятия\\26_10107.txt").readlines()
n = int(f[0])

events = [list(map(int, f[i].split())) for i in range(1, len(f))]

events.sort() # сортировка по времени начала

# Набираем мероприятия в events_queue
events_queue = [events[0]]

for i in range(1, len(events)):
    # Если мероприятие можно уместить за последним, то добавляем мероприятие
    if events[i][0] >= events_queue[-1][1]:
        events_queue.append(events[i])
    # Если нельзя, то последнее (events_queue[-1]) следует заменить на текущее (events[i]) при условии
    # что оно (events[i]) оканчивается раньше по времени, чем последнее (events_queue[-1])
    elif events[i][1] < events_queue[-1][1]:
        events_queue.pop()
        events_queue.append(events[i])

print(len(events_queue))
# максимальное время: удалим последний из events_queue, добавим последний из events
events_queue.pop()
events_queue.append(events[-1])
print(events_queue[-1][0] - events_queue[-2][1])


