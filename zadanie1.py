def compress_string(s):
    compressed_string = ""
    count = 1  # Счетчик повторений для текущего символа

    # Проходим по всей строке, начиная с первого символа
    for i in range(1, len(s)):
        # Если текущий символ совпадает с предыдущим, увеличиваем счетчик
        if s[i] == s[i - 1]:
            count += 1
        else:
            # Если символ меняется, добавляем количество повторений и предыдущий символ к сжатой строке
            if count > 1:
                compressed_string += s[i - 1] + str(count)
            else:
                compressed_string += s[i - 1]
            count = 1  # Сбрасываем счетчик для нового символа

    # Добавляем последний символ и его количество повторений к сжатой строке
    if count > 1:
        compressed_string += s[-1] + str(count)
    else:
        compressed_string += s[-1]

    return compressed_string


# Пример использования
input_string = input("Введите строку: ")
compressed_result = compress_string(input_string)
print("Сжатая строка:", compressed_result)
