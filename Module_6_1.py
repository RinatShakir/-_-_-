class Animal:                   # Создаем родительский класс Animal.
    def __init__(self, name):   # Создаем функцию инициализации конструктора класса Animal для вписания имени (нейма).
        self.alive = True       # Создаем внутри класса Animal атрибут alive = True (живой).
        self.fed = False        # Создаем внутри класса Animal атрибут fed = False (накормленный).
        self.name = name        # Создаем внутри класса Animal атрибут name - индивидуальное название каждого животного.

class Plant:                    # Создаем родительский класс Plant.
    def __init__(self, name):   # Создаем функцию инициализации конструктора класса Plant для вписания имени (нейма).
        self.edible = False     # Создаем внутри класса Plant атрибут edible = False (съедобность).
        self.name = name        # Создаем внутри класса Plant атрибут name - индивидуальное название каждого растения.

class Mammal(Animal):           # Создаем класс наследника Mammal от класса Animal.
    def eat(self, food):        # Создаем фукнцию, в которой определяем будет ли животное подкласса Mammal принмать в пищу растение или нет.
        if food.edible:         # Создаем условную конструкцию, что если еда съедобна, то
            print(f"{self.name} съел {food.name}")  # выводим на печать имя животного и имя растения, которое съедобно.
            self.fed = True
        else:                   # Создаем условие невыполнения предыдущего условия,
            print(f"{self.name} не стал есть {food.name}")  # когда на экран выводим информацию о том, что животное не съело наименование растения.
            self.alive = False

class Predator(Animal):         # Создаем класс наследника Predator от класса Animal.
    def eat(self, food):        # Создаем фукнцию, в которой определяем будет ли животное подкласса Predator принмать в пищу растение или нет.
        if food.edible:         # Создаем условную конструкцию, что если еда съедобна, то
            print(f"{self.name} съел {food.name}") # выводим на печать имя животного и имя растения, которое съедобно.
            self.fed = True
        else:                   # Создаем условие невыполнения предыдущего условия,
            print(f"{self.name} не стал есть {food.name}") # когда на экран выводим информацию о том, что дивотное не съело наименование растения.
            self.alive = False

class Flower(Plant):            # Создаем класс наследника Flower от класса Plant.
    def __init__(self, name):   # Создаем функцию инициализации конструктора подкласса Flower для вписания имени (нейма).
        super().__init__(name)  # Внутри функции определяем объект с помощью метода 'super().__init__(name)'.
        self.edible = False     # Также опеределяем несъедобность растений.

class Fruit(Plant):             # Создаем класс наследника Fruit от класса Plant.
    def __init__(self, name):   # Создаем функцию инициализации конструктора подкласса Fruit для вписания имени (нейма).
        super().__init__(name)  # Внутри функции определяем объект с помощью метода 'super().__init__(name)'.
        self.edible = True      # Также определяем съедобность фруктов.

                                # Задаем вводные параметры:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
                                # Выводим на экран необходимую информацию согласно заданию:
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)