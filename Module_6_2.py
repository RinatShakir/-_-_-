class Vehicle:                                                      # Создаем родительский класс Vehicle.
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']   # Внутри род.класса создаем атрубит определения своих цветов машины с заданными параметрами.

    def __init__(self, owner, model, color, engine_power):          # Внутри род.класса Vehicle создаем функцию инициализации конструктора класса для вписания наименований атрибутов.
        self.owner = owner                                          # Создаем внутри функции род.класса атрибут владельца машины.
        self.__model = model                                        # Создаем внутри функции род.класса атрибут модели машины.
        self.__engine_power = engine_power                          # Создаем внутри функции род.класса атрибут мощности двигателя.
        self.__color = color                                        # Создаем внутри функции род.класса атрибут цвета машины.

    def get_model(self):                                            # Создаем внутри род.класса функцию получения информации о модели машины.
        return f"Модель: {self.__model}"                            # Где возвращаем информацию о модели машины.

    def get_horsepower(self):                                       # Создаем внутри род.класса функцию получения информации о мощности двигателя.
        return f"Мощность двигателя: {self.__engine_power}"         # Где возвращаем информацию о мощности двигателя.

    def get_color(self):                                            # Создаем внутри род.класса функцию получения информации о цвете машины.
        return f"Цвет: {self.__color}"                              # Где возвращаем информацию о цвете машины.

    def set_color(self, new_color):                                 # Создаем внутри род.класса функцию установки нового цвета машины.
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]: # Внутри функции создаем условия определения нового цвета автомобиля в пределах аттрибута __COLOR_VARIANTS.
                                                                                    # в условии используем метода вызова нижнего регистра, для того чтобы не обращать внимание на регистры запрашиваемого новго цвета машины.
            self.__color = new_color                                                # определяем в условии атрибут нового цвета.
        else:                                                                       # Создаем прочее условие, если меняемый цвет машины, отсутствует в заданной диапазоне аттрибута новых цветов.
            print(f"Нельзя сменить цвет на {new_color}")                            # в этом случае выводим сообщение о невозможности смены цвета машины.

    def print_info(self):                                           # Создаем внутри род.класса функцию вывода на экран информации по аттрибутам.
        print(self.get_model())                                     # Выводим на экран информацию о моделе машины.
        print(self.get_horsepower())                                # Выводим на экран информацию о мощности двигателя машины.
        print(self.get_color())                                     # Выводим на экран информацию о цвете машины.
        print(f"Владелец: {self.owner}")                            # Выводим на экран информацию о владельце машины.

class Sedan(Vehicle):                                               # Создаем наследный класс Sedan, который наследует аттрибуты от род.класса Vehicle.
    __PASSENGERS_LIMIT = 5                                          # Внутри наследного класса Sedan создаем атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров).

    def __init__(self, owner, model, color, engine_power):          # Внутри наследного класса Sedan создаем функцию инициализации конструктора класса для вписания наименований атрибутов наследного класса.
        super().__init__(owner, model, color, engine_power)         # Внутри функции определяем объект с помощью метода "super().__init__(owner, model, color, engine_power)".

                                                                    # Записываем исходный код:
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

                                                                    # Изначальные свойства:
vehicle1.print_info()

                                                                    # Меняем свойства (в т.ч. вызывая методы):
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

                                                                    # Проверяем, что поменялось:
vehicle1.print_info()