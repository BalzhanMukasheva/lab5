try:
    # Входной список
    list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

    # Сортируем список
    sorted_list = sorted(list_A)

    # Вычисляем индексы для разделения
    total_elements = len(sorted_list)
    q1_index = total_elements // 4
    q2_index = q1_index * 2
    q3_index = q1_index * 3

    # Делим на четыре части
    q1 = sorted_list[:q1_index] + [0] * (total_elements % 4)
    q2 = sorted_list[q1_index:q2_index]
    q3 = sorted_list[q2_index:q3_index]
    q4 = sorted_list[q3_index:]

    # Выводим результаты
    print("q1 =", q1)
    print("q2 =", q2)
    print("q3 =", q3)
    print("q4 =", q4)

except Exception as e:
    # Обрабатываем исключения, если они воз