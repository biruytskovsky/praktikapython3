def decompress_string(compressed_string):
    decompressed_string = ""
    count = 0  # Переменная для отслеживания количества повторений символа

    for char in compressed_string:
        if char.isdigit():
            count = count * 10 + int(char)  # Обновляем количество повторений
        else:
            if count == 0:
                decompressed_string += char
            else:
                decompressed_string += char * count
                count = 0  # Сбрасываем счетчик повторений

    return decompressed_string

# Пример использования
compressed_string = input("Введите сжатую строку: ")
decompressed_result = decompress_string(compressed_string)
print("Исходная строка:", decompressed_result)