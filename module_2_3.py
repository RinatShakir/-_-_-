my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # заводим массив из цифр
a = 0 # задаем значение индекса, чтобы впоследствии ограничить действие в рамках длины всего массива
while a < len(my_list): # задаем цикличность, ограничивая длиной массива с помощью функций while и len
    number = my_list[a] # задаем переменную, которую заполним числом из массива по индексу
    if number > 0: # задаем условие что число из массива должно быть больше 0
        print(number) # выводим на экран число из массив, которое больше 0
        a = a + 1 # мы должны перейти к анализу следующего индекса массива, поэтому прибавляем 1.
        continue # нам необходимо вернуться к условию цикла и проигнорировать следующие действия, пока мы не дойдем до цифры 0 в массиве
    if number < 0:  # поскольку у нас есть 0 в массиве и мы к нему вернулись по порядку, ставим условие меньше нуля, чтобы исключить 0
        break  # и впоследствие останавливаемся на 0 и переходим к следующему действию
    else: # ставим условие в остальных случаях перейти к следующему индексу в массиве, чтобы избежать ошибки
        a = a + 1

