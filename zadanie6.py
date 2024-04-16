def create_acronym(sentence):
    # Разбиваем строку на слова
    words = sentence.split()

    # Инициализируем переменную для хранения аббревиатуры
    acronym = ""

    # Для каждого слова добавляем первую букву (заглавную) в аббревиатуру
    for word in words:
        acronym += word[0].upper()

    return acronym


# Запрашиваем у пользователя ввод строки
input_string = input("Введите строку: ")

# Создаем аббревиатуру и выводим ее
abbreviation = create_acronym(input_string)
print("Аббревиатура:", abbreviation)