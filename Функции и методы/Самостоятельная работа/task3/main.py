def count(items_list, search_value):

    counter = 0  # Инициализируем счётчик
    for item in items_list:  # Проходим по каждому элементу списка
        if item == search_value:  # Если элемент равен искомому значению
            counter += 1  # Увеличиваем счётчик на 1
    return counter  # Возвращаем итоговое количество


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
