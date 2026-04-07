numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)

total_sum = sum(x for x in numbers if x is not None)

# Длина списка (включая пропуск)
length = len(numbers)

# Среднее арифметическое
average = total_sum / length

# Заменяем None на среднее
numbers[none_index] = average

print("Измененный список:", numbers)
