# Нам дана структура - назовем ее хранилищем.
# Нам необходимо просмотреть эту структуру и мы должны перебрать каждый элемент.
# При этом нам необходимо суммировать кол-во элементов.

# Создаем функцию, в рамках которой нам необходимо циклом вернуться в эту функцию столько раз, сколько необходимо раскрыть видов хранилищ по задаче.
# (или по другому раскрыть скобки, т.е. хранилищ, кортежей, словарей, и т.д.).

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), 'Hello', ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calc(*args):
    t = 0                                       # для посчета кол-ва элементов мы используем пустой элемент.
    for elem in args:                           # мы должны пройти по этому списку по элементам. Эти элементы будут просматриваться по всем аргументам хранилища.
        if isinstance(elem, (list, tuple, set)): # мы должны произвести сравнение, поэтому берем элемент и проверяем его отношение к таким структурам, как список=LIST, кортеж=TUPLE, множество=SET.
                                                # таким образом, мы проверям элементы хранилища, к какой структуре он относится.
            t = t + calc(*elem)                 # если элемент относится к какому-либо типу из поиска, тогда переменная t должна принмать значение, которое будет присваивать значение "t + значение функции calc".
                                                # сколько у нас будет элементов, столько раз будем обращаться к функции calc. Здесь внутри функции мы обращаемся к этой же функции.
        elif isinstance(elem, dict):            # ставим дополнительное условие, что если элемент относится к струтуре словаря,
            t = t + calc(*elem.items())         # то мы снова должны взять переменную t, которая должна принять значение "t + значение из функции calc" с пересчетом элементов и значений элементов словаря, используя операцию пересчета items.
        elif isinstance(elem, str):             # ставим следующее условие, где мы должны просмотреть ту строку, которая есть, при этом строка будет возвращать длину, и должны посчитать кол-во элементов.
            t = t + len(elem)                   # если элемент имеет тип "Строки", то тогда в переменную t вписывается значение "t + длина этой строки" (с операцией len).
        elif isinstance(elem, (int, float)):    # у нас в хранилище также есть целые числа и нецелые числа, которые мы должны проверить. Поэтому записыввем также данное условие.
            t = t + elem                        # при выполнении условия значение t принимает значение "t + значение самого элемента".
        else:                                   # как только мы дошли до аргумента, значение которого принимает значение None, то мы останавливаем работу цикла.
            pass
    return t                                    # здесь мы долдны сделать возвращение работы функции, но возвратить значение переменной t.

result = calc(data_structure)                   # записываем (определяем) реузльтат работы функции, для последующего вывода результата на экран.
print(result)
# ------------------------------------------------------------------------------------------------------------------------