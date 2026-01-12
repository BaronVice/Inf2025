

# Считать строки с файла
lines = open("D:\\vscode\\Inf2025\\Inf2025\\.9\\demo2026\\task.txt").readlines()
# По условию "Определите сумму чисел в строке с наибольшим номером..." 
# -> наибольший номер это с конца, тогда и перебирать будем с конца. Первую подходящую строку с конца и выведем
lines.reverse()

for line in lines:
    # Распарсить строку
    numbers = list(map(int, line.split()))

    # Количество повторений к числу
    count_to_number = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for number in set(numbers):
        counted = numbers.count(number)
        count_to_number[counted].append(number)
    
    if len(count_to_number[1]) == 4 and len(count_to_number[3]) == 1:
        if sum(count_to_number[1]) / 4 <= count_to_number[3][0]:
            print(sum(numbers))
            break


