def get_multiplied_digits(number): # записываем функцию et_multiplied_digits, которая будет принимать аргумент целое число number и подсчитывать произведение цифр этого числа.
    number = int(number) # создаем параметр number как целое число.
    str_number = str(number) # создаем переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0]) # создаем переменную first и записываем в неё 1-ый символ из str_number в числовом представлении (int).

    while str_number.endswith('0'): # создаем цикл while для выполнения последовательности, пока проверяем условие что переменная str_number заканчивается 0.
        str_number = str_number[:len(str_number) - 1] # при этом значение переменной str_number принимает число элемента, возвращенное из этой же переменной за минусом 1.
    if len(str_number) > 1: # создаем условие, что возвращенное число элемента переменно str_number больше 1.
        return first * get_multiplied_digits(int(str_number[1:])) # с последующим возвратом переменной first умноженной на целое число переменной str_number, вызванной рекурсией (повторным вызовом созданной функции get_multiplied_digits)
    else: # добавляем дополнительное условие для иных вариантов, когда необходимо возвращать значение переменной first.
        return first

# записываем исходный код согласно данным задачи и выводим на экран результат:
result = get_multiplied_digits(40203)
print(result)