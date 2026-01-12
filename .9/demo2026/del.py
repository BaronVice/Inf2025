

lines = open("D:\\vscode\\Inf2025\\Inf2025\\.9\\demo2026\\task.txt").readlines()
s = 0

for line in lines:
    # Распарсить строку
    numbers = list(map(int, line.split()))

    # Количество повторений к числу
    count_to_number = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for number in set(numbers):
        counted = numbers.count(number)
        count_to_number[counted].append(number)
    
    if len(count_to_number[3]) == 1 and len(count_to_number[2]) == 1:
        if max(count_to_number[2][0], count_to_number[3][0]) > max(count_to_number[1]):
            s += 1
print(s)