                                            # Третьим шагом создаем модуль module_4_1

from fake_math import divide as div_fake    # импортируем из модуля fake_math функцию divide под новым именем div_fake во избежание ошибки с одинаковым именем функции во втором модуле.
from true_math import divide as div_true    # мпортируем из модуля true_math функцию divide под новым именем div_true

result1 = div_fake(69, 3)       # записываем под четыремя результатами водные параметры для каждой функции div_fake и div_true.
result2 = div_fake(3, 0)
result3 = div_true(49, 7)
result4 = div_true(15, 0)
print(result1)                              # выводим на экран результаты выполнения функций.
print(result2)
print(result3)
print(result4)
                                            # На экране отобразятся: 23.0, Ошибка, 7.0 и Infinite.