class Figura:                               # Создаем родительский класс Figura и его дальнейшее описание.
    def __init__(self, sides_count = 0):    # Внутри род.класса Figura создаем функцию инициализации конструктора класса для вписания наименований атрибутов.
        self.sides_count = sides_count      # Создаем внутри функции род.класса Figura атрибут slides_count.
        self.__sides = []                   # Создаем внутри функции род.класса Figura атрибут __slides.
        self.__color = []                   # Создаем внутри функции род.класса Figura атрибут __color.
        self.filled = False                 # Создаем внутри функции род.класса Figura атрибут filled со значением boolean False.

    def get_color(self):                    # Внутри род.класса Figura создаем функцию get_color.
        return self.__color                 # Данная функция возвращает аттрибут __color.

    def __is_valid_color(self, r, g, b):    # Внутри род.класса Figura создаем функцию __is_valid_color, которая принимает параметры r, g, b.
        colors = [r, g, b]                  # определяем атрибут colors.
        for color in colors:                # записываем цикл для атрибута colors, где задаем условие,
            if not (0 <= color <= 255):     # что если цвет в диапазоне от 0 до 255, то возвращать False.
                return False
        return True

    def set_color(self, r, g, b):           # Внутри род.класса Figura создаем функцию set_color, которая принимает параметры r, g, b - числа.
        if len(self.__color) == 0:          # и изменяет атрибут __color на соответствующие значения, при условии предварительной проверки их на корректность.
            self.__color = [r, g, b]        # создаем внутри условия атрибут __color с нужными параметрами.

    def __is_valid_sides(self, *sides):     # Внутри род.класса Figura создаем служебную функцию __is_valid_sides.
        if len(sides) != self.sides_count:  # в которой ставим условие, что если длина объекта sides не равно значению sides_count,
            return False                    # то возвращаем False.
        for side in sides:                  # Также внутри функции задаем цикл для объекта side,
            if side <= 0:                   # которое при условии меньшь или равно 0,
                return False                # то возвращает False.
        return True                         # Во всех остальных случаях возвращает True.

    def get_sides(self):                    # Внутри род.класса Figura создаем функцию для метода get_sides,
        return self.__sides                 # которая должна возвращать значение атрибута __sides.

    def __len__(self):                      # Внутри род.класса Figura создаем функцию для метода __len__,
        return len(self.__sides)            # которая должна возвращать значение периметра фигуры.

    def set_sides(self, *new_sides):        # Внутри род.класса Figura создаем функцию для метода set_sides(self, *new_sides), которая должна принимать новые стороны.
        if self.__is_valid_sides(*new_sides):  # При этом также создаем внутри этой функции условие, если количество сторон равно sides_count, то изменять на new_sides.
            self.__sides = new_sides

class Circle(Figura):                       # Создаем наследный класс Circle от класса Figura.
    def __init__(self, radius = 0):         # Внутри наследного класса Circle инициируем атрибуты родительского класса и определяем параметр radius со значением 0.
        super().__init__(sides_count = 1)   # Обращаемся к классу Figura и вызываем его атрибут sides_count, который будет равным 1.
        self.__radius = radius / 2          # Задаем атрибут __radius и определяем как половину атрибута raduis.

    def get_square(self):                   # Внутри наследного класса Circle создаем функцию для метода get_square,
        return 3.14 * (self.__radius ** 2)  # которая возвращает значение площади круга (применяем значение Пи умноженное на радиус в квадрате.

    def set_radius(self, r):                # Внутри наследного класса Circle создаем функцию для метода set_radius
        self.__radius = r                   # с атрибутом __radius = r

    def get_sides(self):                    # Внутри наследного класса Circle создаем функцию для метода get_sides,
        return [self.__radius * 2]          # которая возвращает атрибут __radius * 2.

class Triangle(Figura):                     # Создаем наследный класс Triangle от класса Figura.
    def __init__(self):                     # Внутри наследного класса Triangle инициируем атрибуты родительского класса.
        super().__init__(sides_count = 3)   # Обращаемся к классу Figura и вызываем его атрибут sides_count, который будет равным 3.
        self.__base = 0                     # Определяем атрибут __base, который будет равным 0.
        self.__height = 0                   # Определяем атрибут __height, который будет равным 0.

    def get_square(self):                   # Внутри наследного класса Triangle создаем функцию для метода get_square
        return (self.__base * self.__height) / 2    # где возвращаем значение основания умноженного на высоту и деленного на 2.

class Cube(Figura):                         # Создаем наследный класс Cube от класса Figura.
    def __init__(self, side = 1):           # Внутри наследного класса Cube инициируем атрибуты родительского класса и определяем параметр side со значением 1
        super().__init__(sides_count = 12)  # Обращаемся к классу Figura и вызываем его атрибут sides_count, который будет равным 12.
        self.__side = side                  # Определяем атрибут __side = side.

    def get_sides(self):                    # Внутри наследного класса Cube создаем функцию для метода get_sides,
        return [self.__side] * 12           # которая возвращает значение атрибута __side умноженное на 12.

    def get_volume(self):                   # Внутри наследного класса Cube создаем функцию для метода get_volume,
        return self.__side ** 3             # которая возвращает значение __side в кубе.

    def set_sides(self, side):              # Внутри наследного класса Cube создаем функцию для метода set_sides
        if side <= 0:                       # с условием что если side <= 0,
            return
        self.__side = side                  # то возвращает значение __side = side


circle1 = Circle(15)
cube1 = Cube(6)

circle1.set_color(200, 200, 100)
cube1.set_color(222, 35, 130)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(6)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())