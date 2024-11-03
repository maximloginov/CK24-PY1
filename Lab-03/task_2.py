def find_common_participants(str1, str2, sep=','):
    set1 = set(str1.split(sep))
    set2 = set(str2.split(sep))
    common = set1.intersection(set2)
    return sorted(list(common))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))