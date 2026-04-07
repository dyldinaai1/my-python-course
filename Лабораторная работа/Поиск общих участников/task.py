def find_common_participants(group1, group2, delimiter=','):
    # Разбиваем строки на списки, убирая лишние пробелы
    list1 = [name.strip() for name in group1.split(delimiter)]
    list2 = [name.strip() for name in group2.split(delimiter)]
    # Находим пересечение и сортируем
    return sorted(set(list1) & set(list2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, " | "))
