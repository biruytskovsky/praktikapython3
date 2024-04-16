def count_string_repeats(strings):
    # Создаем пустой словарь для подсчета повторений
    counts = {}

    # Подсчитываем количество повторений каждой строки
    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1

    # Выводим количество повторений для каждой строки
    for key in counts:
        print(counts[key], end=" ")


# Примеры работы программы
input1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
input2 = ['aaa', 'bbb', 'ccc']
input3 = ['abc', 'abc', 'abc']

print("Выходные данные для input1:")
count_string_repeats(input1)
print("\nВыходные данные для input2:")
count_string_repeats(input2)
print("\nВыходные данные для input3:")
count_string_repeats(input3)