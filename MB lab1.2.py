try:
    # Получаем ввод пользователя
    user_input = input("Введите строку с пробелами: ")

    # Преобразуем ввод в нижний регистр
    user_input = user_input.lower()

    # Создаем список 
    char_list = list(user_input)

    # Создаем пустой список для хранения результатов
    char_frequency = []

    # Подсчитываем частоту каждого символа
    for char in set(char_list):
        frequency = char_list.count(char)
        char_frequency.append((char, frequency))

    # Выводим полученный список кортежей
    print(char_frequency)

except Exception as e:
    # Обрабатываем исключения
    print("Произошла ошибка:", e)
